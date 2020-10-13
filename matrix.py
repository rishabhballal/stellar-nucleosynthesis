import numpy as np

def generate(dim):
    bound = dim//10 if dim >= 10 else 1

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

mag = lambda vec: np.sqrt(np.inner(vec, vec))

def core(a, cm):
    dim = int(0.2*len(a)) if len(a) >= 10 else 1

    c_pos = np.zeros(2, dtype=int)
    for i in range(len(a)):
        for j in range(len(a)):
            r = mag([i, j] - cm)
            if r <= dim:
                c_pos = np.vstack((c_pos, [i, j]))

    c_a = []
    for i in c_pos:
        c_a.append(a[i[0], i[1]])

    c_dens = sum(c_a)/len(c_a)
    c_temp = 10 * c_dens/max(c_a)

    return c_pos[1:], c_temp
