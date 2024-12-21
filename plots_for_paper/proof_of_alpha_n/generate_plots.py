import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import sys
sys.path.append('./')
from utils.common import rank_transform_unbiased
from utils.matplotlib_helpers import _RCPARAMS_LATEX_SINGLE_COLUMN, save_figure


def generate_alpha_n_proof_plots():
    n=19
    edge_length = np.sqrt(1/n)
    x = [i for i in range(n)]
    y = [i for i in range(n)]
    x,y = rank_transform_unbiased(x,y)
    
    with plt.rc_context(rc = _RCPARAMS_LATEX_SINGLE_COLUMN):
        ax = plt.gca()
        fig = plt.gcf()
        half_edge_length = edge_length/2
        for i in range(n):
            rect = Rectangle((x[i]-half_edge_length,y[i]-half_edge_length), edge_length, edge_length, fill=True, zorder=2, linewidth=0, edgecolor='black',alpha=0.8)
            ax.add_patch(rect)
        rect = Rectangle((0,0), 1,1, fill=False,edgecolor='black', linewidth=1, zorder=3, linestyle='--')
        ax.add_patch(rect)
        ax.set_xlim([-0.1,1.1])
        ax.set_ylim([-0.1,1.1])
        fig.set_size_inches(8,8)
        ax.scatter(x,y,zorder=5,color='yellow',s=5)
        ax.axis('equal')
        ax.set_xticks([0,1])
        ax.set_yticks([0,1])

        L = edge_length
        q = 1/(n+1)
        H = 0.5*L

        num_overlap1 = int(H//q)

        c = L - q
        left_over = num_overlap1*q + H - c

        plt.plot([0,c],[0,0], color='r',zorder=10)
        plt.plot([0,0],[0,c], color='r',zorder=10)
        plt.plot([1-c,1],[1,1], color='r',zorder=10)
        plt.plot([1,1],[1-c,1], color='r',zorder=10)

        plt.plot([c,1],[0,1-c], color='r')
        plt.plot([0,1-c],[c,1], color='r')
        plt.plot([0,c],[c,0], color='r')
        plt.plot([1-c,1],[1,1-c], color='r')

        plt.plot([c,c+left_over],[0,0], color='b',zorder=10)
        plt.plot([0,0],[c,c+left_over], color='b',zorder=10)
        plt.plot([1-c-left_over,1-c],[1,1], color='b',zorder=10)
        plt.plot([1,1],[1-c-left_over,1-c], color='b',zorder=10)

        plt.plot([c+left_over,c+left_over],[0,left_over], color='b',zorder=10)
        plt.plot([0,left_over],[c+left_over,c+left_over], color='b',zorder=10)
        plt.plot([1-c-left_over,1-c-left_over],[1-left_over,1], color='b',zorder=10)
        plt.plot([1-left_over,1],[1-c-left_over,1-c-left_over], color='b',zorder=10)

        for i in range(0, n - 2*num_overlap1):
            plt.plot([c+left_over+i*q,c+left_over+q+i*q],[left_over+i*q,left_over+i*q], color='g',zorder=10)
            plt.plot([left_over+i*q,left_over+i*q],[c+left_over+i*q,c+left_over+q+i*q], color='g',zorder=10)
            plt.plot([c+left_over+q+i*q,c+left_over+q+i*q],[left_over+i*q,left_over+i*q+q], color='g',zorder=10)
            plt.plot([left_over+i*q,left_over+i*q+q],[c+left_over+q+i*q,c+left_over+q+i*q], color='g',zorder=10)

        plt.text(c/2, -0.03, 'C')
        plt.text(-0.03, c/2, 'C')
        plt.text(1-c + c/2, 1.01, 'C')
        plt.text(1.01, 1-c + c/2, 'C')



        plt.text(c + (1-c)/2, -0.03, '1-C')
        plt.text(-0.07, c + (1-c)/2, '1-C')
        plt.text((1-c)/2, 1.01, '1-C')
        plt.text(1.01, (1-c)/2, '1-C')

        plt.text(c/3, c/3, 'D')
        plt.text(1-c+0.55*c, 1-c+0.55*c, 'D')

        plt.text(c+(1-c)/2+0.005, (1-c)/2-0.02, 'E')
        plt.text((1-c)/2-0.025, c+(1-c)/2+0.005, 'E')
        
        save_figure(fig, 'plots_for_paper/proof_of_alpha_n/plots/proof_of_alpha_n.pdf')

if __name__ == '__main__':
    generate_alpha_n_proof_plots()