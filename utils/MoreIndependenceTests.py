from functools import lru_cache
from hyppo.independence.base import IndependenceTest, IndependenceTestOutput
import xicorpy
from rpy2.robjects import FloatVector
import rpy2.robjects.packages as rpackages
# from minepy import MINE

HHG = rpackages.importr('HHG', lib_loc='/home/itaipelles/R/x86_64-pc-linux-gnu-library/4.3')

@lru_cache(22)
def get_nulltable(n):
    return HHG.Fast_independence_test_nulltable(n)

class XiCorPYIndependenceTest(IndependenceTest):
    def __init__(self, **kwargs):
        super(XiCorPYIndependenceTest, self).__init__(**kwargs)
        
    def statistic(self, x, y):
        return xicorpy.compute_xi_correlation(x, y, get_modified_xi=False)[0][0]
    
    def test(self, x, y):
        res = xicorpy.compute_xi_correlation(x,y, get_modified_xi=False, get_p_values=True)
        return IndependenceTestOutput(res[0][0][0], res[1][0][0])

class HHGRIndependenceTest(IndependenceTest):
    def __init__(self, **kwargs):
        super(HHGRIndependenceTest, self).__init__(**kwargs)
        
    def statistic(self, x, y):
        n = x.shape[0]
        x = FloatVector(x)
        y = FloatVector(y)
        res = HHG.Fast_independence_test(x,y,NullTable=get_nulltable(n))
        for item in res.items():
            if item[0] == 'MinP':
                return -item[1][0]
    
    def test(self, x, y, **kwargs):
        return super(HHGRIndependenceTest, self).test(x, y, **kwargs)
    
class MICIndependenceTest(IndependenceTest):
    def __init__(self, **kwargs):
        super(MICIndependenceTest, self).__init__(**kwargs)
        
    def statistic(self, x, y):
        mine = MINE()
        mine.compute_score(x.squeeze(),y.squeeze())
        return mine.mic()
    
    def test(self, x, y, **kwargs):
        return super(MICIndependenceTest, self).test(x, y, **kwargs)
