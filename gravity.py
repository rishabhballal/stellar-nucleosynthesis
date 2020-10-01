import numpy as np

mag = lambda vec: np.sqrt(np.inner(vec, vec))

def force(a, pos):
    grav = np.array([0, 0], dtype=float)

    for i in pos:
        f = np.array([0, 0], dtype=float)
        for j in pos:
            rvec = j - i
            if rvec.any():
                f += a[i[0], i[1]]*a[j[0], j[1]]*rvec/mag(rvec)
        grav = np.vstack((grav, f))
    grav = grav[1:]

    for i in range(len(grav)):
        norm = abs(grav[i, 0]) + abs(grav[i, 1])
        grav[i, 0] /= norm
        grav[i, 1] /= norm

    return np.round(grav, 2)
