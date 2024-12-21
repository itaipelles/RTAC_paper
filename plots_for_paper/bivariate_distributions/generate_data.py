import numpy as np
import sys
sys.path.append('./')
from utils.distribution_defs import SIMULATIONS

NOISY = 100  # sample size of noisy simulation
NO_NOISE = 1000  # sample size of noise-free simulation

def generate_data_for_bivariate_distributions_plots(seed):
    for sim in SIMULATIONS.keys():
        sim_func = SIMULATIONS[sim]
        # the multiplicative noise and independence simulation don't have a noise
        # parameter
        np.random.seed(seed)
        if sim in ["multiplicative_noise", "multimodal_independence"]:
            x, y = sim_func(NO_NOISE, 1)
            x_no_noise, y_no_noise = x, y
        else:
            x, y = sim_func(NOISY, 1, noise=0.5)
            x_no_noise, y_no_noise = sim_func(NO_NOISE, 1)
        
        np.save(f'plots_for_paper/bivariate_distributions/data/{sim}', np.array([x_no_noise,y_no_noise]))
        np.save(f'plots_for_paper/bivariate_distributions/data/{sim}_noisy', np.array([x,y]))

if __name__ == '__main__':
    generate_data_for_bivariate_distributions_plots(int(sys.argv[1]))
