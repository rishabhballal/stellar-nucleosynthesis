import numpy as np


def generate(dim):
    '''Returns three (dim x dim) matrices:
    z - proton number matrix
    n - neutron number matrix
    a - mass number matrix = z + n

    The only condition imposed on their randomisation is to generate
    Hydrogen and Deuterium in the initial state of the star.
    '''

    bound = dim//10 if dim >= 10 else 1

    z = np.zeros((dim, dim), dtype=int)
    n = np.zeros((dim, dim), dtype=int)
    for i in range(bound, dim-bound):
        for j in range(bound, dim-bound):
            z[i, j] = np.random.randint(2)
            if z[i, j]:
                n[i, j] = np.random.randint(2)

    a = z + n
    return z, n, a


def positions(a):
    '''Returns the indices of all nonzero elements in the matrix.'''

    pos = np.array([0, 0], dtype=int)

    for i in range(len(a)):
        for j in range(len(a)):
            if a[i, j]:
                pos = np.vstack((pos, [i, j]))

    return pos[1:]


def centre_of_mass(a, pos):
    '''Returns the indices of the centre of mass of the matrix.'''

    cm = np.array([0, 0], dtype=float)

    for i in pos:
        cm += i*a[i[0], i[1]]
    cm /= a.sum()
    cm = np.round(cm)

    return np.array([cm[0], cm[1]], dtype=int)


def core(a, pos, cm):
    '''Returns the indices of the core of the matrix, as well as the
    temperature, computed as an order of magnitude.
    '''

    # returns the magnitude of a vector
    def mag(vec): return np.sqrt(np.inner(vec, vec))

    c_dim = int(0.2*len(a)) if len(a) >= 10 else 1

    c_pos = np.zeros(2, dtype=int)
    for i in pos:
        r = mag(i - cm)
        if r <= c_dim:
            c_pos = np.vstack((c_pos, i))
    c_pos = c_pos[1:]

    c_a = []
    for i, j in c_pos:
        c_a.append(a[i, j])

    c_dens = sum(c_a)/len(c_a)
    c_temp = 10*c_dens/max(c_a)

    return c_pos, c_temp
