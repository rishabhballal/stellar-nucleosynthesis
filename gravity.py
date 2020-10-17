import numpy as np


def force(a, pos):
    '''Computes the gravitational force acting on each element of the
    matrix and returns it as normalised directional probabilities.
    '''

    # returns the magnitude of a vector
    def mag(vec): return np.sqrt(np.inner(vec, vec))

    grav = np.array([0, 0], dtype=float)

    for i in pos:
        f = np.array([0, 0], dtype=float)
        for j in pos:
            rvec = j - i
            if rvec.any():
                f += a[i[0], i[1]] * a[j[0], j[1]] * rvec/mag(rvec)
        grav = np.vstack((grav, f))
    grav = grav[1:]

    for i in range(len(grav)):
        norm = abs(grav[i, 0]) + abs(grav[i, 1])
        grav[i, 0] /= norm
        grav[i, 1] /= norm

    return np.round(grav, 2)
