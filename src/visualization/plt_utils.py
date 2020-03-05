import matplotlib.pyplot as plt


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
    fig1, ax1 = plt.subplots(figsize=(10, 8))
    assert len(y_li) <= 5, "Please select <= 5 series"
    assert len(y_li) == len(labels), "len(y_li) != len(labels)"
    for i in range(len(y_li)):
        ax1.plot(x, y_li[i], markers[i], markersize=10, alpha=0.8, label=labels[i])
        ax1.set_xlabel(xlab)
        ax1.set_ylabel(ylab)
        if ylim:
            ax1.set_ylim(ylim)
        if grid:
            ax1.grid(True)
        if href:
            ax1.axhline(href, linestyle="--", color="k")
        if title:
            ax1.set_title(title)
    ax1.set_xticks(x)
    ax1.legend()
