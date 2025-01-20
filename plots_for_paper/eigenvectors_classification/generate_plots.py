import numpy as np
import pickle

table_prefix_string = '''\\begin{tabular}{c c c c c c c}
\\hline
 & $\\xi_n$ & MIC & dCor & HSIC  & $\\eta_n$ (ours) \\\\ [0.5ex] 
\\hline
'''

table_suffix_string = ''' [1ex]
\\hline
\\end{tabular}'''

def get_best_threshold_success_rate(low_vals, high_vals, two_sided=False):
    start = np.min(low_vals + high_vals)
    end = np.max(low_vals + high_vals)
    all_options = [start, end] + [val for val in low_vals if val > start] + [val for val in high_vals if val < end]
    all_options = np.sort(np.unique(all_options))
    best_success_rate = 0.0
    best_threshold = 0.0
    for val in all_options:
        if two_sided:
            success_rate = 100.0*(np.mean((low_vals <= val) & (high_vals > val)))
        else:
            success_rate = 100.0*(np.mean(low_vals <= val) + np.mean(high_vals > val))/2.0
        if success_rate > best_success_rate:
            best_success_rate = success_rate
            best_threshold = val
    return best_threshold, best_success_rate

def generate_eigienvectors_classification_plots():
    with open(f'plots_for_paper/eigenvectors_classification/data/results.pkl', 'rb') as f:
        results = pickle.load(f)
    
    table_stats = {
        key: {
            'mean_c_minus': np.mean(value['c_minus']),
            'max_c_minus': np.max(value['c_minus']),
            'mean_c_plus': np.mean(value['c_plus']),
            'min_c_plus': np.min(value['c_plus']),
            'success_rate': 100.0*np.mean(np.array(value['c_plus']) > np.array(value['c_minus'])),
            'best_threshold_data': get_best_threshold_success_rate(value['c_minus'], value['c_plus'], two_sided=True)
        } for key, value in results.items()
    }
    
    for key in table_stats:
        if table_stats[key]['best_threshold_data'][0] == 0.0:
            table_stats[key]['best_threshold_data'] = get_best_threshold_success_rate(results[key]['all_vals_for_gt_0'], results[key]['all_vals_for_gt_1'])
    
    for key in table_stats:
        threshold = table_stats[key]['best_threshold_data'][0]
        table_stats[key]['best_threshold'] = threshold
        table_stats[key]['case_success_rate_with_best_threshold'] = 100*(np.mean((np.array(results[key]['c_plus']) > threshold) & (np.array(results[key]['c_minus']) <= threshold)))
        all_errors = np.sum(np.array(results[key]['all_vals_for_gt_0']) > threshold) + np.sum(np.array(results[key]['all_vals_for_gt_1']) <= threshold)
        num_sims = len(results[key]['c_minus'])
        table_stats[key]['avg_errors_per_sim'] = all_errors/num_sims
    
    order_of_keys = ['xicor', 'mic', 'hsic', 'dcor', 'area']
    # order_of_keys = ['xicor', 'area']
    row_defs = [
        ('mean_c_minus', 'Mean $C_-$'),
        ('mean_c_plus', 'Mean $C_+$'),
        # ('max_c_minus', 'Max $C_-$'),
        # ('min_c_plus', 'Min $C_+$'),
        ('best_threshold', 'Best Threshold $\\alpha$'),
        ('success_rate', 'Simulations With $C_+ > C_-$'),
        # ('best_threshold_success_rate', 'Individual Coefficient Classification Success Rate'),
        ('case_success_rate_with_best_threshold', 'Simulations With $C_+ > \\alpha \\geq C_-$'),
        ('avg_errors_per_sim', 'Mean Num of Errors Per Sim.'),
    ]
    lines = []
    for field, title in row_defs:
        cur_items = [title]
        for key in order_of_keys:
            digits = 1 if 'success' in field else 4
            if key == 'area' and ('success' in field or 'avg' in field):
                cur_items.append('\\textbf{' + str(round(table_stats[key][field],digits)) + '}')
            else:
                cur_items.append(str(round(table_stats[key][field],digits)))
            if 'success' in field:
                cur_items[-1] += '\%'
        lines.append(' & '.join(cur_items) + ' \\\\')
    
    latex_table_string = table_prefix_string + '\n'.join(lines) + table_suffix_string
    with open(f'plots_for_paper/eigenvectors_classification/plots/table_latex.txt', 'w') as f:
        f.write(latex_table_string)

if __name__ == '__main__':
    generate_eigienvectors_classification_plots()