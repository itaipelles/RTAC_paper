import numpy as np
import os
import sys
sys.path.append('./')
from utils.AreaCoefficientIndependenceTest import AreaCoefficientIndependenceTest
from plots_for_paper.tests_of_indep_comparison.generate_data import power

# Constants
N = 50  # Sample size
GAMMA_VALUES = np.linspace(0.1, 6, 40)
ALPHA = 0.05
REPS = 3000

# 7 distributions to use
DISTRIBUTIONS_CHOICE_OF_GAMMA = [
    {'name': 'sin_four_pi', 'noise_level': 0.1},
    {'name': 'spiral', 'noise_level': 0.2},
    {'name': '4_circles', 'noise_level': 0.0},
    {'name': 'checkerboard8', 'noise_level': 0.0},
    {'name': 'diamond', 'noise_level': 0.0},
    {'name': 'joint_normal', 'noise_level': 0.0},
    {'name': 'Gaussian_X', 'noise_level': 0.0}
]

def generate_power_vs_gamma_data(dist_name, noise_level):
    """
    Generate power vs gamma data for a single distribution.
    
    Args:
        dist_name (str): Name of the distribution
        noise_level (float): Noise level for the distribution
    
    Returns:
        tuple: (gamma_values, powers)
    """
    print(f"Processing {dist_name} with noise={noise_level}...")
    
    powers = []
    for gamma in GAMMA_VALUES:
        test = AreaCoefficientIndependenceTest(coverage_factor=gamma)
        pwr = power(test, dist_name, alpha=ALPHA, reps=REPS, n=N, noise=noise_level)
        powers.append(pwr)
        # print(f"  Gamma={gamma:.2f}, Power={pwr:.3f}")
    
    return GAMMA_VALUES, powers

def save_data(dist_name, noise_level, gamma_values, powers):
    """
    Save the power vs gamma data to CSV files.
    
    Args:
        dist_name (str): Name of the distribution
        noise_level (float): Noise level
        gamma_values (array): Array of gamma values
        powers (array): Array of power values
    """
    # Save gamma values
    gamma_path = f"plots_for_paper/choice_of_gamma/data/{dist_name}_noise_{noise_level}_gamma.csv"
    np.savetxt(gamma_path, gamma_values, delimiter=",")
    
    # Save power values
    power_path = f"plots_for_paper/choice_of_gamma/data/{dist_name}_noise_{noise_level}_power.csv"
    np.savetxt(power_path, powers, delimiter=",")
    
    print(f"Saved data for {dist_name} to {gamma_path} and {power_path}")

def generate_data_for_choice_of_gamma_plots():
    """
    Generate power vs gamma data for all distributions and save to CSV files.
    """
    # Create data directory if it doesn't exist
    os.makedirs("plots_for_paper/choice_of_gamma/data", exist_ok=True)
    
    for dist_config in DISTRIBUTIONS_CHOICE_OF_GAMMA:
        dist_name = dist_config['name']
        noise_level = dist_config['noise_level']
        
        # Generate data
        gamma_values, powers = generate_power_vs_gamma_data(dist_name, noise_level)
        
        # Save data
        save_data(dist_name, noise_level, gamma_values, powers)
    
    print("Completed generating data for choice_of_gamma plots")

if __name__ == '__main__':
    generate_data_for_choice_of_gamma_plots()
