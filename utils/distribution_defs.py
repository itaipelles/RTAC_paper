import numpy as np
from scipy.stats import multivariate_normal
from .hyppo_distributions import linear, exponential, cubic,joint_normal,step,quadratic,w_shaped,spiral,uncorrelated_bernoulli,logarithmic,fourth_root,sin_four_pi,sin_sixteen_pi,square,two_parabolas,circle,ellipse,diamond,multiplicative_noise,multimodal_independence


def four_circles(n,p,noise=0):
    theta = np.random.rand(n)*2*np.pi
    x = np.cos(theta)
    y = np.sin(theta)
    x_center = ([-0.5,0.5,0.5,-0.5]*(n//4 + 1))[:n]
    y_center = ([-0.5,0.5,-0.5,0.5]*(n//4 + 1))[:n]
    x+=x_center
    y+=y_center
    x+=noise*np.random.normal(loc=0, scale=0.1, size=n)
    y+=noise*np.random.normal(loc=0, scale=0.1, size=n)
    return np.expand_dims(x,1),np.expand_dims(y,1)

def checkerboard(n, p, noise=0,k=8):
    # Calculate total number of black cells
    num_black_cells = k*k - (k * k) // 2
    
    # Generate random indices for black cells
    black_indices = np.random.choice(num_black_cells, size=n, replace=True)
    
    # Map black cell indices to (i, j) coordinates
    black_cells = [(i, j) for i in range(k) for j in range(k) if (i + j) % 2 == 0]
    chosen_cells = np.array([black_cells[idx] for idx in black_indices])
    
    # Generate random points within these cells
    random_offsets = np.random.rand(n, 2)  # Random offsets within cells
    points = chosen_cells + random_offsets  # Map to points within black cells
    x = points[:,0]
    y = points[:,1]
    x+=noise*np.random.normal(loc=0, scale=0.3, size=n)
    y+=noise*np.random.normal(loc=0, scale=0.3, size=n)
    return np.expand_dims(x,1),np.expand_dims(y,1)

def checkerboard_k(k):
    return lambda n,p,noise=0: checkerboard(n,p,noise=noise,k=k)

def Gaussian_X(n,p,noise=0):
    coins = np.random.rand(n)>0.5
    cov=0.0125
    var=0.015
    positive_corr = multivariate_normal.rvs([0.5,0.5],[[var,cov],[cov,var]],n).T
    negative_corr = multivariate_normal.rvs([0.5,0.5],[[var,-cov],[-cov,var]],n).T
    x,y = np.multiply(coins, positive_corr) + np.multiply(1-coins, negative_corr)
    return np.expand_dims(x,1),np.expand_dims(y,1)

SIMULATIONS = {
    'checkerboard2': checkerboard_k(2),
    'checkerboard4': checkerboard_k(4),
    'checkerboard6': checkerboard_k(6),
    'checkerboard8': checkerboard_k(8),
    "linear": linear,
    "exponential": exponential,
    "cubic": cubic,
    "joint_normal": joint_normal,
    "step": step,
    "quadratic": quadratic,
    "w_shaped": w_shaped,
    "spiral": spiral,
    "uncorrelated_bernoulli": uncorrelated_bernoulli,
    "logarithmic": logarithmic,
    "fourth_root": fourth_root,
    "sin_four_pi": sin_four_pi,
    "sin_sixteen_pi": sin_sixteen_pi,
    "square": square,
    "two_parabolas": two_parabolas,
    "circle": circle,
    "ellipse": ellipse,
    "diamond": diamond,
    "multiplicative_noise": multiplicative_noise,
    "multimodal_independence": multimodal_independence,
    "4_circles": four_circles,
    'Gaussian_X': Gaussian_X
}

SIMULATIONS_IN_PAPER_NAMES = ['exponential', 'quadratic', 'sin_four_pi', 'circle', 'spiral', '4_circles', 'diamond', 'checkerboard8', 'joint_normal', 'Gaussian_X', 'multimodal_independence']
SIMULATIONS_IN_PAPER = {
    key: SIMULATIONS[key] for key in SIMULATIONS_IN_PAPER_NAMES
}

SIM_TITLES = {
    'checkerboard2': 'Checkerboard 2x2',
    'checkerboard4': 'Checkerboard 4x4',
    'checkerboard6': 'Checkerboard 6x6',
    'checkerboard8': 'Checkerboard 8x8',
    "linear": "Linear",
    "exponential": "Exponential",
    "cubic": "Cubic",
    "joint_normal": "Joint Normal",
    "step": "Step",
    "quadratic": "Quadratic",
    "w_shaped": "W-Shaped",
    "spiral": "Spiral",
    "uncorrelated_bernoulli": "Bernoulli",
    "logarithmic": "Logarithmic",
    "fourth_root": "Fourth Root",
    "sin_four_pi": "Sine $4\pi$",
    "sin_sixteen_pi": "Sine $16\pi$",
    "square": "Square",
    "two_parabolas": "Two Parabolas",
    "circle": "Circle",
    "ellipse": "Ellipse",
    "diamond": "Diamond",
    "multiplicative_noise": "Noise",
    "multimodal_independence": "Independence",
    "4_circles": "Four Circles",
    'Gaussian_X': "Gaussian Mixture"
}
