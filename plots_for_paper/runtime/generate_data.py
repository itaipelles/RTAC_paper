import numpy as np
from tqdm import tqdm
import pickle
import time
import sys
sys.path.append('./')
from utils.AreaCoefficientIndependenceTest import AreaCoefficientIndependenceTest
from utils.MoreIndependenceTests import HHGRIndependenceTest
from utils.distribution_defs import multimodal_independence
from utils.methods_defs import INDEP_TESTS

def prepare_for_runtime_plots(ns):
    # call rtac function once for numba compilation:
    AreaCoefficientIndependenceTest().statistic(np.random.rand(100),np.random.rand(100))
    
    # call rtac function once for each n to pre-calculate alpha_n for n
    for n in tqdm(ns):
        AreaCoefficientIndependenceTest().statistic(np.random.rand(n),np.random.rand(n))
    
    # call HHGR once for each n to create the null tables
    for n in tqdm(ns):
        HHGRIndependenceTest().statistic(np.random.rand(n),np.random.rand(n))

def generate_data_for_runtime():
    ns = [100, 500, 1000, 2000, 10000]
    np.save('plots_for_paper/runtime/data/ns', ns)
    dist = multimodal_independence # it doesn't matter which distribution we use, we only check runtime
    
    test_instances = {
        key: value() for key,value in INDEP_TESTS.items()
    }

    times = {
        key: [] for key in test_instances.keys()
    }
    
    prepare_for_runtime_plots(ns)

    for n in tqdm(ns):
        cur_n_times = {
            key: [] for key in test_instances.keys()
        }
        num_of_reps = 100000//n
        for _ in range(num_of_reps):
            x,y = dist(n,1)
            for key, test_instance in test_instances.items():
                bef = time.time()
                test_instance.statistic(x,y)
                cur_n_times[key].append(time.time()-bef)
        for key in test_instances.keys():
            times[key].append(np.mean(cur_n_times[key]))
    with open(f'plots_for_paper/runtime/data/runtimes.pkl', 'wb') as f:
        pickle.dump(times, f)

if __name__ == '__main__':
    generate_data_for_runtime()