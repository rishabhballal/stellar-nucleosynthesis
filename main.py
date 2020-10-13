import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import matrix
import density
import gravity
import nuclear

np.seterr(all='ignore')

# minimum = 10
dim = 20

z, n, a = matrix.generate(dim)
print('\nINITIAL ATOMIC MASS NUMBER MATRIX')
print(a)

m = a.sum()
print('\nMASS: ', m)

pos = matrix.positions(a)
cm = matrix.centre_of_mass(a, pos)
print('\nCENTRE OF MASS: ', cm)

dens = density.matrix(a)
density.plot(dens)

en = 0*a

flag1 = 0
time = 20
print('\nITERATIONS')
for t in range(time):
    print(t+1)

    pos = matrix.positions(a)
    cm = matrix.centre_of_mass(a, pos)
    c_pos, c_temp = matrix.core(a, cm)

    if not flag1:
        if c_temp > 7:
            flag1 = 1
    else:
        for i in c_pos:
            j = i.copy()

            r = np.random.randint(2, size=2)
            # r[0] determines the axis (horizontal: 0, vertical: 1)
            # r[1] determines the direction along the axis
            dir = (-1)**r[1]
            if r[0]:
                j[0] += dir
            else:
                j[1] += dir

            p1 = [z[i[0], i[1]], n[i[0], i[1]]]
            p2 = [z[j[0], j[1]], n[j[0], j[1]]]
            try:
                f = c_temp/(p1[0]*p2[0])
                if f > 1:
                    f = 1
            except ZeroDivisionError:
                f = 1
            e = en[i[0], i[1]]

            nr = nuclear.reaction(p1, p2, f, e)
            z[i[0], i[1]] = nr[0]
            n[i[0], i[1]] = nr[1]
            z[j[0], j[1]] = nr[2]
            n[j[0], j[1]] = nr[3]
            a = z + n
            en[i[0], i[1]] = nr[4]

    pos = matrix.positions(a)
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
