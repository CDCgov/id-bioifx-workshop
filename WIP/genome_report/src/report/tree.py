import pandas as pd
from Bio import Phylo
import plotly.express as px
import plotly.graph_objects as go

class TreeCoordinates:
    """
    Manages phylogenetic tree coordinates and attributes for visualization.
    
    Attributes:
        tree: Biopython Phylo tree object
        xpos: dict mapping clades to x-coordinates (branch-length distances)
        ypos: dict mapping clades to y-coordinates (vertical positions)
        branch_x: list of x-coordinates for branch segments
        branch_y: list of y-coordinates for branch segments
        tip_x: list of x-coordinates for tip labels
        tip_y: list of y-coordinates for tip labels
        tip_names: list of tip label names
        attr_map: dict mapping attribute names to visualization data
        tip_color_attr: attribute name to use for coloring tips
        tip_colors: list of colors for tips
        tip_color_labels: list of color category labels for tips
    """
    
    def __init__(self, tree):
        """
        Initialize TreeCoordinates with a phylogenetic tree.
        
        Args:
            tree: Biopython Phylo tree object
        """
        self.tree = tree
        self.xpos = {}
        self.ypos = {}
        self.branch_x = []
        self.branch_y = []
        self.tip_x = []
        self.tip_y = []
        self.tip_names = []
        self.attr_map = {}
        self.tip_color_attr = None
        self.tip_colors = []
        self.tip_color_labels = []
        
        self._compute_coordinates()
        self._build_line_segments()
        self._extract_tip_data()
    
    def _compute_coordinates(self):
        """Compute x and y coordinates for all clades in the tree."""
        # Get x-positions (branch-length distances)
        self.xpos = self.tree.depths()
        if not max(self.xpos.values()):
            self.xpos = self.tree.depths(unit_branch_lengths=True)
        
        # Initialize y-positions for terminal nodes (leaves)
        terminals = self.tree.get_terminals()
        self.ypos = dict((leaf, i) for i, leaf in enumerate(terminals))
        
        # Recursively compute y-positions for internal nodes
        def calc_ypos(clade):
            if clade in self.ypos:
                return self.ypos[clade]
            child_y = [calc_ypos(c) for c in clade.clades]
            self.ypos[clade] = sum(child_y) / len(child_y)
            return self.ypos[clade]
        
        calc_ypos(self.tree.root)
    
    def _build_line_segments(self):
        """Build line segments for branches using level-order traversal."""
        xs, ys = [], []
        
        for clade in self.tree.find_clades(order="level"):
            x = self.xpos[clade]
            y = self.ypos[clade]
            
            for child in clade.clades:
                xc = self.xpos[child]
                yc = self.ypos[child]
                
                # Horizontal branch
                xs += [x, xc, None]
                ys += [yc, yc, None]
                
                # Vertical connector
                xs += [x, x, None]
                ys += [y, yc, None]
        
        self.branch_x = xs
        self.branch_y = ys
    
    def _extract_tip_data(self):
        """Extract coordinates and names for terminal nodes."""
        terminals = self.tree.get_terminals()
        self.tip_x = [self.xpos[t] for t in terminals]
        self.tip_y = [self.ypos[t] for t in terminals]
        self.tip_names = [t.name for t in terminals]
    
    def add_attributes(self, df, categories=None, tip_color_attr=None):
        """
        Map sample attributes from a dataframe to tree tips for visualization.

        Rules:
        - tip_color_attr is used ONLY for tip coloring/hover, never as a tile.
        - If no tile categories are provided, no tile traces are generated.
        """
        if df is None or df.empty:
            return

        self.tip_color_attr = tip_color_attr

        # ---- tile categories: only what the user explicitly asked for ----
        # If categories is None or [], then we generate NO tiles.
        tile_categories = list(categories) if categories else []
        # Never tile the tip color attribute (even if user included it)
        if tip_color_attr:
            tile_categories = [c for c in tile_categories if c != tip_color_attr]

        # ---- attributes we will actually extract from df ----
        requested_attrs = set(tile_categories)
        if tip_color_attr:
            requested_attrs.add(tip_color_attr)

        if not requested_attrs:
            # Nothing requested: keep defaults (black tips, no tiles)
            self.tip_colors = ['black'] * len(self.tip_names)
            self.tip_color_labels = [None] * len(self.tip_names)
            self.attr_map = {}
            return

        # Build sample-to-attributes mapping (only requested attrs)
        sample_map = {}
        available_attrs = set()

        for rec in df.to_dict(orient="records"):
            sample = rec.get("Sample")
            if sample and sample in self.tip_names:
                filtered = {k: rec.get(k) for k in requested_attrs if k in rec}
                sample_map[sample] = filtered
                available_attrs.update(filtered.keys())

        # Initialize attr_map for available attrs
        for attr in available_attrs:
            self.attr_map[attr] = {"labels": []}

        # Populate labels in tip order (fill missing with None)
        for tip_name in self.tip_names:
            rec = sample_map.get(tip_name, {})
            for attr in available_attrs:
                self.attr_map[attr]["labels"].append(rec.get(attr))

        # ---- tip colors ----
        if tip_color_attr and tip_color_attr in self.attr_map:
            labels = self.attr_map[tip_color_attr]["labels"]
            self.tip_color_labels = labels

            label_set = set(labels) - {None}
            palette = px.colors.qualitative.Plotly
            color_map = {lab: palette[i % len(palette)] for i, lab in enumerate(label_set)}
            color_map[None] = "black"

            self.tip_colors = [color_map[v] for v in labels]
        else:
            self.tip_colors = ["black"] * len(self.tip_names)
            self.tip_color_labels = [None] * len(self.tip_names)

        # ---- tiles ----
        # Only generate tiles if the user provided tile categories AND those exist
        tile_attrs = [a for a in tile_categories if a in self.attr_map]
        if not tile_attrs:
            return  # no tiles

        tile_offset = 0.3 * (max(self.tip_x) - min(self.tip_x) + 1e-9)
        x_max = max(self.tip_x) + tile_offset * 3

        for attr in tile_attrs:
            labels = self.attr_map[attr]["labels"]

            label_set = set(labels) - {None}
            palette = px.colors.qualitative.Plotly
            color_map = {lab: palette[i % len(palette)] for i, lab in enumerate(label_set)}
            color_map[None] = "lightgray"

            self.attr_map[attr]["colors"] = [color_map[v] for v in labels]

            x_max += tile_offset
            self.attr_map[attr]["x"] = [x_max] * len(self.tip_y)

    
    def get_branch_coordinates(self):
        """Return branch line coordinates as (x_list, y_list)."""
        return self.branch_x, self.branch_y
    
    def get_tip_coordinates(self):
        """Return tip coordinates and names as (x_list, y_list, names_list)."""
        return self.tip_x, self.tip_y, self.tip_names
    
    def get_tip_colors(self):
        """Return tip colors and color category labels."""
        return self.tip_colors, self.tip_color_labels
    
    def get_attributes(self):
        """Return the attribute map dictionary."""
        return self.attr_map


