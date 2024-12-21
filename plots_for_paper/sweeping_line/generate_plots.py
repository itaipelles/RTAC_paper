import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import sys
sys.path.append('./')
from utils.matplotlib_helpers import _RCPARAMS_LATEX_SINGLE_COLUMN, save_figure
from utils.common import rank_transform_unbiased


def plot_rects(rects, n, idx_of_chosen_rect):
    ax = plt.gca()
    fig = plt.gcf()
    for i in range(n):
        edge_color = 'black' if i == idx_of_chosen_rect else 'black'
        facecolor = 'green' if i == idx_of_chosen_rect else None
        z_order = 2 if i==idx_of_chosen_rect else 2
        alpha = 0.7 if i==idx_of_chosen_rect else 0.5
        rect = Rectangle(rects[i][0:2], rects[i][2]-rects[i][0], rects[i][3]-rects[i][1], fill=True, zorder=z_order, linewidth=1, edgecolor=edge_color,alpha=alpha, facecolor=facecolor)
        ax.add_patch(rect)
    rect = Rectangle((0,0), 1,1, fill=False,edgecolor='black', linewidth=1, zorder=3, linestyle='--')
    ax.add_patch(rect)
    ax.set_xlim([-0.01,1.01])
    ax.set_ylim([-0.08,1.08])
    fig.set_size_inches(6,6.8)
    ax.axis('off')
    ax.axis('equal')
    ax.set_xticks([])
    ax.set_yticks([])

def plot_just_sweeping_line(rects, half_edge_length, start_of_rect, n):
        # the sweeping line itself
    x_of_line = (n//2)/(n+1) + (-half_edge_length if start_of_rect else half_edge_length)
    plt.vlines(x_of_line, -0.07,1.07,color='orange', linewidth=2)
    
    # the arrow showing the sweeping line's direction of progress
    plt.arrow(x_of_line, -0.035, 0.1, 0, head_width=.03,color='orange')
    
    # dashed lines at each y-axis point of interest
    p_i_ys = [y for rect in rects for y in rect[[1,3]]]
    for p_i_y in p_i_ys:
        plt.plot([0,1],[p_i_y, p_i_y], linestyle='--', linewidth=0.6,zorder=-999,color='black')
    
    # counters to the left of the sweeping line
    delta_x_for_counters=0.025
    sorted_p_i_ys = sorted(p_i_ys)
    middle_points = [0.5*(sorted_p_i_ys[i] + sorted_p_i_ys[i+1]) for i in range(len(sorted_p_i_ys)-1)]
    counters_per_interval_before = [np.sum((rects[:,0]<x_of_line) & (rects[:,2]>=x_of_line) & (rects[:,1]<=middle_y) & (rects[:,3]>=middle_y)) for middle_y in middle_points]
    for y,counter  in zip(middle_points, counters_per_interval_before):
        plt.text(x_of_line-delta_x_for_counters, y-0.015, str(counter))
    
    # change signs to the right of the sweeping line
    counters_per_interval_after = [np.sum((rects[:,0]<=x_of_line) & (rects[:,2]>x_of_line) & (rects[:,1]<=middle_y) & (rects[:,3]>=middle_y)) for middle_y in middle_points]
    delta_counters = np.subtract(counters_per_interval_after, counters_per_interval_before)
    for y,counter  in zip(middle_points, delta_counters):
        plt.text(x_of_line+0.4*delta_x_for_counters, y-0.015, ('+' if counter>0 else '')+str(counter) if counter!=0 else '')

def plot_sweeping_line(x,y,n,do_RT=False,name=None):
    if do_RT:
        x,y=rank_transform_unbiased(x,y)
    gamma=1
    edge_length = gamma/np.sqrt(n)
    half_edge_length = edge_length/2
    rects = np.array([
            (np.maximum(x-half_edge_length,0), 
            np.maximum(y-half_edge_length,0), 
            np.minimum(x+half_edge_length,1), 
            np.minimum(y+half_edge_length,1))]).T.squeeze()
    
    argsort_of_x = np.argsort(x)
    idx_of_chosen_rect_in_argsort = (n//2)-1
    idx_of_chosen_rect = argsort_of_x[idx_of_chosen_rect_in_argsort]
    
    with plt.rc_context(rc = _RCPARAMS_LATEX_SINGLE_COLUMN):
        plot_rects(rects, n, idx_of_chosen_rect)
        plot_just_sweeping_line(rects, half_edge_length, True, n)
        save_figure(plt.gcf(), 'plots_for_paper/sweeping_line/plots/sweeping_line_start_square.pdf')
        plt.clf()
        
        plot_rects(rects, n, idx_of_chosen_rect)
        plot_just_sweeping_line(rects, half_edge_length, False, n)
        save_figure(plt.gcf(), 'plots_for_paper/sweeping_line/plots/sweeping_line_end_square.pdf')

def generate_sweeping_line_plots():
    x,y = np.load('plots_for_paper/sweeping_line/data/rects.npy')
    n = x.shape[0]
    plot_sweeping_line(x,y,n, do_RT=True)

if __name__ == '__main__':
    generate_sweeping_line_plots()