from dash.testing.application_runners import import_app


def test_header_is_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header is not None
    assert header.text == "Pink Morsel Sales Visualizer"


def test_visualisation_is_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


def test_region_picker_is_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None