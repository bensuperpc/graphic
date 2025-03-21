import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.ticker as ticker

import json

import datetime

from loguru import logger

def linechart_years(data : list, columns : list, categorie_names : list, slices_label_points : list, title : str, xlabel : str, ylabel : str,
               legend_title : str, source : str, 
               dark_mode : bool = True, show_plt : bool = False, save_plt : bool = True) -> None:
    if not isinstance(data, np.ndarray):
        data = np.array(data)

    if len(data.shape) == 1:
        data = np.array([data])
        logger.warning(f"line_chart: data is not a 2d array, it will be converted to a 2d array")

    if len(columns) != len(data[0]):
        raise ValueError(f"Labels count ({len(columns)}) is not equal to categorie_names count ({len(categorie_names)})")

    if len(categorie_names) != len(data):
        raise ValueError(f"Size_names count ({len(categorie_names)}) is not equal to data count ({len(data)})")

    if len(columns) != data.shape[1]:
        raise ValueError(f"Labels count ({len(columns)}) is not equal to data count ({data.shape[1]})")
    
    columns = np.array(columns).astype(int)

    df = pd.DataFrame(data, index=categorie_names, columns=columns).T

    #df = df.sort_values(by=["1"], ascending=False)

    if dark_mode:
        sns.set_theme(style="darkgrid")
        plt.style.use("dark_background")
    else:
        sns.set_theme(style="whitegrid")
        plt.style.use("default")

    fig, ax = plt.subplots()
    fig.set_size_inches(32, 18)
    #fig.set_dpi(240)

    # fig.suptitle(title)
    palette = sns.color_palette("tab10", n_colors=len(categorie_names))
    plot = sns.lineplot(data=df, ax=ax, dashes=False, marker="o", palette=palette, estimator=None, sort=False)

    # Set up the y-axis to be logarithmic
    ax.set_yscale("log", base=10)
    ax.yaxis.set_major_locator(ticker.LogLocator(base=10.0, subs=[5,10], numticks=20))
    #ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    y_fmt = ticker.FormatStrFormatter("%1.0e")
    ax.yaxis.set_major_formatter(y_fmt)

    # Add grid lines for clarity
    ax.xaxis.grid(True, which="major", linestyle="--", linewidth=0.85)
    ax.yaxis.grid(True, which="major", linestyle="--", linewidth=0.85)
    ax.yaxis.set_minor_locator(ticker.LogLocator(base=10.0, subs=np.arange(2, 10)*0.1, numticks=20))
    ax.yaxis.grid(True, which="minor", linestyle=":", linewidth=0.75)

    # Configure x-axis ticks, one year before first and one year after last
    min_year = df.index.min()
    max_year = df.index.max()
    extended_years = np.arange(min_year - 1, max_year + 2)
    ax.set_xlim(min_year - 1, max_year + 1)
    ax.set_xticks(extended_years)
    ax.xaxis.set_minor_locator(ticker.NullLocator())

    for i, size_name in enumerate(categorie_names):
        for j, label in enumerate(columns):
            ax.text(label, data[i][j], slices_label_points[i][j],
                    fontsize=12, verticalalignment="bottom", horizontalalignment="right")

    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.set_title(title, fontsize=17)

    ax.tick_params(axis="both", which="major", labelsize=13)
    ax.legend(title=legend_title, loc="upper left")

    ax.text(0.99, 0.01, source, fontsize=13, color="darkgray", transform=ax.transAxes,
            horizontalalignment="right", verticalalignment="bottom")
    
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

    if save_plt:
        now = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S_%f")[:-3]
        plt.savefig(f"{now}.png", dpi=240)
    
    if show_plt:
        plt.show()


