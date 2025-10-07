import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('./')
from plots_for_paper.tests_of_indep_comparison.generate_data import SAMP_SIZES
from utils.matplotlib_helpers import _RCPARAMS_LATEX_SINGLE_COLUMN, save_figure
from utils.distribution_defs import SIMULATIONS
from utils.methods_defs import TEST_LABELS

def generate_indep_tests_plots():
    num_missing = 0
    with plt.rc_context(rc = _RCPARAMS_LATEX_SINGLE_COLUMN):
        for sim in SIMULATIONS.keys():
            for noise in [0, 0.05, 0.1, 0.2, 0.5, 1]:
                # First three methods are RTAC with gammas 1, 4, 0.5. Apply specific colors and marker sizes only to them.
                color_overrides = ['blue', 'navy', 'lightblue']  # blue, dark blue, light blue
                marker_size_overrides = [None, 10, 6]  # normal (default), large, small
                for idx, (test, marker) in enumerate(zip([key for key in TEST_LABELS.keys()], ['s', 's', 's', 'o', '*', '>', 'P', 'X'])):
                    try:
                        est_power = np.genfromtxt(
                            f"plots_for_paper/tests_of_indep_comparison/data/{sim}_{test}_noise_{noise}.csv",
                            delimiter=",",
                        )
                        if idx < 3:
                            plot_kwargs = {
                                'label': TEST_LABELS[test],
                                'lw': 2,
                                'marker': marker,
                                'color': color_overrides[idx],
                            }
                            if marker_size_overrides[idx] is not None:
                                plot_kwargs['markersize'] = marker_size_overrides[idx]
                            plt.plot(SAMP_SIZES, est_power, **plot_kwargs)
                        else:
                            # Leave all other colors and marker sizes untouched
                            plt.plot(SAMP_SIZES, est_power, label=TEST_LABELS[test], lw=2, marker=marker)
                    except:
                        print('missing', sim, test, noise)
                        num_missing += 1
                ax = plt.gca()
                ax.set_xticks([SAMP_SIZES[0], SAMP_SIZES[-1]])
                ax.set_xlim([SAMP_SIZES[0], SAMP_SIZES[-1]])
                ax.set_ylim(0, 1)
                ax.set_yticks([0, 1])

                plt.gca().legend()
                save_figure(plt.gcf(), f'plots_for_paper/tests_of_indep_comparison/plots/{sim}_noise_{noise}.pdf')
                plt.clf()
    if num_missing:
        print(f"Number of missing files: {num_missing}")
if __name__ == '__main__':
    generate_indep_tests_plots()