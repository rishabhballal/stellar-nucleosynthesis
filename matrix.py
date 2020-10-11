import numpy as np

def generator():
    dim = 20
    bound = dim//10

    z = np.zeros((dim, dim))
    n = np.zeros((dim, dim))
    for i in range(bound, dim-bound):
        for j in range(bound, dim-bound):
            z[i, j] = np.random.randint(2)
            if z[i, j]:
                n[i, j] = np.random.randint(2)
    a = z + n

    return z, n, a

def positions(a):
    pos = np.array([0, 0], dtype=int)

    for i in range(len(a)):
        for j in range(len(a)):
            if a[i, j]:
                pos = np.vstack((pos, [i, j]))

    return pos[1:]

def centre_of_mass(a, pos):
    cm = np.array([0, 0], dtype=float)

    for i in pos:
        cm += i*a[i[0], i[1]]
    cm /= a.sum()
    cm = np.round(cm)

    return np.array([cm[0], cm[1]], dtype=int)

def core_temp(a, cm):
    dim = 4
    core = a[cm[0]-dim:cm[0]+dim+1, cm[1]-dim:cm[1]+dim+1]

    dens = core.sum()/core.size
    maxim = core.max()

    t = 10*dens/maxim
    return t
