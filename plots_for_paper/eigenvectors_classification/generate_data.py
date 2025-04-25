import numpy as np
import pickle
from tqdm import tqdm
import matplotlib.pyplot as plt
import sys
sys.path.append('./')
from utils.graph_laplacian import get_3d_rect_evs
from utils.methods_defs import INDEP_TESTS
from utils.matplotlib_helpers import save_figure

GT = {
    1: [0,1,0],
    2: [0,0,1],
    3: [1,1,0],
    4: [1,0,0],
    5: [1,0,1],
    6: [0,1,1],
    7: [0,1,0],
    8: [1,1,0],
    9: [1,1,1],
    10: [0,0,1],
    11: [1,1,0],
    12: [1,0,1],
    13: [1,0,0],
    14: [0,1,1],
    15: [1,0,1],
    16: [0,1,1],
    17: [0,1,0],
    18: [1,1,1]
}

def plot_ij(EVs, i, j, ax, color=None):
    x,y = EVs[j], EVs[i]
    ax.scatter(x,y, c=color)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(INDEP_TESTS['rtac']().statistic(np.reshape(x, (-1,1)), np.reshape(y, (-1,1))))

def plot_n_by_m(EVs, i_list, j_list, color=None):
    n = len(i_list)
    m = len(j_list)
    fig, axes = plt.subplots(n,m,figsize=(m*3,n*3))
    for ax_i, ev_i in enumerate(i_list):
        for ax_j, ev_j in enumerate(j_list):
            ax = axes[ax_i][ax_j]
            plot_ij(EVs, ev_i, ev_j, ax, color=color)

def generate_data_for_eigenvector_classification(seed):
    np.random.seed(seed)
    methods = {
        key: value() for key,value in INDEP_TESTS.items() if 'hhg' not in key
    }
    
    results = {
        key: {
            'c_plus': [],
            'c_minus': [],
            'all_vals_for_gt_1': [],
            'all_vals_for_gt_0': [],
        } for key in methods.keys()
    }
    
    iterations = 100
    for i in tqdm(range(iterations)):
        x,y,z,EVs = get_3d_rect_evs(n=4000)
        all_vs = EVs[1:20]
        plot_n_by_m(EVs, range(4,20), range(1,4), color=x)
        save_figure(plt.gcf(), f'plots_for_paper/eigenvectors_classification/data/scatters_{i}.pdf')
        plt.close('all')
        
        for name, method in methods.items():
            c_minus = -999
            c_plus = 999
            for key in GT:
                for i, is_good in enumerate(GT[key]):
                    corr_val = method.statistic(np.reshape(all_vs[key], (-1,1)), np.reshape(all_vs[i], (-1,1)))
                    if is_good:
                        c_plus = min(c_plus, corr_val)
                        results[name]['all_vals_for_gt_1'].append(corr_val)
                    else:
                        c_minus = max(c_minus, corr_val)
                        results[name]['all_vals_for_gt_0'].append(corr_val)
            results[name]['c_plus'].append(c_plus)
            results[name]['c_minus'].append(c_minus)
        
        with open(f'plots_for_paper/eigenvectors_classification/data/results.pkl', 'wb') as f:
            pickle.dump(results, f)
    
    
    
if __name__ == '__main__':
    generate_data_for_eigenvector_classification(int(sys.argv[1]))