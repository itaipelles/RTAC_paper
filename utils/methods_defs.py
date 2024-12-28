from hyppo.independence import Hsic, Dcorr
import utils.AreaCoverageIndependenceTest as AreaCoverageIndependenceTest
import utils.MoreIndependenceTests as MoreIndependenceTests

INDEP_TESTS = {
    'area': AreaCoverageIndependenceTest.AreaCoverageIndependenceTest,
    'xicor': MoreIndependenceTests.XiCorPYIndependenceTest,
    "dcor": Dcorr,
    "hsic": Hsic,
    'mic': MoreIndependenceTests.MICIndependenceTest,
    'hhg': MoreIndependenceTests.HHGRIndependenceTest
}

TEST_LABELS = {
    'area': '$\\eta_n$',
    'xicor': "$\\xi_n$",
    'dcor': "dCor",
    'hsic': "HSIC",
    # 'mic': "MIC",
    'hhg': "HHG"
}