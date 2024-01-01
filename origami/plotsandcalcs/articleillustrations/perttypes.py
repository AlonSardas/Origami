import os

import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

from origami import origamiplots
from origami.plotsandcalcs.alternating.utils import create_perturbed_origami, create_MM_from_list, create_F_from_list
from origami.plotsandcalcs.articleillustrations import FIGURES_PATH
from origami.utils import plotutils


def plot_F_const():
    F = lambda x: 0.3
    MM = None

    L0 = 1
    C0 = 1.3

    rows, cols = 6, 6
    angle = 1
    ori = create_perturbed_origami(angle, rows, cols, L0, C0, F, MM)

    fig: Figure = plt.figure(figsize=(7, 8))
    ax: Axes3D = fig.add_subplot(111, projection="3d",
                                 elev=60, azim=-108,
                                 computed_zorder=False)

    plot_flat(ax, ori)

    ori.set_gamma(ori.calc_gamma_by_omega(0.8))
    ori.dots.dots[1, :] += 5
    ori.dots.dots[2, :] += 2
    panels, surf = ori.dots.plot(ax, alpha=1.0)
    surf.set_alpha(0.3)

    ax.set_aspect("equal")

    ax.set_position([-0.1, 0, 1.15, 1])

    # fig.patch.set_facecolor('xkcd:mint green')
    # ax.patch.set_facecolor('#4545FF')

    # fig.tight_layout()
    mpl.rcParams["savefig.bbox"] = "standard"
    fig.savefig(os.path.join(FIGURES_PATH, "pert-F-only.svg"))
    fig.savefig(os.path.join(FIGURES_PATH, "pert-F-only.pdf"))

    plt.show()


def plot_M_only():
    F = None
    Ms = np.append(0, np.cumsum([-1.2, -0.2, 0.8, 2.3, 0.1, -0.4]))
    MM = create_MM_from_list(Ms)

    L0 = 1.5
    C0 = 1.3

    rows = 12
    cols = 6
    angle = 1.3
    omega = 0.8
    ori = create_perturbed_origami(angle, rows, cols, L0, C0, F, MM)

    fig: Figure = plt.figure(figsize=(7.5, 6))
    ax: Axes3D = fig.add_subplot(111, projection="3d",
                                 elev=53, azim=-1596,
                                 computed_zorder=False)

    plot_flat(ax, ori)

    ori.set_gamma(ori.calc_gamma_by_omega(omega))
    ori.dots.dots[0, :] += 7
    ori.dots.dots[1, :] -= 3
    ori.dots.dots[2, :] += 3
    panels, surf = ori.dots.plot(ax, alpha=1.0)
    surf.set_alpha(0.3)

    # plotutils.set_labels_off(ax)
    ax.set_aspect("equal")

    ax.set_position([-0.1, -0.15, 1.15, 1.4])

    # fig.patch.set_facecolor('xkcd:mint green')
    # ax.patch.set_facecolor('#4545FF')

    # fig.tight_layout()
    mpl.rcParams["savefig.bbox"] = "standard"
    fig.savefig(os.path.join(FIGURES_PATH, "pert-M-only.svg"))
    fig.savefig(os.path.join(FIGURES_PATH, "pert-M-only.pdf"))

    plt.show()


def plot_F_change_M_const_column():
    F = create_F_from_list(np.array([0.15, 0.4, -0.3]))
    Ms = np.append(0, np.cumsum([-0.5, -0.5, -0.5]))
    MM = create_MM_from_list(Ms)

    L0 = 1.3
    C0 = 1.0

    rows = 6
    cols = 2
    angle = 1.1
    omega = 0.4
    ori = create_perturbed_origami(angle, rows, cols, L0, C0, F, MM)

    fig: Figure = plt.figure(figsize=(7, 6.5))
    ax: Axes3D = fig.add_subplot(111, projection="3d",
                                 elev=46, azim=-128,
                                 computed_zorder=False)

    plot_flat(ax, ori)

    ori.set_gamma(ori.calc_gamma_by_omega(omega))
    ori.dots.dots[0, :] += 1
    ori.dots.dots[1, :] -= 1
    ori.dots.dots[2, :] += 2
    panels, surf = ori.dots.plot(ax, alpha=1.0)
    surf.set_alpha(0.3)

    # plotutils.set_labels_off(ax)
    ax.set_aspect("equal")
    # ax.set(zticks=[-0.5, 0, 0.5])

    ax.set_position([-0.1, -0.15, 1.15, 1.4])

    # fig.patch.set_facecolor('xkcd:mint green')
    # ax.patch.set_facecolor('#4545FF')

    # fig.tight_layout()
    mpl.rcParams["savefig.bbox"] = "standard"
    fig.savefig(os.path.join(FIGURES_PATH, "pert-F-change-M-const.svg"))
    fig.savefig(os.path.join(FIGURES_PATH, "pert-F-change-M-const.pdf"))

    plt.show()


def plot_M_change_F_const_row():
    F = lambda x: 0.25
    Ms = np.append(0, np.cumsum([1.1]))
    MM = create_MM_from_list(Ms)

    L0 = 0.8
    C0 = 1.0

    rows, cols = 2, 6
    angle = 1.1
    omega = 0.8
    ori = create_perturbed_origami(angle, rows, cols, L0, C0, F, MM)

    fig: Figure = plt.figure(figsize=(7.5, 6))
    ax: Axes3D = fig.add_subplot(111, projection="3d",
                                 elev=44, azim=-114,
                                 computed_zorder=False)

    plot_flat(ax, ori)

    ori.set_gamma(ori.calc_gamma_by_omega(omega))
    ori.dots.dots[0, :] -= 0.6
    ori.dots.dots[1, :] += 1
    ori.dots.dots[2, :] += 2
    panels, surf = ori.dots.plot(ax, alpha=1.0)
    surf.set_alpha(0.3)

    # plotutils.set_labels_off(ax)
    ax.set_aspect("equal")
    # ax.set(zticks=[-0.5, 0, 0.5])

    ax.set_position([-0.1, -0.15, 1.15, 1.4])

    # fig.patch.set_facecolor('xkcd:mint green')
    # ax.patch.set_facecolor('#4545FF')

    # fig.tight_layout()
    mpl.rcParams["savefig.bbox"] = "standard"
    fig.savefig(os.path.join(FIGURES_PATH, "pert-M-change-F-const.svg"))
    fig.savefig(os.path.join(FIGURES_PATH, "pert-M-change-F-const.pdf"))

    plt.show()


def plot_flat(ax, ori):
    ori.set_gamma(ori.calc_gamma_by_omega(0))
    panels, surf = ori.dots.plot(ax, alpha=0.6)
    surf.set_alpha(0)
    panels.set_fc('C7')
    panels.set_zorder(-10)
    origamiplots.draw_creases(ori, 1, ax)
    _set_XY_labels(ax)
    plotutils.remove_tick_labels(ax)


def _set_XY_labels(ax: Axes3D):
    ax.set_xlabel('Xsdfsdfsd')
    ax.set_ylabel('Y')


def main():
    # plot_F_const()
    # plot_M_only()
    plot_F_change_M_const_column()
    plot_M_change_F_const_row()


if __name__ == '__main__':
    main()