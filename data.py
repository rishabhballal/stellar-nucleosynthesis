import numpy as np
import matplotlib.pyplot as plt

def composition(z, pos):
    # [atomic number, percentage by mass]
    comp = np.array([0, 0], dtype=float)
    for i in range(1, z.max()):
        comp = np.vstack((comp, [i, 0]))

    # counting their occurence
    for i in range(len(comp)):
        for j, k in pos:
            if z[j, k] == comp[i, 0]:
                comp[i, 1] += 1
        comp[i, 1] *= comp[i, 0] * 100/z.sum()

    return np.round(comp[1:], 2)

def log(comp, type, iter):
    with open('log.txt', type) as file:
        file.write('iteration %d\n' %iter)
        for i in comp:
            file.write('%d: %.2f\n' %(i[0], i[1]))
        file.write('\n')
