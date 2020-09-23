import time
import numpy as np
from eff_loop import iter_range

def centre_of_mass(a):
    m = sum(sum(a))
    cm = np.array([0, 0])

    v, h = iter_range(a)

    for i in range(v[0], v[1]):
        for j in range(h[0], h[1]):
            pass

    return v, h

dim = 20
bound = 2

z = np.zeros((dim, dim))
n = np.zeros((dim, dim))
for i in range(bound, dim-bound):
    for j in range(bound, dim-bound):
        z[i, j] = np.round(np.random.rand(1))
        if z[i, j]:
            n[i, j] = np.round(np.random.rand(1))
a = z + n
# print(a)

print(centre_of_mass(a))
