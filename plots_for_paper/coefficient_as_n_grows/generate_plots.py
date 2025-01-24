import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('./')
from utils.matplotlib_helpers import _RCPARAMS_LATEX_SINGLE_COLUMN, save_figure
from utils.distribution_defs import SIM_TITLES
from utils.methods_defs import TEST_LABELS


def generate_single_plot(dist_name, dist_title, ns, noise):
    with open(f'plots_for_paper/coefficient_as_n_grows/data/{dist_name}_noise_{noise}.pkl', 'rb') as f:
        stats = pickle.load(f)
    with plt.rc_context(rc = _RCPARAMS_LATEX_SINGLE_COLUMN):
        for (key, values), marker in zip(stats.items(), ['o', 'd', 's', '*', '>']):
            plt.plot(ns, values,marker=marker,linestyle='-',label=TEST_LABELS[key])
        plt.gca().legend()
        plt.gca().set_ylim(0,1.02)
        plt.gca().set_xscale('log')
        plt.gca().set_xticks([100,1000,10000])
        plt.xlim(ns[0], ns[-1]+1000)
        save_figure(plt.gcf(), f'plots_for_paper/coefficient_as_n_grows/plots/{dist_name}_coefficients_noise_{noise}.pdf')
        plt.clf()

def generate_coefficients_plots():
    ns = np.load('plots_for_paper/coefficient_as_n_grows/data/ns.npy')
    for dist_name, dist_title in SIM_TITLES.items():
        for noise in [0, 0.05, 0.1, 0.2, 0.5]:
            try:
                generate_single_plot(dist_name, dist_title, ns, noise)
            except Exception as e:
                print('missing', dist_name, noise, e)

if __name__ == '__main__':
    generate_coefficients_plots()