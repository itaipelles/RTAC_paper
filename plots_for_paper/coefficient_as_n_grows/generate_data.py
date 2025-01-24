import math
import pickle
import numpy as np
from tqdm import tqdm
from joblib import Parallel, delayed
import sys
sys.path.append('./')
from utils.distribution_defs import SIMULATIONS, SIMULATIONS_IN_PAPER
from utils.methods_defs import INDEP_TESTS

def generate_data_single_dist(dist, dist_name, ns, noise):
    test_instances = {
        key: value() for key,value in INDEP_TESTS.items() if 'hhg' not in key
    }

    stats = {
        key: [] for key in test_instances.keys()
    }

    reps_per_n = 80
    i=0
    for n in tqdm(ns):
        i+=1
        cur_n_stats = {
            key: [] for key in stats.keys()
        }
        for _ in range(reps_per_n-4*i):
            if dist_name in ["multiplicative_noise", "multimodal_independence"]:
                x,y = dist(n,1)
            else:
                x,y = dist(n,1, noise=noise)
            for key, test_instance in test_instances.items():
                cur_n_stats[key].append(test_instance.statistic(x,y))
        for key in stats.keys():
            stats[key].append(np.mean(cur_n_stats[key]))
    with open(f'plots_for_paper/coefficient_as_n_grows/data/{dist_name}_noise_{noise}.pkl', 'wb') as f:
        pickle.dump(stats, f)

def generate_data_for_coefficient_plots(seed):
    n_from = 12 # 64
    n_to = 28 # 16384
    ns = [math.floor(np.sqrt(2)**i) for i in range(n_from,n_to)]
    np.save('plots_for_paper/coefficient_as_n_grows/data/ns', ns)
    np.random.seed(seed)
    Parallel(n_jobs=-1, verbose=100)(
        [
            delayed(generate_data_single_dist)(dist, dist_name, ns, noise)
            for dist_name, dist in SIMULATIONS.items()
            # for dist_name, dist in SIMULATIONS_IN_PAPER.items()
            for noise in [0, 0.05, 0.1, 0.2, 0.5]
        ]
    )

if __name__ == '__main__':
    generate_data_for_coefficient_plots(int(sys.argv[1]))
    