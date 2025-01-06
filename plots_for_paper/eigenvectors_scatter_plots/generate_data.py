import numpy as np

import sys
sys.path.append('./')
from utils.graph_laplacian import get_3d_rect_evs

def generate_data_for_eigenvector_scatter_plots(seed):
    np.random.seed(seed)
    x,y,z,EVs = get_3d_rect_evs(n=2000)
    np.save('plots_for_paper/eigenvectors_scatter_plots/data/rect3d_x', x)
    np.save('plots_for_paper/eigenvectors_scatter_plots/data/rect3d_y', y)
    np.save('plots_for_paper/eigenvectors_scatter_plots/data/rect3d_z', z)
    np.save('plots_for_paper/eigenvectors_scatter_plots/data/rect3d_evs', EVs)
    

if __name__ == '__main__':
    generate_data_for_eigenvector_scatter_plots(int(sys.argv[1]))