def linechart_generic(data : list, columns : list, categorie_names : list, slices_label_points : list, title : str, xlabel : str, ylabel : str,
               legend_title : str, source : str, 
               dark_mode : bool = True, show_plt : bool = False, save_plt : bool = True) -> None:
    if not isinstance(data, np.ndarray):
        data = np.array(data)

    if len(data.shape) == 1:
        data = np.array([data])
        logger.warning("line_chart: data is not a 2d array, converting to 2d...")

    if len(columns) != len(data[0]):
        raise ValueError(f"Labels count ({len(columns)}) != categorie_names count ({len(categorie_names)})")

    if len(categorie_names) != len(data):
        raise ValueError(f"Size_names count ({len(categorie_names)}) != data count ({len(data)})")

    if len(columns) != data.shape[1]:
        raise ValueError(f"Labels count ({len(columns)}) != data count ({data.shape[1]})")

    columns = np.array(columns).astype(int)
    df = pd.DataFrame(data, index=categorie_names, columns=columns).T

    if dark_mode:
        sns.set_theme(style="darkgrid")
        plt.style.use("dark_background")
    else:
        sns.set_theme(style="whitegrid")
        plt.style.use("default")

    fig, ax = plt.subplots()
    fig.set_size_inches(32, 18)

    palette = sns.color_palette("tab10", n_colors=len(categorie_names))
    sns.lineplot(data=df, ax=ax, dashes=False, marker="o", palette=palette, estimator=None, sort=False)

    # Set axis limits and ticks to ensure text is visible
    ax.set_xlim(columns[0] - 1, columns[-1] + 1)
    ax.set_xticks(columns)

    for i, size_name in enumerate(categorie_names):
        for j, label in enumerate(columns):
            ax.text(label, data[i][j], slices_label_points[i][j],
                    fontsize=13, verticalalignment="bottom", horizontalalignment="right")

    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.set_title(title, fontsize=17)
    ax.tick_params(axis="both", which="major", labelsize=13)
    ax.legend(title=legend_title, loc="upper left")
    ax.text(0.99, 0.01, source, fontsize=13, color="darkgray", transform=ax.transAxes,
            horizontalalignment="right", verticalalignment="bottom")
    
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

    if save_plt:
        now = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S_%f")[:-3]
        plt.savefig(f"{now}.png", dpi=240)
    
    if show_plt:
        plt.show()

def pie_chart_generic(sizes : list, labels : list, title : str, source : str, display_autopct : bool = True, display_legend : bool = True, sort : bool = True, display_labels : bool = False, 
        dark_mode : bool = True, show_plt : bool = False, save_plt : bool = True) -> None:

    if sort:
        labels, sizes = zip(
            *sorted(zip(labels, sizes), key=lambda x: x[1], reverse=True))

    # Check if labels count is equal to sizes count
    if len(labels) != len(sizes):
        raise ValueError(
            f"Labels count ({len(labels)}) is not equal to sizes count ({len(sizes)})")

    explode = None
    # Explode the first slice on only if lower than 50%, otherwise explode all
    if (sizes[0] / sum(sizes)) < 0.5:
        explode = (0.1, 0) + (0,) * (len(labels) - 2)
    # else:
    #    explode = (0.1,) * len(labels)

    if dark_mode:
        sns.set_theme(style="darkgrid")
        plt.style.use("dark_background")
    else:
        sns.set_theme(style="whitegrid")
        plt.style.use("default")

    fig, ax = plt.subplots()
    fig.set_size_inches(32, 18)
    #fig.set_dpi(240)

    autopct = None

    if display_autopct:
        def autopct(p): return f"{p:.2f}%\n {p*sum(sizes)/100 :.0f}"

    pie = None

    palette = sns.color_palette("tab10", n_colors=len(labels))
    if display_labels:
        pie = ax.pie(sizes, labels=labels, autopct=autopct,
                     explode=explode, shadow=True, startangle=90, colors=palette)
    else:
        pie = ax.pie(sizes, autopct=autopct, explode=explode,
                     shadow=True, startangle=90, colors=palette)

    ax.set_title(title)
    # ax.legend(title="Data", loc="upper left")

    if display_legend:
        labels_pie = [
            f"{l}, {((s/sum(sizes)) * 100):0.2f}% ({s})" for l, s in zip(labels, sizes)]

        # Sort the labels by size
        labels_pie, _ = zip(*sorted(zip(labels_pie, sizes),
                                    key=lambda x: x[1], reverse=True))

        ax.legend(pie[0], labels_pie, loc="upper left")


    ax.text(0.99, 0.01, source, fontsize=13, color="darkgray", transform=ax.transAxes,
            horizontalalignment="right", verticalalignment="bottom")
    
    plt.tight_layout()

    if save_plt:
        now = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S_%f")[:-3]
        plt.savefig(f"{now}.png", dpi=240)
    
    if show_plt:
        plt.show()

def filled_line_chart_sns(labels : list, sizes1 : list, sizes2 : list, title : str, xlabel : str, ylabel : str,
        dark_mode : bool = True, show_plt : bool = False, save_plt : bool = True) -> None:

    if len(labels) != len(sizes1):
        raise ValueError(
            f"Labels count ({len(labels)}) is not equal to sizes1 count ({len(sizes1)})")

    if len(labels) != len(sizes2):
        raise ValueError(
            f"Labels count ({len(labels)}) is not equal to sizes2 count ({len(sizes2)})")

    if dark_mode:
        sns.set_theme(style="darkgrid")
        plt.style.use("dark_background")
    else:
        sns.set_theme(style="whitegrid")
        plt.style.use("default")

    fig, ax = plt.subplots()
    fig.set_size_inches(32, 18)
    #fig.set_dpi(240)

    # Plot lines
    #palette = sns.color_palette("tab10", n_colors=len(labels))
    ax.plot(labels, sizes1, color="green")
    ax.plot(labels, sizes2, color="red")

    ax.fill_between(
        labels, sizes1, sizes2, where=(sizes1 > sizes2),
        interpolate=True, color="green", alpha=0.25,
        label="Positive"
    )

    ax.fill_between(
        labels, sizes1, sizes2, where=(sizes1 <= sizes2),
        interpolate=True, color="red", alpha=0.25,
        label="Negative"
    )

    ax.legend(loc="upper left")

    # Set labels title
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)

    # Set title
    ax.set_title(title)

    ax.margins(x=0)
    # plt.margins(x=0)

    ax.text(0.99, 0.01, "", fontsize=13, color="darkgray", transform=ax.transAxes,
            horizontalalignment="right", verticalalignment="bottom")
    
    plt.tight_layout()

    if save_plt:
        now = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S_%f")[:-3]
        plt.savefig(f"{now}.png", dpi=240)
    
    if show_plt:
        plt.show()


