import numpy as np

def particle_positions(a):
    pos = np.array([0, 0], dtype=int)

    for i in range(len(a)):
        for j in range(len(a)):
            if a[i, j]:
                pos = np.vstack((pos, [i, j]))

    return pos[1:]

# TEST SECTION
#
# dim = 5
# bound = 1
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
# print(positions(a))
