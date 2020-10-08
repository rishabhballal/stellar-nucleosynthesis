import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def matrix(a):
    dens = 0*a

    for i in range(1, len(a)-1):
        for j in range(1, len(a)-1):
            d = a[i-1:i+2, j-1:j+2]
            dens[i, j] = round(d.sum()/d.size, 2)

    return dens

def plot(dens):
    u = v = np.arange(0, len(dens), dtype=float)
    x, y = np.meshgrid(u, v)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, dens)
    ax.set_zlim(0, )
    plt.show()

def profile(dens, cm):
    prof1 = dens[cm[0], cm[1]:len(dens)]
    prof2 = dens[cm[0]:len(dens), cm[1]]
    prof3 = dens[cm[0], cm[1]:0:-1]
    prof4 = dens[cm[0]:0:-1, cm[1]]

    maxim = max(cm) if len(dens)/2 < max(cm) else len(dens) - min(cm)

    def normalise_length(arr):
        while len(arr) < maxim:
            arr = np.append(arr, 0)
        return arr

    prof1 = normalise_length(prof1)
    prof2 = normalise_length(prof2)
    prof3 = normalise_length(prof3)
    prof4 = normalise_length(prof4)

    prof = (prof1 + prof2 + prof3 + prof4)/4

    r = np.arange(maxim)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(r, prof)
    ax.grid()
    plt.show()
