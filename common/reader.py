import json

from . import linechart_years as linechart_years

def json_linechart_years(file_path: str) -> None:
    '''Reads a JSON file and creates a line chart from the data in the file'''

    if not file_path.endswith(".json"):
        raise ValueError("File must be a JSON file")
    
    json_data = None

    with open(file_path, "r") as f:
        json_data = json.load(f)
    
    if json_data is None:
        raise ValueError("Invalid JSON data: Empty json file: " + file_path)
    if "data" not in json_data:
        raise ValueError("Invalid JSON data: Missing 'data' key")
    if "title" not in json_data:
        raise ValueError("Invalid JSON data: Missing 'title' key")
    if "xlabel" not in json_data:
        raise ValueError("Invalid JSON data: Missing 'xlabel' key")
    if "ylabel" not in json_data:
        raise ValueError("Invalid JSON data: Missing 'ylabel' key")
    if "legend_title" not in json_data:
        raise ValueError("Invalid JSON data: Missing 'legend_title' key")
    if "categories_data_name" not in json_data:
        raise ValueError("Invalid JSON data: Missing 'categories_data_name' key")
    if "x_data_name" not in json_data:
        raise ValueError("Invalid JSON data: Missing 'x_data_name' key")
    if "y_data_name" not in json_data:
        raise ValueError("Invalid JSON data: Missing 'y_data_name' key")
    if "point_data_name" not in json_data:
        raise ValueError("Invalid JSON data: Missing 'point_data_name' key")
    if "source" not in json_data:
        raise ValueError("Invalid JSON data: Missing 'source' key")
    if "dark_mode" not in json_data:
        raise ValueError("Invalid JSON data: Missing 'dark_mode' key")

    data = json_data["data"]
    title = json_data["title"]
    xlabel = json_data["xlabel"]
    ylabel = json_data["ylabel"]
    legend_title = json_data["legend_title"]
    categories_data_name = json_data["categories_data_name"]
    x_data_name = json_data["x_data_name"]
    y_data_name = json_data["y_data_name"]
    point_data_name = json_data["point_data_name"]
    source = json_data["source"]
    dark_mode = json_data["dark_mode"]

    linechart_years(data, title, xlabel, ylabel, legend_title, categories_data_name, x_data_name, y_data_name, point_data_name, source, dark_mode, False, True)

