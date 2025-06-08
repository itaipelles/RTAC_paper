from hyppo.independence import Hsic, Dcorr
import utils.AreaCoefficientIndependenceTest as AreaCoefficientIndependenceTest
import utils.MoreIndependenceTests as MoreIndependenceTests

INDEP_TESTS = {
    'rtac': AreaCoefficientIndependenceTest.AreaCoefficientIndependenceTest,
    'xicor': MoreIndependenceTests.XiCorPYIndependenceTest,
    "dcor": Dcorr,
    "hsic": Hsic,
    'mic': MoreIndependenceTests.MICIndependenceTest,
    'adp': MoreIndependenceTests.ADP_MMAX5_IndependenceTest,
}

TEST_LABELS = {
    'rtac': 'RTAC',
    'xicor': "$\\xi_n$",
    'dcor': "dCor",
    'hsic': "HSIC",
    'mic': "MIC",
    'adp': "ADP",
}