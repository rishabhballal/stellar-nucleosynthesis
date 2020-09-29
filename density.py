import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def matrix(a):
    dens = 0*a

    for i in range(1, len(a)-1):
        for j in range(1, len(a)-1):
            dens[i, j] = round(sum(sum(a[i-1:i+2, j-1:j+2]))/9, 2)

    return dens

def plot(dens):
    u = v = np.arange(0, len(dens), dtype=float)
    x, y = np.meshgrid(u, v)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, matrix(a))
    ax.set_zlim(0, )
    plt.show()

def profile(dens, cm):
    print(cm)
    prof1 = dens[cm[0], cm[1]:len(dens)]
    prof2 = dens[cm[0]:len(dens), cm[1]]
    prof3 = dens[cm[0], cm[1]:0:-1]
    prof4 = dens[cm[0]:0:-1, cm[1]]
    print(prof1, prof2, prof3, prof4)

    # r = np.arange(len(prof1))
    # fig, ax = plt.subplots(figsize=(8, 6))
    # ax.plot(r, prof1)
    # ax.grid()
    # plt.show()

# TEST SECTION

from centre_of_mass import centre_of_mass
from positions import particle_positions

dim = 10
bound = 2

z = np.zeros((dim, dim))
n = np.zeros((dim, dim))
for i in range(bound, dim-bound):
    for j in range(bound, dim-bound):
        z[i, j] = np.random.randint(2)
        if z[i, j]:
            n[i, j] = np.random.randint(2)
a = z + n
# print(a)

dens = matrix(a)
print(dens)
# plot(dens)

pos = particle_positions(a)
cm = centre_of_mass(a, pos)
profile(dens, cm)
