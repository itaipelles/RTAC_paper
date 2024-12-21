import numpy as np
from tqdm import tqdm
import pickle
import time
import sys
sys.path.append('./')
from AreaIndependenceTest import AreaCoverageIndependenceTest
from MoreIndependenceTests import HHGRIndependenceTest
from plots_for_paper.consts import multimodal_independence, INDEP_TESTS

def prepare_for_runtime_plots(ns):
    # call area function once for numba compilation:
    AreaCoverageIndependenceTest().statistic(np.random.rand(100),np.random.rand(100))
    
    # call area function once for each n to pre-calculate the min area for n
    for n in tqdm(ns):
        AreaCoverageIndependenceTest().statistic(np.random.rand(n),np.random.rand(n))
    
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
        key: [] for key in INDEP_TESTS.keys()
    }
    
    prepare_for_runtime_plots(ns)

    for n in tqdm(ns):
        cur_n_times = {
            key: [] for key in INDEP_TESTS.keys()
        }
        num_of_reps = 100000//n
        for _ in range(num_of_reps):
            x,y = dist(n,1)
            for key, test_instance in test_instances.items():
                bef = time.time()
                test_instance.statistic(x,y)
                cur_n_times[key].append(time.time()-bef)
        for key in INDEP_TESTS.keys():
            times[key].append(np.mean(cur_n_times[key]))
    with open(f'plots_for_paper/runtime/data/runtimes.pkl', 'wb') as f:
        pickle.dump(times, f)

if __name__ == '__main__':
    generate_data_for_runtime()