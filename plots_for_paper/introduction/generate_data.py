import numpy as np
from scipy.stats import multivariate_normal
import sys

n=300

def independent(seed):
    np.random.seed(seed)
    x = np.random.rand(n)
    y = np.random.rand(n)
    return np.array((x,y))

def normal(seed):
    np.random.rand(seed)
    cov=0.0125
    var=0.015
    return multivariate_normal.rvs([0.5,0.5],[[var,cov],[cov,var]],n).T

def circle(seed):
    np.random.seed(seed)
    theta = np.random.rand(n)*2*np.pi
    x = 0.5+0.5*np.cos(theta)
    y = 0.5+0.5*np.sin(theta)
    return np.array((x,y))

distribution_to_data = {
    'independent': independent,
    'normal': normal,
    'circle': circle
}

def generate_data_for_introduction_plots(seeds):
    for (dist_name, dist_fn), seed in zip(distribution_to_data.items(), seeds):
        data = dist_fn(int(seed))
        np.save(f'plots_for_paper/introduction/data/{dist_name}', data)
        
if __name__ == '__main__':
    generate_data_for_introduction_plots(sys.argv[1:4])