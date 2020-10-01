def generator():
    dim = 5
    bound = 1

    z = np.zeros((dim, dim))
    n = np.zeros((dim, dim))
    for i in range(bound, dim-bound):
        for j in range(bound, dim-bound):
            z[i, j] = np.random.randint(2)
            if z[i, j]:
                n[i, j] = np.random.randint(2)
    a = z + n
    return a

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
    cm /= sum(sum(a))
    cm = np.round(cm)

    return np.array([cm[0], cm[1]], dtype=int)
