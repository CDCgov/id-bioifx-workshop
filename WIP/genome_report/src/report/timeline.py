import pandas as pd
import plotly.express as px

def plot_timeline(df):
    date_col = 'year_month'
    # parse dates
    df = df.copy()  # avoid modifying original df
        
    # counts per month + subtype
    counts = (
        df.dropna(subset=[date_col, "Clade"])
        .groupby([date_col, "Clade"])
        .size()
        .reset_index(name="n")
        .sort_values(date_col)
    )

    # stacked area chart
    fig = px.area(
        counts,
        x=date_col,
        y="n",
        color="Clade",
        title=f"Clade counts by {date_col}"
    )

    fig.update_layout(
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        xaxis=dict(showgrid=False, zeroline=False),
        xaxis_title=date_col,
        yaxis_title="Number of samples",
        plot_bgcolor="white",   # inside plotting area
        paper_bgcolor="white",  # outside plotting area
    )

    return fig
