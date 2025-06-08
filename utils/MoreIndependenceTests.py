from functools import lru_cache
from hyppo.independence.base import IndependenceTest, IndependenceTestOutput
import xicorpy
from rpy2.robjects import FloatVector
import rpy2.robjects.packages as rpackages
from minepy import MINE

HHG = rpackages.importr('HHG', lib_loc='/home/itaipelles/R/x86_64-pc-linux-gnu-library/4.3')

@lru_cache(22)
def get_adp_fast_nulltable(n):
    return HHG.Fast_independence_test_nulltable(n)

@lru_cache(22)
def get_adp_non_fast_nulltable(n, mmax=None, variant=None):
    if mmax is not None and variant is not None:
        return HHG.hhg_univariate_ind_nulltable(n, mmax=mmax, variant=variant)
    if mmax is not None:
        return HHG.hhg_univariate_ind_nulltable(n, mmax=mmax)
    if variant is not None:
        return HHG.hhg_univariate_ind_nulltable(n, variant=variant)
    return HHG.hhg_univariate_ind_nulltable(n)

class XiCorPYIndependenceTest(IndependenceTest):
    def __init__(self, **kwargs):
        super(XiCorPYIndependenceTest, self).__init__(**kwargs)
        
    def statistic(self, x, y):
        return xicorpy.compute_xi_correlation(x, y, get_modified_xi=False)[0][0]
    
    def test(self, x, y):
        res = xicorpy.compute_xi_correlation(x,y, get_modified_xi=False, get_p_values=True)
        return IndependenceTestOutput(res[0][0][0], res[1][0][0])

class ADP_EQP_ML_IndependenceTest(IndependenceTest):
    def __init__(self, **kwargs):
        super(ADP_EQP_ML_IndependenceTest, self).__init__(**kwargs)
        
    def statistic(self, x, y):
        n = x.shape[0]
        x = FloatVector(x)
        y = FloatVector(y)
        res = HHG.Fast_independence_test(x,y,NullTable=get_adp_fast_nulltable(n))
        for item in res.items():
            if item[0] == 'MinP':
                return -item[1][0]
    
    def test(self, x, y, **kwargs):
        return super(ADP_EQP_ML_IndependenceTest, self).test(x, y, **kwargs)

class ADPIndependenceTest(IndependenceTest):
    def __init__(self, **kwargs):
        super(ADPIndependenceTest, self).__init__(**kwargs)
        
    def statistic(self, x, y):
        n = x.shape[0]
        x = FloatVector(x)
        y = FloatVector(y)
        res = HHG.hhg_univariate_ind_combined_test(x,y,NullTable=get_adp_non_fast_nulltable(n))
        for item in res.items():
            if item[0] == 'MinP':
                return -item[1][0]
    
    def test(self, x, y, **kwargs):
        return super(ADPIndependenceTest, self).test(x, y, **kwargs)

class ADP_MMAX4_IndependenceTest(IndependenceTest):
    def __init__(self, **kwargs):
        super(ADP_MMAX4_IndependenceTest, self).__init__(**kwargs)
        
    def statistic(self, x, y):
        n = x.shape[0]
        x = FloatVector(x)
        y = FloatVector(y)
        res = HHG.hhg_univariate_ind_combined_test(x,y,NullTable=get_adp_non_fast_nulltable(n,mmax=4))
        for item in res.items():
            if item[0] == 'MinP':
                return -item[1][0]
    
    def test(self, x, y, **kwargs):
        return super(ADP_MMAX4_IndependenceTest, self).test(x, y, **kwargs)


class ADP_MMAX5_IndependenceTest(IndependenceTest):
    def __init__(self, **kwargs):
        super(ADP_MMAX5_IndependenceTest, self).__init__(**kwargs)
        
    def statistic(self, x, y):
        n = x.shape[0]
        x = FloatVector(x)
        y = FloatVector(y)
        res = HHG.hhg_univariate_ind_combined_test(x,y,NullTable=get_adp_non_fast_nulltable(n,mmax=5))
        for item in res.items():
            if item[0] == 'MinP':
                return -item[1][0]
    
    def test(self, x, y, **kwargs):
        return super(ADP_MMAX5_IndependenceTest, self).test(x, y, **kwargs)

class ADP_MMAX10_IndependenceTest(IndependenceTest):
    def __init__(self, **kwargs):
        super(ADP_MMAX10_IndependenceTest, self).__init__(**kwargs)
        
    def statistic(self, x, y):
        n = x.shape[0]
        x = FloatVector(x)
        y = FloatVector(y)
        res = HHG.hhg_univariate_ind_combined_test(x,y,NullTable=get_adp_non_fast_nulltable(n,mmax=min(n, 10)))
        for item in res.items():
            if item[0] == 'MinP':
                return -item[1][0]
    
    def test(self, x, y, **kwargs):
        return super(ADP_MMAX10_IndependenceTest, self).test(x, y, **kwargs)


class ADP_ML_IndependenceTest(IndependenceTest):
    def __init__(self, **kwargs):
        super(ADP_ML_IndependenceTest, self).__init__(**kwargs)
        
    def statistic(self, x, y):
        n = x.shape[0]
        x = FloatVector(x)
        y = FloatVector(y)
        res = HHG.hhg_univariate_ind_combined_test(x,y,NullTable=get_adp_non_fast_nulltable(n,mmax=min(10,n), variant='ADP-ML'))
        for item in res.items():
            if item[0] == 'MinP':
                return -item[1][0]
    
    def test(self, x, y, **kwargs):
        return super(ADP_ML_IndependenceTest, self).test(x, y, **kwargs)
    
class MICIndependenceTest(IndependenceTest):
    def __init__(self, **kwargs):
        super(MICIndependenceTest, self).__init__(**kwargs)
        
    def statistic(self, x, y):
        mine = MINE()
        mine.compute_score(x.squeeze(),y.squeeze())
        return mine.mic()
    
    def test(self, x, y, **kwargs):
        return super(MICIndependenceTest, self).test(x, y, **kwargs)
