import numpy as np
from colour import Color
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

"""
Utility module for creating and visualizing custom color ramps for matplotlib.
"""

RD = '#FF657A'  # Red
OR = '#FF9B5E'  # Orange
YE = '#FFD76D'  # Yellow
GR = '#BAD761'  # Green
BL = '#9CD1BB'  # Blue
PU = '#C39AC9'  # Purple
WH = '#EAF2F1'  # White
GY = "#888D94"  # Gray


def make_ramp(colors: list, name="custom_ramp", plot=False) -> LinearSegmentedColormap:
    """
    Create a matplotlib color ramp from a list of colors.
    """

    color_ramp = LinearSegmentedColormap.from_list(name, [Color(c).rgb for c in colors])
    if plot:
        plot_ramp(color_ramp, len(colors))
    return color_ramp


def plot_ramp(color_ramp: LinearSegmentedColormap, n_colors: int, width=15, height=3):
    """
    Visualize a color ramp.
    """

    plt.figure(figsize=(width, height))
    plt.imshow([list(np.arange(0, n_colors, 0.1))],
               interpolation='nearest', origin='lower', cmap=color_ramp)
    plt.xticks([])
    plt.yticks([])
    plt.show()


def create_predefined_palettes(plot_all=False) -> dict:
    """
    Create and return predefined color palettes.
    """

    categorical_colors = [RD, OR, YE, GR, BL, PU]
    sequential_colors = [WH, YE, OR, RD]
    diverging_colors = [RD, WH, GR]

    palettes = {
        'categorical': make_ramp(categorical_colors, "toutl_categorical"),
        'sequential': make_ramp(sequential_colors, "toutl_sequential"),
        'diverging': make_ramp(diverging_colors, "toutl_diverging")
    }

    if plot_all:
        for name, cmap in palettes.items():
            print(f"Toutl {name} palette:")
            num_colors = {
                'categorical': len(categorical_colors),
                'sequential': len(sequential_colors),
                'diverging': len(diverging_colors)
            }[name]
            plot_ramp(cmap, num_colors)
    else:
        return palettes


TOUTL_PALETTES = create_predefined_palettes(plot_all=False)
