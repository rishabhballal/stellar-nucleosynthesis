import numpy as np
from data import mass

# rewriting data as: [proton number, neutron number, mass]
mass[:, 1] = mass[:, 1] - mass[:, 0]

def reaction(p1, p2, e):
    res = p1[0] + p1[1] + p2[0] + p2[1]

    # obtaining masses of the reactants
    mr1, mr2 = 0, 0
    for i in range(len(mass)):
        if mass[i, 0] == p1[0] and mass[i, 1] == p1[1]:
            mr1 = mass[i, 2]
        if mass[i, 0] == p2[0] and mass[i, 1] == p2[1]:
            mr2 = mass[i, 2]

    # identifying possible products (upto 2 elements)
    p = np.zeros(6)
    for i in range(len(mass)):
        if mass[i, 0] + mass[i, 1] == res:
            p = np.vstack((p, np.append(mass[i], np.zeros(3))))
            p = np.vstack((p, np.append(np.zeros(3), mass[i])))
        for j in range(len(mass)):
            if mass[i, 0] + mass[j, 0] + mass[i, 1] + mass[j, 1] == res:
                p = np.vstack((p, np.append(mass[i], mass[j])))
    p = p[1:]

    # computing reaction q values
    q = np.array([])
    for i in range(len(p)):
        q = np.append(q, (mr1 + mr2) - (p[i, 2] + p[i, 5]))

    p = np.delete(p, [2, 5], 1)

    # one percent of the energy is radiated out
    q += 0.99*e

    # including only positive q value reactions
    ind = []
    for i in range(len(q)):
        if q[i] <= 0:
            ind.append(i)
    p = np.delete(p, ind, 0)
    q = np.delete(q, ind, 0)

    # normalising q values as weighted probabilities
    norm = sum(q)
    q = np.vstack((q, q))
    q[1] /= 0.01*norm

    # determining the final reaction
    rn = np.append([p1, p2], 0)
    r = 100*np.random.rand(1)
    for i in range(len(p)):
        if r < sum(q[1, 0:i+1]):
            rn = np.append(p[i], q[0, i])
            break

    return rn
