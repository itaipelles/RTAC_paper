import numpy as np
from hyppo.independence.base import IndependenceTest
from rtacpy.calc_rtac import calc_rtac


class AreaCoverageIndependenceTest(IndependenceTest):
    coverage_factor_default = 1
    def __init__(self, coverage_factor=coverage_factor_default, **kwargs):
        self.coverage_factor = coverage_factor
        super(AreaCoverageIndependenceTest, self).__init__(**kwargs)
        
    def statistic(self, x, y):
        x = np.reshape(x, (len(x),))
        y = np.reshape(y, (len(y),))
        return calc_rtac(x,y,self.coverage_factor)
    
    def test(self, x, y,reps=1000,workers=-1):
        return super(AreaCoverageIndependenceTest, self).test(x,y, reps, workers, is_distsim=False)
