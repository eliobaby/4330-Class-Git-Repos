import numpy as np

def list_sum(x):
    sum = 0
    for i in x:
        sum += i
    return sum

x = np.array([1, 2, 3])
print(list_sum(x))
