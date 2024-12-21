import numpy as np
import sys

def generate_data_for_sweeping_line_plots(seed):
    n = 11
    np.random.seed(seed)
    rects = np.random.rand(2, n)
    np.save('plots_for_paper/sweeping_line/data/rects', rects)

if __name__ == '__main__':
    generate_data_for_sweeping_line_plots(int(sys.argv[1]))