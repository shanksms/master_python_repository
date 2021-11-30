import numpy as np
import string
import pandas as pd
import seaborn as sns
import missingno as msno
import matplotlib.pyplot as plt



def min_max_scaler(x):
    unique_vals = np.unique(x)  # checks how many unique values
    if len(unique_vals) == 1 and isinstance(x, list):
        return np.array([0.5] * len(x))
    else:
        return (x - x.min()) / (x.max() - x.min())


def strip_punctuation(text):
    return ''.join(s for s in text if s not in string.punctuation)


def missing_data_check_visualization():
    sns.set_style('white')
    df = pd.read_csv('bostan_ei-corrupt.csv')
    msno.matrix(df)
    plt.show()



if __name__ == '__main__':
    missing_data_check_visualization()