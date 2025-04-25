import numpy as np
import matplotlib.pyplot as plt
from rtacpy import calc_rtac
import sys
sys.path.append('./')
from utils.matplotlib_helpers import _RCPARAMS_LATEX_SINGLE_COLUMN, save_figure


def plot_ij(EVs, i, j, ax, color=None):
    x,y = EVs[j], EVs[i]
    ax.scatter(x,y, c=color, s=5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(f"RTAC = {round(calc_rtac(x,y), 3)}", ha="center", fontsize=14)

def plot_n_by_m(EVs, i_list, j_list, color=None):
    n = len(i_list)
    m = len(j_list)
    fig, axes = plt.subplots(n,m,figsize=(m*3,n*3))
    for ax_i, ev_i in enumerate(i_list):
        for ax_j, ev_j in enumerate(j_list):
            ax = axes[ax_i][ax_j]
            plot_ij(EVs, ev_i, ev_j, ax, color=color)
                
    col_titles = [f'\\textbf{{X Axis - Eigenvector {j}}}' for j in j_list]
    row_titles = [f'\\textbf{{Y Axis - Eigenvector {i}}}' for i in i_list]
    
    for ax, title in zip(axes[0], col_titles):
        ax.set_title(title,fontweight='bold')

    for ax, title in zip(axes[:,0], row_titles):
        ax.set_ylabel(title, size='large',fontweight='bold')




def generate_eigienvectors_scatter_plots():
    x = np.load('plots_for_paper/eigenvectors_scatter_plots/data/rect3d_x.npy')
    EVs = np.load('plots_for_paper/eigenvectors_scatter_plots/data/rect3d_evs.npy')
    with plt.rc_context(rc = _RCPARAMS_LATEX_SINGLE_COLUMN):
        plot_n_by_m(EVs, [4,8,10,14], [1,2,3], color=x)
        save_figure(plt.gcf(), 'plots_for_paper/eigenvectors_scatter_plots/plots/rect3d_selected_evs.pdf')
        plt.close('all')
        plot_n_by_m(EVs, range(1,23), range(1,4), color=x)
        save_figure(plt.gcf(), 'plots_for_paper/eigenvectors_scatter_plots/plots/rect3d_all_evs.pdf')

if __name__ == '__main__':
    generate_eigienvectors_scatter_plots()