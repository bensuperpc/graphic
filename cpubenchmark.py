import common.reader as reader
import common.linechart as lc

if __name__ == "__main__":
    #reader.json_linechart_years("data_mt.json")
    #reader.json_linechart_years("data_st.json")

    #exit(0)

    days_of_week = ["2018", "2019", "2020", "2021", "2022", "2023", "2024"]

    slices = [[40, 56, 80, 70, 50, 30, 20],
              [50, 60, 70, 80, 90, 100, 110]]
    
    slices_label_points = [["i7-8700K", "i9-9900K", "i9-10900K", "i9-11900K", "i9-12900K", "i9-13900K", "i9-14900K"],
                    ["Ryzen 7 2700X", "Ryzen 7 3700X", "Ryzen 7 4700X", "Ryzen 7 5700X", "Ryzen 7 6700X", "Ryzen 7 7700X", "Ryzen 7 8700X"]]
    
    size_names = ["Intel", "AMD"]

    #lc.linechart_generic(days_of_week, slices, size_names, slices_label_points, "CPU Benchmark", "Année", "Score", "Fabricant", "By Bensuperpc", True, True, False)

    pie_labels = ["Intel", "AMD", "ARM", "Apple"]
    pie_slices = [40, 30, 20, 10]

    lc.pie_chart_generic(pie_labels, pie_slices, "CPU Market Share", "By Bensuperpc", True, True, True, True, 
        True, True, False) 