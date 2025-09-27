import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('./')
from utils.distribution_defs import SIM_TITLES
from utils.matplotlib_helpers import _RCPARAMS_LATEX_SINGLE_COLUMN, save_figure
from plots_for_paper.choice_of_gamma.generate_data import DISTRIBUTIONS_CHOICE_OF_GAMMA

def generate_choice_of_gamma_plots():
    """
    Generate the power vs gamma plot for multiple distributions.
    """
    with plt.rc_context(rc=_RCPARAMS_LATEX_SINGLE_COLUMN):
        # Create the plot
        plt.figure(figsize=(12, 8))
        
        # Define colors for different distributions
        colors = plt.cm.tab10(np.linspace(0, 1, len(DISTRIBUTIONS_CHOICE_OF_GAMMA)))
        
        for i, dist_config in enumerate(DISTRIBUTIONS_CHOICE_OF_GAMMA):
            dist_name = dist_config['name']
            noise_level = dist_config['noise_level']
            
            try:
                # Load gamma values and power data
                gamma_values = np.genfromtxt(
                    f"plots_for_paper/choice_of_gamma/data/{dist_name}_noise_{noise_level}_gamma.csv",
                    delimiter=","
                )
                powers = np.genfromtxt(
                    f"plots_for_paper/choice_of_gamma/data/{dist_name}_noise_{noise_level}_power.csv",
                    delimiter=","
                )
                
                # Plot this distribution
                plt.plot(gamma_values, powers, marker='o', label=SIM_TITLES[dist_name], 
                        color=colors[i], linewidth=2, markersize=4)
                
            except Exception as e:
                print(f"Error loading data for {dist_name}: {e}")
                continue
        
        # Customize the plot
        plt.xlabel('Gamma (coverage_factor)', fontsize=12)
        plt.ylabel('Estimated Power', fontsize=12)
        plt.title('RTAC Power vs Gamma - Multiple Distributions (n=50)', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
        plt.tight_layout()
        
        # Save the plot
        save_figure(plt.gcf(), 'plots_for_paper/choice_of_gamma/plots/power_vs_gamma_multiple_distributions.pdf')
        plt.clf()
        
        print("Generated choice_of_gamma plot: power_vs_gamma_multiple_distributions.pdf")

if __name__ == '__main__':
    generate_choice_of_gamma_plots()