def bar_chart_sns(labels : list, sizes : list, title : str, xlabel : str, ylabel : str, display_legend=True, display_grid=True, sort=True,
        dark_mode : bool = True, show_plt : bool = False, save_plt : bool = True) -> None:

    # Sort the labels and sizes by size
    if sort:
        labels, sizes = zip(*sorted(zip(labels, sizes), key=lambda x: x[0]))

    # Check if labels count is equal to sizes count
    if len(labels) != len(sizes):
        raise ValueError(
            f"Labels count ({len(labels)}) is not equal to sizes count ({len(sizes)})")

    df = pd.DataFrame({"labels": labels, "sizes": sizes})

    # df = df.sort_values(by=["1"], ascending=False)

    if dark_mode:
        sns.set_theme(style="darkgrid")
        plt.style.use("dark_background")
    else:
        sns.set_theme(style="whitegrid")
        plt.style.use("default")

    fig, ax = plt.subplots()
    fig.set_size_inches(32, 18)
    #fig.set_dpi(240)

    # fig.suptitle(title)

    palette = sns.color_palette("tab10", n_colors=len(labels))
    plot = sns.barplot(ax=ax, data=df, palette=palette,
                       x="labels", y="sizes")

    # Set labels title
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)

    # Set title
    ax.set_title(title)

    # Add value on top of each bar
    ax.bar_label(ax.containers[0])

    # ax.legend(title="Data", loc="upper left")
    ax.text(0.99, 0.01, "", fontsize=13, color="darkgray", transform=ax.transAxes,
            horizontalalignment="right", verticalalignment="bottom")
    
    plt.tight_layout()

    if save_plt:
        now = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S_%f")[:-3]
        plt.savefig(f"{now}.png", dpi=240)
    
    if show_plt:
        plt.show()


def heatmap_chart_sns(data, title : str, xlabel : str, ylabel : str, xlabels : list, ylabels : list, display_legend=True, display_grid=False,
        dark_mode : bool = True, show_plt : bool = False, save_plt : bool = True) -> None:

    if not isinstance(data, np.ndarray):
        raise ValueError(f"heatmap_chart_sns: data is not a numpy array")

    if len(data.shape) != 2:
        raise ValueError(f"heatmap_chart_sns: data is not a 2d array")

    if len(xlabels) != len(data[0]):
        raise ValueError(
            f"xlabels count ({len(xlabels)}) is not equal to data[0] count ({len(data[0])})")

    if len(ylabels) != len(data):
        raise ValueError(
            f"ylabels count ({len(ylabels)}) is not equal to data count ({len(data)})")

    df = pd.DataFrame(data, columns=xlabels, index=ylabels)

    # df = df.sort_values(by=["1"], ascending=False)

    if dark_mode:
        sns.set_theme(style="darkgrid")
        plt.style.use("dark_background")
    else:
        sns.set_theme(style="whitegrid")
        plt.style.use("default")

    fig, ax = plt.subplots()
    fig.set_size_inches(32, 18)
    #fig.set_dpi(240)

    # fig.suptitle(title)

    #plot = sns.heatmap(ax=ax, data=data, linewidth=0.0, xticklabels=xlabels, yticklabels=ylabels, annot=True, cmap="coolwarm", fmt="g", square= True, cbar=True, cbar_kws={"label": ""})
    plot = sns.heatmap(ax=ax, data=df, linewidth=0.0, annot=True,
                       cmap="crest", fmt="g", square=True, cbar=False)
    plot.set_ylabel(ylabel)
    plot.set_xlabel(xlabel)
    # plot.set_title(title)
    ax.set(title=title)

    ax.text(0.99, 0.01, "", fontsize=13, color="darkgray", transform=ax.transAxes,
            horizontalalignment="right", verticalalignment="bottom")
    
    plt.tight_layout()

    if save_plt:
        now = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S_%f")[:-3]
        plt.savefig(f"{now}.png", dpi=240)
    
    if show_plt:
        plt.show()
