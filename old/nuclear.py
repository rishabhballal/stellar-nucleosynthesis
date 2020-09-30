from data import mass

import numpy as np
import matplotlib.pyplot as plt

mass[:, 1] = mass[:, 1] - mass[:, 0]
ml = len(mass)

def reaction(p1, p2, f, e):
    a1 = p1[0] + p1[1]
    a2 = p2[0] + p2[1]
    res = a1 + a2

    m1, m2 = 0, 0
    for i in range(ml):
        if(mass[i, 0] == p1[0] and mass[i, 1] == p1[1]):
            m1 = mass[i, 2]
        if(mass[i, 0] == p2[0] and mass[i, 1] == p2[1]):
            m2 = mass[i, 2]

    m3 = np.zeros(3)
    m4 = np.zeros(6)
    for i in range(ml):
        if((mass[i, 0] + mass[i, 1]) == res):
            m3 = np.vstack((m3, mass[i]))

        for j in range(ml):
            if((mass[i, 0] + mass[j, 0] + mass[i, 1] + mass[j, 1]) == res):
                m4 = np.vstack((m4, np.append(mass[i], mass[j])))

    q1 = np.zeros(5)
    if(m3.ndim > 1):
        m3 = m3[1:]

        for i in m3:
            q1 = np.vstack((q1, np.array([i[0], i[1], 0, 0,
                                          (m1 + m2) - i[2]])))
        q1 = q1[1:]

        for i in range(len(q1)):
            q1 = np.vstack((q1, q1[i]))
            q1[-1, 0], q1[-1, 2] = q1[-1, 2], q1[-1, 0]
            q1[-1, 1], q1[-1, 3] = q1[-1, 3], q1[-1, 1]

    q2 = np.zeros(5)
    if(m4.ndim > 1):
        m4 = m4[1:]

        for i in m4:
            q2 = np.vstack((q2, np.array([i[0], i[1], i[3], i[4],
                                          (m1 + m2) - (i[2] + i[5])])))
        q2 = q2[1:]

    q = np.vstack((q1, q2))

    if(np.array_equal(q1, np.zeros(5))):
        q = q[1:]

    q[:, -1] += 0.01*e

    # print(q)

    p = np.zeros(5)
    for i in range(len(q)):
        if(q[i, -1] > 0):
            p = np.vstack((p, q[i]))

    rn = np.array([p1[0], p1[1], p2[0], p2[1], 0])

    if(np.array_equal(p, np.zeros(5))):
        pass
    else:
        p = p[1:]
        norm = sum(p[:, -1])
        p[:, -1] /= norm
        p[:, -1] *= f

        r = np.random.rand(1)

        for i in range(len(p)):
            if(r < sum(p[0:i+1, -1])):
                rn = p[i]
                break

        for i in range(len(q)):
            if(np.array_equal(rn[0:3], q[i, 0:3])):
                rn[-1] = q[i, -1]
    return rn

# p1 = [0, 1]
# p2 = [1, 0]
# print(reaction(p1, p2, 1, 0))
