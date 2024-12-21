import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('./')
from .generate_data import SAMP_SIZES
from plots_for_paper.consts import SIMULATIONS
from matplotlib_helpers import _RCPARAMS_LATEX_SINGLE_COLUMN, save_figure
from plots_for_paper.consts import SIM_TITLES, TEST_LABELS

def generate_indep_tests_plots():
    with plt.rc_context(rc = _RCPARAMS_LATEX_SINGLE_COLUMN):
        for sim in SIMULATIONS.keys():
            for noise in [0, 0.5, 1]:
                for test, marker in zip(TEST_LABELS.keys(), ['o', 'd', 's', '*', '>', 'P']):
                    est_power = np.genfromtxt(
                        f"plots_for_paper/tests_of_indep_comparison/data/{sim}_{test}_noise_{noise}.csv",
                        delimiter=",",
                    )
                    plt.plot(SAMP_SIZES, est_power, label=TEST_LABELS[test], lw=2, marker=marker)
                ax = plt.gca()
                ax.set_xticks([SAMP_SIZES[0], SAMP_SIZES[-1]])
                ax.set_xlim([SAMP_SIZES[0], SAMP_SIZES[-1]])
                ax.set_ylim(0, 1)
                ax.set_yticks([0, 1])
                # plt.xlabel('Sample Size')
                # plt.ylabel('Average Power')
                # plt.title(f'{SIM_TITLES[sim]} Distribution - Test Power Comparison')

                plt.gca().legend()
                save_figure(plt.gcf(), f'plots_for_paper/tests_of_indep_comparison/plots/{sim}_noise_{noise}.pdf')
                plt.clf()

if __name__ == '__main__':
    generate_indep_tests_plots()