import matplotlib.pyplot as plt
import numpy as np


def bar_plot(x, y_li, labels, xlab, ylab, ylim=None, grid=False, href=None, title=None):
    """Simple bar plot for up to 5 series/groups.
    
    Args:
        x (list:string): list of data points x-coordinates
        y_li (list:list:float): list or list of lists of data points y-coordinates
        xlab (string): label for x-axis
        ylab (string): label for y-axis
        ylim (list:float, optional): optional limiter for y-axis
        labels (list:string): labels for each series
        grid (bool, optional): whether you would like a grid.
        href (float, optional): whether you would like a horizontal ref. line.
        title (string, optional): chart title
    """

    markers = ["g", "b", "r", "k", "c"]
    fig, ax = plt.subplots(figsize=(10, 8))
    assert len(y_li) <= 5, "Please select <= 5 series"
    assert len(y_li) == len(labels), "len(y_li) != len(labels)"
    assert len(y_li[0]) == len(x), "len(y_li[i]) != len(x)"
    x_int = np.arange(len(x))
    w = 0.8 / len(y_li)
    adj = np.array([-2 * w, -3 / 2 * w, -w, -w / 2, 0, w / 2, w, 3 * w / 2, 2 * w])
    x_adj = adj[5 - len(y_li) : len(adj) - (5 - len(y_li)) : 2]
    for i in range(len(y_li)):
        ax.bar(
            x_int + x_adj[i], y_li[i], w, label=labels[i],
        )
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    if ylim:
        ax.set_ylim(ylim)
    if grid:
        ax.grid(True)
    if href:
        ax.axhline(href, linestyle="--", color="k")
    if title:
        ax.set_title(title)
    ax.set_xticks(x_int)
    ax.set_xticklabels(x)
    ax.legend()


def scatter_plot(
    x, y_li, labels, xlab, ylab, ylim=None, grid=False, href=None, title=None
):
    """Simple scatter plot for up to 5 series with same x-axis.
    
    Args:
        x (list:float): list of data points x-coordinates
        y_li (list:list:float): list or list of lists of data points y-coordinates
        xlab (string): label for x-axis
        ylab (string): label for y-axis
        ylim (list:float, optional): optional limiter for y-axis
        labels (list:string): labels for each series
        grid (bool, optional): whether you would like a grid.
        href (float, optional): whether you would like a horizontal ref. line.
        title (string, optional): chart title
    """

    markers = ["go", "bo", "ro", "ko", "co"]
    fig, ax = plt.subplots(figsize=(10, 8))
    assert len(y_li) <= 5, "Please select <= 5 series"
    assert len(y_li) == len(labels), "len(y_li) != len(labels)"
    for i in range(len(y_li)):
        ax.plot(x, y_li[i], markers[i], markersize=10, alpha=0.8, label=labels[i])
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    if ylim:
        ax.set_ylim(ylim)
    if grid:
        ax.grid(True)
    if href:
        ax.axhline(href, linestyle="--", color="k")
    if title:
        ax.set_title(title)
    ax.set_xticks(x)
    ax.legend()
