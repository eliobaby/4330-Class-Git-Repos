import numpy as np

def list_product(x):
    product = 1
    for i in range(len(x)):
        product *= x[i]
    return product

x = np.array([1, 2, 3])
print(list_product(x))
