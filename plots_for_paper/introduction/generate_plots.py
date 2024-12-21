import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import sys
sys.path.append('./')
from utils.matplotlib_helpers import _RCPARAMS_LATEX_SINGLE_COLUMN, save_figure
from utils.common import rank_transform_unbiased
from utils.AreaCoverageIndependenceTest import AreaCoverageIndependenceTest

def plot_squares(x,y,n,do_RT=False,name=None):
    if do_RT:
        x,y=rank_transform_unbiased(x,y)
    gamma=1.2
    with plt.rc_context(rc = _RCPARAMS_LATEX_SINGLE_COLUMN):
        ax = plt.gca()
        fig = plt.gcf()
        edge_length = gamma/np.sqrt(n)
        half_edge_length = edge_length/2
        for i in range(n):
            rect = Rectangle((x[i]-half_edge_length,y[i]-half_edge_length), edge_length, edge_length, fill=True, zorder=2, linewidth=0, edgecolor='black',alpha=0.8)
            ax.add_patch(rect)
        rect = Rectangle((0,0), 1,1, fill=False,edgecolor='black', linewidth=1, zorder=3, linestyle='--')
        ax.add_patch(rect)
        ax.set_xlim([-0.1,1.1])
        ax.set_ylim([-0.1,1.1])
        fig.set_size_inches(6,6)
        ax.scatter(x,y,zorder=5,color='yellow',s=5)
        ax.axis('equal')
        ax.set_xticks([0,1])
        ax.set_yticks([0,1])
        if do_RT:
            eta_n = AreaCoverageIndependenceTest(1).statistic(x,y)
            plt.figtext(0.5, 0.05, f"$\eta_n$ = {round(eta_n, 3)}", ha="center", fontsize=26)
        if name is not None:
            save_figure(fig, name)
        plt.clf()

distributions = ['independent', 'normal', 'circle']
def generate_introduction_plots():
    for dist in distributions:
        x,y = np.load(f'plots_for_paper/introduction/data/{dist}.npy')
        n = x.shape[0]
        plot_squares(x,y,n,name=f'plots_for_paper/introduction/plots/{dist}.pdf')
        plot_squares(x,y,n,do_RT=True,name=f'plots_for_paper/introduction/plots/{dist}_rt.pdf')

if __name__ == '__main__':
    generate_introduction_plots()