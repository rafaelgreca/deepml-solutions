import numpy as np

def shuffle_data(X, y, seed=None):
    # Your code here
    np.random.seed(seed)

    indexes = np.arange(0, X.shape[0])
    np.random.shuffle(indexes)

    return X[indexes], y[indexes]
