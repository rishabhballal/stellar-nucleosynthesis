import numpy as np
from eff_loop import iter_range

def centre_of_mass(a):
    m = sum(sum(a))
    cm = np.array([0, 0])

    h, v = iter_range(a)

    cm = np.array([0, 0], dtype=float)

    cm_h = np.zeros(len(a))
    for i in range(h[0], h[1]):
        for j in range(v[0], v[1]):
            cm_h[i] += j*a[i, j]
        cm_h[i] /= sum(a[:, i])

    cm_v = np.zeros(len(a))
    for i in range(v[0], v[1]):
        for j in range(h[0], h[1]):
            cm_v[i] += j*a[i, j]
        cm_v[i] /= sum(a[i])

    for i in range(len(a)):
        cm[0] += i*cm_h[i]
        cm[1] += i*cm_v[i]
    cm[0] /= sum(cm_h)
    cm[1] /= sum(cm_v)

    return np.round(cm)

# TEST SECTION
#
# dim = 20
# bound = 2
#
# z = np.zeros((dim, dim))
# n = np.zeros((dim, dim))
# for i in range(bound, dim-bound):
#     for j in range(bound, dim-bound):
#         z[i, j] = np.round(np.random.rand(1))
#         if z[i, j]:
#             n[i, j] = np.round(np.random.rand(1))
# a = z + n
# print(a)
#
# print(centre_of_mass(a))