def plot_tree(path, df=None, cat=None, tip_color_attr=None):
    """
    Plot a phylogenetic tree with optional sample attributes.
    
    Args:
        path: path to Newick tree file
        df: pandas DataFrame with sample attributes (optional)
        cat: list of attribute categories to visualize (optional)
        tip_color_attr: column name to use for coloring tips (optional, default=black)
    
    Returns:
        Plotly Figure object
    """
    # Load and root tree
    tree = Phylo.read(path, 'newick')
    tree.root_at_midpoint()
    
    # Create coordinate manager
    coords = TreeCoordinates(tree)
    
    # Add attributes if provided
    if df is not None:
        coords.add_attributes(df, cat, tip_color_attr)
    
    # Build Plotly figure
    fig = go.Figure()
    
    # Add branch lines
    branch_x, branch_y = coords.get_branch_coordinates()
    fig.add_trace(go.Scatter(
        x=branch_x, 
        y=branch_y,
        mode="lines",
        hoverinfo="skip",
        line=dict(width=1, color='black'),
        name="branches",
        showlegend=False
    ))
    
    # Add tip labels
    tip_x, tip_y, tip_names = coords.get_tip_coordinates()
    tip_colors, tip_color_labels = coords.get_tip_colors()
    
    # Build hover template
    if coords.tip_color_attr and tip_color_labels[0] is not None:
        hovertemplate = "%{text}<br>" + f"{coords.tip_color_attr}: %{{customdata}}<extra></extra>"
        customdata = tip_color_labels
    else:
        hovertemplate = "%{text}<extra></extra>"
        customdata = None
    
    fig.add_trace(go.Scatter(
        x=tip_x, 
        y=tip_y,
        mode="markers",
        text=tip_names,
        customdata=customdata,
        hovertemplate=hovertemplate,
        marker=dict(
            size=8,
            color=tip_colors
        ),
        name="tips",
        showlegend=False
    ))
    
    # Add attribute tiles (ONLY attrs that actually have tile coords/colors)
    attr_map = coords.get_attributes()
    for attr_name, attr_data in attr_map.items():
        # Never render tip_color_attr as a tile
        if attr_name == tip_color_attr:
            continue
        # Only render tiles if they were generated (x/colors present)
        if "x" not in attr_data or "colors" not in attr_data:
            continue

        fig.add_trace(go.Scatter(
            x=attr_data["x"],
            y=tip_y,
            mode="markers",
            marker=dict(
                symbol="square",
                size=20,
                color=attr_data["colors"]
            ),
            customdata=attr_data["labels"],
            hovertemplate=f"{attr_name}: %{{customdata}}<extra></extra>",
            name=attr_name
        ))

    
    # Update layout
    fig.update_layout(
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        xaxis=dict(showgrid=False, zeroline=False),
        xaxis_title="Divergence",
        plot_bgcolor="white",   # inside plotting area
        paper_bgcolor="white",  # outside plotting area
        height=600
    )
    
    fig.write_html("figure.html")
    
    return fig