import json

import common.linechart as lc

if __name__ == "__main__":
    with open("data_mt.json", "r") as file:
        json_data = json.load(file)

    if not json_data:
        print("Error: No data")
    
    linechart_years = []
    linechart_brands = []
    for i, cpu in enumerate(json_data["data"]):
        if cpu["years"] not in linechart_years:
            linechart_years.append(cpu["years"])
        if cpu["brand"] not in linechart_brands:
            linechart_brands.append(cpu["brand"])
    
    linechart_years.sort()
    linechart_brands.sort()

    linechart_slices = []
    linechart_slices_label_points = []

    for i, brand in enumerate(linechart_brands):
        linechart_slices.append([])
        linechart_slices_label_points.append([])
        for j, year in enumerate(linechart_years):
            linechart_slices[i].append(0)
            linechart_slices_label_points[i].append(0)
            for cpu in json_data["data"]:
                if cpu["years"] == year and cpu["brand"] == brand:
                    linechart_slices[i][j] = cpu["score"]
                    linechart_slices_label_points[i][j] = cpu["name"]
                    break
            # If no data for this year, get the previous year data
            if linechart_slices[i][j] == 0 and j > 0:
                linechart_slices[i][j] = linechart_slices[i][j - 1]
                linechart_slices_label_points[i][j] = ""

    lc.linechart_years(linechart_slices, linechart_years, linechart_brands, linechart_slices_label_points, json_data["title"], json_data["xlabel"], json_data["ylabel"], json_data["legend_title"], json_data["source"], True, True, True)


    exit(0)


    linechart_days_of_week = ["2018", "2019", "2020", "2021", "2022", "2023", "2024"]

    linechart_slices = [[40, 56, 80, 70, 50, 680, 4050],
              [50, 60, 70, 80, 90, 500, 4000]]
    
    linechart_slices_label_points = [["i7-8700K", "i9-9900K", "i9-10900K", "i9-11900K", "i9-12900K", "i9-13900K", "i9-14900K"],
                    ["Ryzen 7 2700X", "Ryzen 7 3700X", "Ryzen 7 4700X", "Ryzen 7 5700X", "Ryzen 7 6700X", "Ryzen 7 7700X", "Ryzen 7 8700X"]]
    
    linechart_size_names = ["Intel", "AMD"]

    lc.linechart_years(linechart_slices, linechart_days_of_week, linechart_size_names, linechart_slices_label_points, "CPU Benchmark", "Année", "Score", "Fabricant", "By Bensuperpc", True, True, False)

    pie_labels = ["Intel", "AMD", "ARM", "Apple"]
    pie_slices = [40, 30, 20, 10]

    #lc.pie_chart_generic(pie_slices, pie_labels, "CPU Market Share", "By Bensuperpc", True, True, True, True, 
    #    True, True, False) 