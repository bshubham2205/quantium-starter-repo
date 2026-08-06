import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# Load the processed data
data = pd.read_csv("output.csv")

# Make sure the data is sorted by date
data = data.sort_values("Date")

# Create the line chart
fig = px.line(
    data,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales ($)"
)

# Initialise the Dash app
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="Pink Morsel Sales Visualizer"),
    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)