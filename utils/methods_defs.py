from hyppo.independence import Hsic, Dcorr
import utils.AreaCoefficientIndependenceTest as AreaCoefficientIndependenceTest
import utils.MoreIndependenceTests as MoreIndependenceTests

INDEP_TESTS = {
    'rtac': AreaCoefficientIndependenceTest.AreaCoefficientIndependenceTest(coverage_factor=1),
    'rtac_gamma_2': AreaCoefficientIndependenceTest.AreaCoefficientIndependenceTest(coverage_factor=2),
    'rtac_gamma_4': AreaCoefficientIndependenceTest.AreaCoefficientIndependenceTest(coverage_factor=4),
    'rtac_gamma_0.5': AreaCoefficientIndependenceTest.AreaCoefficientIndependenceTest(coverage_factor=0.5),
    'xicor': MoreIndependenceTests.XiCorPYIndependenceTest(),
    "dcor": Dcorr(),
    "hsic": Hsic(),
    'mic': MoreIndependenceTests.MICIndependenceTest(),
    'adp': MoreIndependenceTests.ADP_MMAX5_IndependenceTest(),
}

TEST_LABELS = {
    'rtac': 'RTAC ($\\gamma=1$)',
    'rtac_gamma_4': 'RTAC ($\\gamma=4$)',
    'rtac_gamma_0.5': 'RTAC ($\\gamma=0.5$)',
    'xicor': "$\\xi_n$",
    'dcor': "dCor",
    'hsic': "HSIC",
    'mic': "MIC",
    'adp': "ADP",
}