from math import ceil
import numpy as np
from joblib import Parallel, delayed
import sys
sys.path.append('./')
from plots_for_paper.consts import INDEP_TESTS, SIMULATIONS

# constants
MAX_SAMPLE_SIZE = 100
STEP_SIZE = 5
SAMP_SIZES = range(5, MAX_SAMPLE_SIZE + STEP_SIZE, STEP_SIZE)
POWER_REPS = 5

def _indep_perm_stat(test, sim, n, noise):
    """
    Generates null and alternate distributions for the independence test.
    """
    if sim in ["multiplicative_noise", "multimodal_independence"]:
        x,y = SIMULATIONS[sim](n,1)
    else:
        x, y = SIMULATIONS[sim](n, 1, noise=noise)
    obs_stat = test.statistic(x, y)
    permy = np.random.permutation(y)
    perm_stat = test.statistic(x, permy)

    return obs_stat, perm_stat

def power(test, sim, alpha=0.05, reps=2000, n=100, noise=1):
    alt_dist, null_dist = map(
        np.float64,
        zip(
            *[
                _indep_perm_stat(test=test, sim=sim, n=n, noise=noise)
                for _ in range(reps)
            ]
        ),
    )
    cutoff = np.sort(null_dist)[ceil(reps * (1 - alpha))]
    empirical_power = (1 + (alt_dist >= cutoff).sum()) / (1 + reps)
    return empirical_power

def estimate_power(test, sim, noise):
    """Compute the mean of the estimated power of 5 replications over sample sizes."""
    est_power = np.array(
        [
            np.mean(
                [
                    power(
                        INDEP_TESTS[test](), sim, n=i, noise=noise
                    )
                    for _ in range(POWER_REPS)
                ]
            )
            for i in SAMP_SIZES
        ]
    )
    np.savetxt(
        "plots_for_paper/tests_of_indep_comparison/data/{}_{}_noise_{}.csv".format(sim, test, noise),
        est_power,
        delimiter=",",
    )

    return est_power

def generate_data_for_indep_tests_plots():
    Parallel(n_jobs=-1, verbose=100)(
        [
            delayed(estimate_power)(test, sim_name, noise)
            for sim_name in SIMULATIONS.keys()
            for test in INDEP_TESTS.keys()
            for noise in [0, 0.5, 1]
        ]
    )

if __name__ == '__main__':
    generate_data_for_indep_tests_plots()


