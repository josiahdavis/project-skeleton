# -*- coding: utf-8 -*-

"""Base functionality for three different types of charts.

Includes plot (for line chart and scatter), hist, and bar.

"""

from functools import partial
import matplotlib.pyplot as plt
import numpy as np

_COLORS = ["g", "b", "r", "k", "c"]


def hist(x, title, xlab, ax=None, bins=10, grid=False, ylab="Count", **kwargs):
    """Create a simple histogram.

    Args:
        x (array): Data to create bins and counts for.
        title (str): Descriptive title for the chart.
        xlab (str): Descriptive x label.
        ax (Axes, optional): A matplotlib Axes object.
        bins (int or list:float, optional): the number or actual bins to count data in.
            Default to 10.
        grid (bool, optional): whether you would like a bacground grid.
            Defaults to false.
        ylab (str, optional): Y axis value.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        Axes object: for more detail see matplotlib docs:
            https://matplotlib.org/3.1.1/api/index.html#the-object-oriented-api
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 8))
    ax.hist(x, bins=bins, **kwargs)
    if not isinstance(bins, int) and len(bins) <= 20:
        ax.set_xticks(bins)
    ax.grid(grid)
    ax.set_title(title)
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    return ax


def bar(
    x,
    y_li,
    labels,
    xlab,
    ylab,
    ax=None,
    ylim=None,
    grid=False,
    href=None,
    title=None,
    overlap=False,
    colors=_COLORS,
    **kwargs
):
    """Create a bar plot for up to 5 series/groups.

    Args:
        x (list:string): list of group labels for x axis.
        y_li (list[:list]:float): list or list of lists of data points y-coordinates.
        labels (list:str): labels for each series to be displayed on legend.
        xlab (string): label for x-axis
        ylab (string): label for y-axis
        ax (Axes, optional): A matplotlib Axes object.
        ylim (list:float, optional): optional limiter for y-axis.
        grid (bool, optional): whether you would like a bacground grid.
            Defaults to false.
        href (float, optional): whether you would like a horizontal ref. line.
        title (string, optional): chart title
        overlap (bool, optional): Come back.
        colors (list:str, optional): Colors for the bars.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        Axes object: for more detail see matplotlib docs:
            https://matplotlib.org/3.1.1/api/index.html#the-object-oriented-api
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 8))
    assert len(y_li) <= 5, "Please select <= 5 series"
    assert len(y_li) == len(labels), "len(y_li) != len(labels)"
    assert len(y_li[0]) == len(x), "len(y_li[i]) != len(x)"
    x_int = np.arange(len(x))
    w = 0.8 / len(y_li)
    adj = np.array([-2 * w, -3 / 2 * w, -w, -w / 2, 0, w / 2, w, 3 * w / 2, 2 * w])
    x_adj = adj[5 - len(y_li) : len(adj) - (5 - len(y_li)) : 2]

    if overlap:
        x_adj = np.zeros_like(x_adj)
        w *= len(y_li)
    for i in range(len(y_li)):
        ax.bar(x_int + x_adj[i], y_li[i], w, label=labels[i], color=colors[i], **kwargs)
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
    return ax


def plot(
    x_li,
    y_li,
    labels,
    xlab,
    ylab,
    ax=None,
    ylim=None,
    xlim=None,
    href=None,
    vref=None,
    title=None,
    set_xticks=False,
    marker_type="-",
    markers=None,
    grid=False,
    **kwargs
):
    """Create a line chart or scatter for up to 5 series/groups.

    Args:
        x_li (list[:list]:string): list or list of lists of data points x-coordinates.
        y_li (list[:list]:float): list or list of lists of data points y-coordinates.
        labels (list:str): labels for each series to be displayed on legend.
        xlab (string): label for x-axis
        ylab (string): label for y-axis
        ax (Axes, optional): A matplotlib Axes object.
        xlim (list:float, optional): optional limiter for x-axis
        ylim (list:float, optional): optional limiter for y-axis
        href (float, optional): horizontal ref. line.
        vref (float, optional): vertical ref. line.
        title (string, optional): chart title
        set_xticks (bool, optional): Whether xticks should be set based
            off of the x data. Only useful when there are few unique data
            points (e.g., 10).
        marker_type (string, optional): Common options are: '-' (line),
            '--' (dashed line), and 'o' (scatter).
            See matplotlib docs for complete list.
            https://matplotlib.org/3.1.1/api/markers_api.html
            Will be overidden markers are specified.
        markers (list:string, optional): Marker types using the standard shorthand.
            Useful when compariing multiple types of objects.
            For example, compariing  models and hypers in the same chart.
        grid (bool, optional): whether you would like a bacground grid.
            Defaults to false.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        Axes object: for more detail see matplotlib docs:
            https://matplotlib.org/3.1.1/api/index.html#the-object-oriented-api
    """
    assert len(y_li) == len(labels), "len(y_li) != len(labels)"
    if markers is None:
        markers = [m + marker_type for m in _COLORS]
    assert len(markers) >= len(y_li), "len(markers) < len(y_li)"
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 8))
    for i in range(len(y_li)):
        if len(x_li) == 1:
            x = x_li[0]
        else:
            x = x_li[i]
        ax.plot(x, y_li[i], markers[i], label=labels[i], **kwargs)
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    ax.grid(grid)
    ax.set_title(title)
    if ylim:
        ax.set_ylim(ylim)
    if xlim:
        ax.set_xlim(xlim)
    if vref:
        ax.axvline(vref, linestyle="--", color="gray")
    if href:
        ax.axhline(href, linestyle="--", color="gray")
    if set_xticks:
        ax.set_xticks(x)
    ax.legend()
    return ax


def subplots(ncols=1, nrows=1, figsize=(8, 8), **kwargs):
    """For creating subplots.

    Args:
        ncols (int, optional): Number of columns.
        nrows (int, optional): Number of rows.
        figsize (tuple:int, optional): size for entire chart.
            Counterintuitively, but in keeping with matplotlib
            convention, specified as (width, height).

    Returns:
        A tuple consisting of a matplotlib figure and a
        matplotlib Axes array.
    """
    return plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize, **kwargs)
