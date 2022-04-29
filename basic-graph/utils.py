import numpy as np

def genUndirectedAdjMatrix(range, size):
    """
        range: tuple of num range
        size: tuple of matrix size
        
        Warning:
            diagonal elements may not be 1
    """
    a = np.random.randint(*range, size=size)
    m = np.tril(a) + np.tril(a, -1).T
    return m