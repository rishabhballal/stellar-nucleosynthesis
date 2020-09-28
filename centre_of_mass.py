import numpy as np

def centre_of_mass(a, pos):
    cm = np.array([0, 0], dtype=float)

    for i in pos:
        cm += i*a[i[0], i[1]]
    cm /= sum(sum(a))
    cm = np.round(cm)

    return np.array([cm[0], cm[1]], dtype=int)

# TEST SECTION
#
# from positions import particle_positions
#
# dim = 20
# bound = 2
#
# z = np.zeros((dim, dim))
# n = np.zeros((dim, dim))
# for i in range(bound, dim-bound):
#     for j in range(bound, dim-bound):
#         z[i, j] = np.random.randint(2)
#         if z[i, j]:
#             n[i, j] = np.random.randint(2)
# a = z + n
# print(a)
#
# pos = particle_positions(a)
# print(centre_of_mass(a, pos))
