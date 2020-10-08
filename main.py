import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import matrix
import density
import gravity
import core

z, n, a = matrix.generator()
print('\nINITIAL ATOMIC MASS NUMBER MATRIX')
print(a)

pos = matrix.positions(a)
cm = matrix.centre_of_mass(a, pos)
print('\nCENTRE OF MASS: ', cm)

dens = density.matrix(a)
density.plot(dens)

time = 20
print('\nITERATIONS')
for t in range(1, time+1):
    print(t)
    pos = matrix.positions(a)
    cm = matrix.centre_of_mass(a, pos)

    temp = core.temp(a, cm)
    if temp > 7:
        pass

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

pos = matrix.positions(a)
cm = matrix.centre_of_mass(a, pos)

dens = density.matrix(a)
density.plot(dens)
density.profile(dens, cm)
