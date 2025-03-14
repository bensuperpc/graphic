import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.ticker as ticker

import json

def linechart_years(data : list, title : str, xlabel : str, ylabel : str, legend_title : str, key_data_name : str, 
        x_data_name : str, y_data_name : str, point_data_name : str, source : str,
        dark_mode : bool, save_path : str) -> None:
    
    # Convert data to a DataFrame and to integer types
    df = pd.DataFrame(data)
    df[x_data_name] = df[x_data_name].astype(int)
    df[y_data_name] = df[y_data_name].astype(int)

    # Set up the plotting style
    if dark_mode:
        sns.set_theme(style="darkgrid")
        plt.style.use("dark_background")
    else:
        sns.set_theme(style="whitegrid")
        plt.style.use("default")

    fig, ax = plt.subplots()
    fig.set_size_inches(32, 18)
    #fig.set_dpi(240)

    # Determine unique brands and assign colors
    brands = df[key_data_name].unique()
    palette = sns.color_palette("tab10", n_colors=len(brands))

    # Plot each brand's data and annotate with the point_data_name
    for i, brand in enumerate(brands):
        brand_df = df[df[key_data_name] == brand].sort_values(x_data_name)
        ax.plot(brand_df[x_data_name], brand_df[y_data_name], marker="o", label=brand,
                color=palette[i], linewidth=2.5, markersize=8)
        for _, row in brand_df.iterrows():
            ax.text(row[x_data_name], row[y_data_name], row[point_data_name], fontsize=13,
                    verticalalignment="bottom", horizontalalignment="right")

    # Set up the y-axis to be logarithmic
    ax.set_yscale('log', base=10)
    ax.yaxis.set_major_locator(ticker.LogLocator(base=10.0, subs=[5,10], numticks=20))
    #ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    y_fmt = ticker.FormatStrFormatter('%1.0e')
    ax.yaxis.set_major_formatter(y_fmt)

    # Add grid lines for clarity
    ax.xaxis.grid(True, which="major", linestyle="--", linewidth=0.85)
    ax.yaxis.grid(True, which="major", linestyle="--", linewidth=0.85)
    ax.yaxis.set_minor_locator(ticker.LogLocator(base=10.0, subs=np.arange(2, 10)*0.1, numticks=20))
    ax.yaxis.grid(True, which="minor", linestyle=":", linewidth=0.75)

    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.set_title(title, fontsize=17)

    # Configure x-axis ticks, one year before first and one year after last
    min_year = df[x_data_name].min()
    max_year = df[x_data_name].max()
    extended_years = np.arange(min_year - 1, max_year + 2)
    ax.set_xlim(min_year - 1, max_year + 1)
    ax.set_xticks(extended_years)
    ax.xaxis.set_minor_locator(ticker.NullLocator())

    ax.tick_params(axis="both", which="major", labelsize=13)
    ax.legend(title=legend_title, loc="upper left")

    # Add source text
    ax.text(0.99, 0.01, source, fontsize=13, color="darkgray", transform=ax.transAxes,
            horizontalalignment="right", verticalalignment="bottom")
    
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=240)
    else:
        plt.show()
