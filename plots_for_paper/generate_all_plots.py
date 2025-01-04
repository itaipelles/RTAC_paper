from sweeping_line.generate_plots import generate_sweeping_line_plots
from introduction.generate_plots import generate_introduction_plots
from bivariate_distributions.generate_plots import generate_bivariate_distributions_plots
from tests_of_indep_comparison.generate_plots import generate_indep_tests_plots
from coefficient_as_n_grows.generate_plots import generate_coefficients_plots
from runtime.generate_plots import generate_runtime_plots
from proof_of_alpha_n.generate_plots import generate_alpha_n_proof_plots
from eigenvectors_scatter_plots.generate_plots import generate_eigienvectors_scatter_plots
import matplotlib.pyplot as plt


generate_sweeping_line_plots()
plt.close('all')
generate_introduction_plots()
plt.close('all')
generate_indep_tests_plots()
plt.close('all')
generate_coefficients_plots()
plt.close('all')
generate_runtime_plots()
plt.close('all')
generate_alpha_n_proof_plots()
plt.close('all')
generate_eigienvectors_scatter_plots()
plt.close('all')

# must be last due to changing colors to grey
generate_bivariate_distributions_plots()