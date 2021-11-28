import numpy as np

def min_max_scaler(x):
    unique_vals = np.unique(x)  # checks how many unique values
    if len(unique_vals) == 1 and isinstance(x, list):
        return np.array([0.5] * len(x))
    else:
        return (x - x.min()) / (x.max() - x.min())


