import numpy as np

def gravity(a, pos):
    grav = np.array([0, 0], dtype=float)
    for i in pos:
        for j in pos:
            pass


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
#         z[i, j] = np.round(np.random.rand(1))
#         if z[i, j]:
#             n[i, j] = np.round(np.random.rand(1))
# a = z + n
# print(a)
#
# pos = particle_positions(a)
# print(gravity(a, pos))
