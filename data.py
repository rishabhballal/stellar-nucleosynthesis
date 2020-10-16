import numpy as np
import matplotlib.pyplot as plt


def composition(z, pos):
    # [atomic number, percentage by mass]
    comp = np.array([[0, 0], [1, 0]], dtype=float)
    for i, j in pos:
        if z[i, j] not in comp[:, 0]:
            comp = np.vstack((comp, [z[i, j], 0]))
    comp = comp[1:]

    # counting their occurence
    for i in range(len(comp)):
        for j, k in pos:
            if z[j, k] == comp[i, 0]:
                comp[i, 1] += 1
        comp[i, 1] *= comp[i, 0] * 100/z.sum()

    # sorting according to atomic number
    for i in range(len(comp)):
        for j in range(i+1, len(comp)):
            if comp[i, 0] > comp[j, 0]:
                comp[i, 0], comp[j, 0] = comp[j, 0], comp[i, 0]
                comp[i, 1], comp[j, 1] = comp[j, 1], comp[i, 1]

    return np.round(comp, 2)


def log(comp, type, iter):
    with open('log.txt', type) as file:
        file.write('iteration %d\n' %iter)
        for i in comp:
            file.write('%d: %.2f\n' %(i[0], i[1]))
        file.write('\n')


def plot(elm, iter):
    labels = ['Hydrogen', 'Helium', 'Carbon', 'Nitrogen', 'Oxygen']
    fig, ax = plt.subplots()
    for i in range(len(elm[0])):
        ax.plot(range(iter), elm[:, i], label=labels[i])
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Percentage by mass')
    ax.grid()
    ax.legend()
    plt.savefig('images/data.jpg')
