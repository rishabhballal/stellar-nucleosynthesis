def density_matrix(a):
    dens = 0*a

    for i in range(1, len(a)-1):
        for j in range(1, len(a)-1):
            dens[i, j] = round(sum(sum(a[i-1:i+2, j-1:j+2]))/9, 2)

    return dens

# TEST SECTION
#
# import numpy as np
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
# print(density_matrix(a))
