import plotly.express as px

def yearly_production_chart(df):

    yearly = (
        df.groupby("Year")["Production"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        yearly,
        x="Year",
        y="Production",
        title="Year-wise Production Trend"
    )

    return fig
