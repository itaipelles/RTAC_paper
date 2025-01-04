import numpy as np

import sys
sys.path.append('./')

def get_line_data(n):
    return np.random.rand(n)

def calc_squared_dists(data):
    n = len(data[0])
    X = np.tile(np.column_stack(data), (n, 1, 1))
    deltaX = X - X.transpose((1,0,2))
    return np.sum(deltaX**2, axis=2)
    
def calc_W(data, sigma):
    return np.exp(-calc_squared_dists(data)/(2*sigma**2))

def calc_density_invariant_normalization(W):
    D = np.diag(np.reciprocal(np.sum(W, axis=1)))
    W_hat = D@W@D
    D_hat = np.diag(np.reciprocal(np.sum(W_hat, axis=1)))
    return D_hat@W_hat

def data_eigenvalues(data, weight_matrix_func=calc_W, laplacian_func=calc_density_invariant_normalization, sigma=1):
    W = weight_matrix_func(data, sigma)
    L = laplacian_func(W)
    EVs, eigenvalues, _ = np.linalg.svd(L)
    return EVs.T, eigenvalues

def get_3d_rect_evs(n=1000, aspect_ratios=(1.72, 1.37)):
    x = get_line_data(n)*aspect_ratios[0]
    y = get_line_data(n)*aspect_ratios[1]
    z = get_line_data(n)
    EVs, eigenvalues = data_eigenvalues((x,y,z))
    return x,y,z,EVs

def generate_data_for_eigenvector_scatter_plots(seed):
    np.random.seed(seed)
    x,y,z,EVs = get_3d_rect_evs(n=2000)
    np.save('plots_for_paper/eigenvectors_scatter_plots/data/rect3d_x', x)
    np.save('plots_for_paper/eigenvectors_scatter_plots/data/rect3d_y', y)
    np.save('plots_for_paper/eigenvectors_scatter_plots/data/rect3d_z', z)
    np.save('plots_for_paper/eigenvectors_scatter_plots/data/rect3d_evs', EVs)
    

if __name__ == '__main__':
    generate_data_for_eigenvector_scatter_plots(int(sys.argv[1]))


