from hyppo.independence.base import IndependenceTest
from etacorpy.calc_eta_n import calc_eta_n


class AreaCoverageIndependenceTest(IndependenceTest):
    coverage_factor_default = 1
    def __init__(self, coverage_factor=coverage_factor_default, **kwargs):
        self.coverage_factor = coverage_factor
        super(AreaCoverageIndependenceTest, self).__init__(**kwargs)
        
    def statistic(self, x, y):
        return calc_eta_n(x,y,self.coverage_factor)
    
    def test(self, x, y,reps=1000,workers=-1):
        return super(AreaCoverageIndependenceTest, self).test(x,y, reps, workers, is_distsim=False)
