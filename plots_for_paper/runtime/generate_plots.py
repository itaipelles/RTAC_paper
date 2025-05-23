import pickle
import numpy as np

table_prefix_string = '''\\begin{tabular}{c|c c c c c c}
{\\bf n} & $\\xi_n$ & HHG & MIC & dCor & HSIC  & RTAC (ours) \\\\ 
\\hline
'''

table_suffix_string = '''
\\hline
\\end{tabular}'''

def generate_runtime_plots():
    ns = np.load('plots_for_paper/runtime/data/ns.npy')
    with open(f'plots_for_paper/runtime/data/runtimes.pkl', 'rb') as f:
        times = pickle.load(f)
    order_of_keys = ['xicor', 'hhg', 'mic', 'dcor', 'hsic', 'rtac']
    lines = []
    for i, n in enumerate(ns):
        cur_items = [str(n)]
        for key in order_of_keys:
            cur_items.append(str(round(times[key][i],4)))
        lines.append(' & '.join(cur_items) + ' \\\\')
    
    latex_table_string = table_prefix_string + '\n'.join(lines) + table_suffix_string
    with open(f'plots_for_paper/runtime/plots/table_latex.txt', 'w') as f:
        f.write(latex_table_string)

if __name__ == '__main__':
    generate_runtime_plots()