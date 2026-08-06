import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# Load the processed data
data = pd.read_csv("output.csv")
data = data.sort_values("Date")

# Initialise the Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div(
    style={
        "backgroundColor": "#fdf6f0",
        "fontFamily": "Arial, sans-serif",
        "padding": "40px",
        "textAlign": "center"
    },
    children=[
        html.H1(
            children="Pink Morsel Sales Visualizer",
            style={
                "color": "#d6336c",
                "marginBottom": "10px"
            }
        ),
        html.P(
            "Explore how Pink Morsel sales changed before and after the price increase on 15 Jan 2021.",
            style={"color": "#555", "marginBottom": "30px"}
        ),

        # Radio buttons for region filter
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"},
            ],
            value="all",
            inline=True,
            style={"marginBottom": "30px", "fontSize": "18px"},
            labelStyle={"marginRight": "20px", "cursor": "pointer"}
        ),

        # Line chart
        dcc.Graph(id="sales-line-chart")
    ]
)


# Callback to update chart based on selected region
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["Region"] == selected_region]

    fig = px.line(
        filtered_data,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time ({selected_region.capitalize()})"
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales ($)",
        plot_bgcolor="#fffaf7",
        paper_bgcolor="#fffaf7",
        title_x=0.5
    )
    fig.update_traces(line_color="#d6336c")

    return fig


if __name__ == "__main__":
    app.run(debug=True)