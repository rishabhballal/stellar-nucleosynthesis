import numpy as np

def composition(z, pos):
    # [atomic number, percentage by number, percentage by mass]
    comp = np.array([[0, 0, 0], [1, 0, 0]])

    # identifying the elements
    for i, j in pos:
        if z[i, j] not in comp[:, 0]:
            comp = np.vstack((comp, [z[i, j], 0, 0]))
    comp = comp[1:]

    # counting their occurence
    for i in range(len(comp)):
        for j, k in pos:
            if z[j, k] == comp[i, 0]:
                comp[i, 1] += 1
                comp[i, 2] += 1
        comp[i, 1] *= 100/np.count_nonzero(z)
        comp[i, 2] *= comp[i, 0] * 100/z.sum()

    # sorting the elements by proton number
    for i in range(len(comp)):
        for j in range(i+1, len(comp)):
            if comp[i, 0] > comp[j, 0]:
                comp[i, 0], comp[j, 0] = comp[j, 0], comp[i, 0]
                comp[i, 1], comp[j, 1] = comp[j, 1], comp[i, 1]
                comp[i, 2], comp[j, 2] = comp[j, 2], comp[i, 2]

    return np.round(comp, 2)

def log(comp, type, iter):
    with open('log.txt', type) as file:
        file.write('iteration %d\n' %iter)
        for i in comp:
            file.write('%d: %.2f, %.2f\n' %(i[0], i[1], i[2]))
        file.write('\n')
