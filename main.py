import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import matrix
import density
import gravity

z, n, a = matrix.generator()
print('\nATOMIC MASS NUMBER MATRIX')
print(a)

pos = matrix.positions(a)
cm = matrix.centre_of_mass(a, pos)
print('\nCENTRE OF MASS: ', cm)

dens = density.matrix(a)
print('\nDENSITY MATRIX')
print(dens)

density.plot(dens)
density.profile(dens, cm)

grav = gravity.force(a, pos)

print()
