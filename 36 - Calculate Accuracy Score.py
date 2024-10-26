import numpy as np

def accuracy_score(y_true, y_pred):
    # Your code here
    return sum(np.where(y_true == y_pred, 1, 0))/y_true.shape[0] * 1.
