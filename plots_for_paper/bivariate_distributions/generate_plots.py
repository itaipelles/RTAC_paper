import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append('./')
from utils.matplotlib_helpers import save_figure
from utils.distribution_defs import SIM_TITLES

def generate_bivariate_distributions_plots():
    special_params_for_plot = {
        'font.family': 'serif',
        # 'text.usetex': True,

        #'axes.prop_cycle': matplotlib.pyplot.cycler('color', ['#006496', '#ff816b', '#fbca60', '#6d904f', '#8b8b8b']) + matplotlib.pyplot.cycler('marker', ['o', 'd', 's', '*', '>']),
        # 'axes.prop_cycle': matplotlib.pyplot.cycler('color', ['#ff7d66', '#ffdc30', '#40a0cc', '#529915', '#8b8b8b']) + matplotlib.pyplot.cycler('marker', ['d', 's', 'o', '*', '>']),

        'lines.markersize': 9,
        'lines.markeredgewidth': 0.75,
        'lines.markeredgecolor': 'k',
                                
        'grid.color': '#C0C0C0', # 25% black

        'legend.fancybox': True, # Rounded legend box
        'legend.framealpha': 0.8,

        'axes.linewidth': 1,
    }
    
    # make plots look pretty
    sns.set(color_codes=True, style="white", context="talk", font_scale=2)
    PALETTE = sns.color_palette("Greys", n_colors=9)
    sns.set_palette(PALETTE[2::2])

    with plt.rc_context(rc = special_params_for_plot):
        for sim, sim_title in SIM_TITLES.items():
            for noise in [0, 0.05, 0.1, 0.2, 0.5, 1]:
                x,y = np.load(f'plots_for_paper/bivariate_distributions/data/{sim}_noise_{noise}.npy')
                plt.scatter(x, y, label="Noisy")
                
                if noise != 0:
                    x_no_noise,y_no_noise = np.load(f'plots_for_paper/bivariate_distributions/data/{sim}_noise_0.npy')
                    plt.scatter(x_no_noise, y_no_noise, label="No Noise")
                else:
                    plt.scatter(x, y, label="Noisy2")

                # make the plot look pretty
                plt.title("{}".format(sim_title))
                ax = plt.gca()
                ax.set_xticks([])
                ax.set_yticks([])
                if sim == 'ellipse':
                    ax.set_ylim([-1.1, 1.1])
                    plt.axis('equal')
                    
                sns.despine(left=True, bottom=True, right=True)

                save_figure(plt.gcf(), f'plots_for_paper/bivariate_distributions/plots/{sim}_noise_{noise}.pdf')
                plt.clf()
        
if __name__ == '__main__':
    generate_bivariate_distributions_plots()