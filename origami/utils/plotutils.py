import fractions

import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def set_pi_ticks(ax, axis, pi_range=(0, 1), divisions=4):
    ticks = np.linspace(pi_range[0], pi_range[1], divisions + 1) * np.pi
    values = [pi_range[0] +
              fractions.Fraction((pi_range[1] - pi_range[0]) * i, divisions) for i in range(divisions + 1)]

    def fraction_to_latex(frac: fractions.Fraction):
        if frac == 1:
            return ''
        if frac.denominator == 1:
            return str(frac.numerator)
        return r'\frac{' + str(frac.numerator) + '}{' + str(frac.denominator) + '}'

    latexs = [fraction_to_latex(f) for f in values]
    labels = ['$ ' + l + r'\pi $' if l != '0' else '0' for l in latexs]

    if 'x' in axis:
        ax.set_xticks(ticks)
        ax.set_xticklabels(labels)
    if 'y' in axis:
        ax.set_yticks(ticks)
        ax.set_yticklabels(labels)


def set_3D_labels(ax: Axes3D):
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


def set_axis_scaled(ax: Axes3D):
    max_lim = max(ax.get_xlim()[1], ax.get_ylim()[1], ax.get_zlim()[1])
    min_lim = min(ax.get_xlim()[0], ax.get_ylim()[0], ax.get_zlim()[0])
    ax.set_xlim(min_lim, max_lim)
    ax.set_ylim(min_lim, max_lim)
    ax.set_zlim(min_lim, max_lim)
