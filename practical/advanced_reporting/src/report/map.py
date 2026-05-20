import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def plot_map(df):
    fig = px.scatter_geo(
        df,
        locations="country",
        locationmode="country names",
        color="Clade",
        hover_name="Sample"
    )

    return fig