from hyppo.independence import Hsic, Dcorr
import utils.AreaCoefficientIndependenceTest as AreaCoefficientIndependenceTest
import utils.MoreIndependenceTests as MoreIndependenceTests

INDEP_TESTS = {
    'rtac': AreaCoefficientIndependenceTest.AreaCoefficientIndependenceTest(coverage_factor=1),
    'rtac_gamma_2': AreaCoefficientIndependenceTest.AreaCoefficientIndependenceTest(coverage_factor=2),
    'xicor': MoreIndependenceTests.XiCorPYIndependenceTest(),
    "dcor": Dcorr(),
    "hsic": Hsic(),
    'mic': MoreIndependenceTests.MICIndependenceTest(),
    'adp': MoreIndependenceTests.ADP_MMAX5_IndependenceTest(),
}

TEST_LABELS = {
    'rtac': 'RTAC',
    'xicor': "$\\xi_n$",
    'dcor': "dCor",
    'hsic': "HSIC",
    'mic': "MIC",
    'adp': "ADP",
    'rtac_gamma_2': 'RTAC ($\\gamma=2$)',
}