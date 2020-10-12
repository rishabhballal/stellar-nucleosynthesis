import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import matrix
import density
import gravity
import nuclear

dim = 20

z, n, a = matrix.generate(dim)
print('\nINITIAL ATOMIC MASS NUMBER MATRIX')
print(a)

# pos = matrix.positions(a)
# cm = matrix.centre_of_mass(a, pos)
# print('\nCENTRE OF MASS: ', cm)
#
# dens = density.matrix(a)
# density.plot(dens)

en = 0*a

time = 20
print('\nITERATIONS')
for t in range(time):
    print(t+1)

    pos = matrix.positions(a)
    cm = matrix.centre_of_mass(a, pos)
    core, c_temp = matrix.core_temp(a, cm)

    if c_temp > 7:
        c_pos = matrix.positions(core)
        print(c_pos)
        # for i in c_pos:
        #     j = i.copy()
        #
        #     r = np.random.randint(2, size=2)
        #     # r[0] determines the axis
        #     # horizontal axis: r[0] = 0, vertical axis: r[0] = 1
        #     # r[1] determines the direction along the axis
        #     dir = (-1)**r[1]
        #     if r[0]:
        #         j[0] += dir
        #     else:
        #         j[1] += dir
        #
        #     p1 = [z[i[0], i[1]], n[i[0], i[1]]]
        #     p2 = [z[j[0], j[1]], n[j[0], j[1]]]
        #     print(p1, p2)
        #     e = en[i[0], i[1]]
        #     rn = nuclear.reaction(p1, p2, e)
        #     z[i[0], i[1]] = rn[0]
        #     n[i[0], i[1]] = rn[1]
        #     z[j[0], j[1]] = rn[2]
        #     n[j[0], j[1]] = rn[3]
        #     a = z + n
        #     en[i[0], i[1]] = rn[4]

    grav = gravity.force(a, pos)
    for i in range(len(grav)):
        r = np.random.rand(1)
        j, k = pos[i]

        if r <= abs(grav[i, 0]):
            dir = int(grav[i, 0]/abs(grav[i, 0]))
            if a[j+dir, k] < a[j, k]:
                z[j, k], z[j+dir, k] = z[j+dir, k], z[j, k]
                n[j, k], n[j+dir, k] = n[j+dir, k], n[j, k]
        else:
            dir = int(grav[i, 1]/abs(grav[i, 1]))
            if a[j, k+dir] < a[j, k]:
                z[j, k], z[j, k+dir] = z[j, k+dir], z[j, k]
                n[j, k], n[j, k+dir] = n[j, k+dir], n[j, k]
        a = z + n

print('\nFINAL ATOMIC MASS NUMBER MATRIX')
print(a)

# pos = matrix.positions(a)
# cm = matrix.centre_of_mass(a, pos)
#
# dens = density.matrix(a)
# density.plot(dens)
# density.profile(dens, cm)
