import numpy as np
import sys
sys.path.append('./')
from utils.distribution_defs import SIMULATIONS

NOISY = 100  # sample size of noisy simulation
NO_NOISE = 1000  # sample size of noise-free simulation

def generate_data_for_bivariate_distributions_plots(seed):
    for sim in SIMULATIONS.keys():
        for noise in [0, 0.05, 0.1, 0.2, 0.5, 1]:
            sim_func = SIMULATIONS[sim]
            np.random.seed(seed)
            # the multiplicative noise and independence simulation don't have a noise
            NUM = NO_NOISE if noise == 0 else NOISY
            if sim in ["multiplicative_noise", "multimodal_independence"]:
                x, y = sim_func(NUM, 1)
            else:
                x, y = sim_func(NUM, 1, noise=noise)
            
            np.save(f'plots_for_paper/bivariate_distributions/data/{sim}_noise_{noise}', np.array([x,y]))

if __name__ == '__main__':
    generate_data_for_bivariate_distributions_plots(int(sys.argv[1]))
