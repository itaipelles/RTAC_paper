import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('./')
from utils.matplotlib_helpers import _RCPARAMS_LATEX_SINGLE_COLUMN, save_figure


def plot_ij(EVs, i, j, ax, color=None):
    # x,y = rank_transform_unbiased(EVs[i], EVs[j])
    x,y = EVs[i], EVs[j]
    ax.scatter(x,y, c=color)
    ax.set_xticks([])
    ax.set_yticks([])

def plot_n_by_m(EVs, n, m, color=None):
    fig, axes = plt.subplots(n,m,figsize=(m*3,n*3))
    i_offset = 4
    j_offset = 1
    for i in range(n):
        for j in range(m):
            ax = axes[i][j]
            plot_ij(EVs, i+i_offset, j+j_offset, ax, color=color)
            ax.set_title(f'Eigenvectors {i+i_offset} / {j+j_offset}')

def generate_eigienvectors_scatter_plots():
    x = np.load('plots_for_paper/eigenvectors_scatter_plots/data/rect3d_x.npy')
    EVs = np.load('plots_for_paper/eigenvectors_scatter_plots/data/rect3d_evs.npy')
    with plt.rc_context(rc = _RCPARAMS_LATEX_SINGLE_COLUMN):
        plot_n_by_m(EVs, 5, 3, color=x)
        save_figure(plt.gcf(), 'plots_for_paper/eigenvectors_scatter_plots/plots/rect3d_evs_4_to_8.pdf')

if __name__ == '__main__':
    generate_eigienvectors_scatter_plots()