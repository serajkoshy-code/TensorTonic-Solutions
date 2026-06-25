import numpy as np

def sample_var_std(x):
    mean_x = np.mean(x)
    n = len(x)
    var = np.sum((x - mean_x) ** 2) / (n - 1) 
    stdev = np.sqrt(var)
    return var, stdev
    # Write code here
    pass