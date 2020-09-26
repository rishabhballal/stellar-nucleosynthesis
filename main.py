import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

from centre_of_mass import centre_of_mass
from density import density_matrix
from positions import particle_positions
import nuclear as ncl

mag = lambda vec: np.sqrt(np.inner(vec, vec))

def gravity(a, ind):
    grav = np.zeros(2)
    for i in ind:
        f = np.zeros(2)
        for j in range(p):
            for k in range(q):
                if(i[0] != j and i[1] != k):
                    pos1 = np.array([i[0], i[1]])
                    pos2 = np.array([j, k])
                    rvec = pos2 - pos1
                    f += (a[i[0], i[1]]*a[j, k]
                          *rvec/mag(rvec)**3)
        grav = np.vstack((grav, f))
    grav = grav[1:]
    for i in grav:
        norm = abs(i[0]) + abs(i[1])
        i[0] /= norm
        i[1] /= norm
    return np.round(grav, 2)

def core_param(a, ind, cm):
    dens = density(a)

    cdens = 0
    for i in range(int(cm[0] - core), int(cm[0] + core + 1)):
        for j in range(int(cm[1] - core), int(cm[1] + core + 1)):
            cdens += dens[i, j]
    cdens /= core_dim**2
    print('core dens: %.4f' %cdens)

    maxim = np.array([])
    for i in range(p):
        for j in range(q):
            maxim = np.append(maxim, a[i, j])
    maxim = sorted(maxim)
    maxim = maxim[::-1]

    mdens = 0
    for i in range(int(core_dim**2)):
        mdens += maxim[i]
    mdens /= core_dim**2

    ctemp = 9*(cdens/mdens)
    print('core temp: 10^%.4f' %ctemp)

    return cdens, ctemp

def profile(a, dstr):
    cm = centreMass(a)

    r1 = np.arange(q-cm[1])
    p1 = dstr[cm[0], cm[1]:q]
    pl1 = len(p1)

    r2 = np.arange(cm[1])
    p2 = dstr[cm[0], cm[1]:0:-1]
    pl2 = len(p2)

    r3 = np.arange(p-cm[0])
    p3 = dstr[cm[0]:p, cm[1]]
    pl3 = len(p3)

    r4 = np.arange(cm[0])
    p4 = dstr[cm[0]:0:-1, cm[1]]
    pl4 = len(p4)

    rm = r1
    if(r2[-1] > r3[-1]):
        if(r2[-1] > r4[-1]):
            rm = r2
        elif(r3[-1] > r4[-1]):
            rm = r3
        else:
            rm = r4

    pl = np.array([pl1, pl2, pl3, pl4])
    p1 = np.hstack((p1, np.zeros(max(pl)-pl1)))
    p2 = np.hstack((p2, np.zeros(max(pl)-pl2)))
    p3 = np.hstack((p3, np.zeros(max(pl)-pl3)))
    p4 = np.hstack((p4, np.zeros(max(pl)-pl4)))

    profile = (p1 + p2 + p3 + p4)/4

    return rm, profile

def fusion(ind, cm, ctemp):
    r1 = np.arange(0, core, space*0.001)
    t1 = ctemp*np.ones(len(r1))
    r2 = np.arange(core, space, space*0.001)
    t2 = np.arange(ctemp, 0, -(ctemp*0.001))
    ra = np.append(r1, r2)
    tprof = np.append(t1, t2)

    tc = 6.5
    for i in ind:
        t = 0
        r = mag(i - cm)
        for j in range(len(ra)):
            if(np.isclose(r, ra[j], atol=0.001)):
                t = tprof[j]
        if(t > tc):
            i1 = i

            i2 = i1.copy()
            r = np.random.randint(4)

            if(r == 0):
                i2[0] -= 1
            elif(r == 1):
                i2[1] += 1
            elif(r == 2):
                i2[0] += 1
            else:
                i2[1] -= 1

            p1 = [z[i1[0], i1[1]], n[i1[0], i1[1]]]
            p2 = [z[i2[0], i2[1]], n[i2[0], i2[1]]]

            if(p1[0] == 0 or p2[0] == 0):
                f = 1
            else:
                cr = 1/(p1[0]*p2[0])
                if(np.random.rand(1) < cr):
                    f = (t - tc)/(9 - tc)
                else:
                    f = 0
            e = en[i[0], i[1]]
            rn = ncl.reaction(p1, p2, f, e)

            z[i1[0], i1[1]] = rn[0]
            n[i1[0], i1[1]] = rn[1]
            z[i2[0], i2[1]] = rn[2]
            n[i2[0], i2[1]] = rn[3]
            en[i1[0], i1[1]] = rn[4]
    return z + n

def count(z, n, ca):
    a = z + n
    m = sum(sum(a))
    ind = positions(a)
    print('composition:')

    el = np.zeros(2)
    for i in range(len(ind)):
        j, k = ind[i, 0], ind[i, 1]
        el = np.vstack((el, (z[j, k], n[j, k])))
    el = el[1:]

    c = np.zeros(5)
    comp = np.zeros(4)
    eld = np.zeros((2,2))

    for i in el:
        flag = 0
        for k in eld:
            if(np.array_equal(i, k)):
                flag = 1
        if(flag == 0):
            ctr = 0
            for j in el:
                if(np.array_equal(i, j)):
                    ctr += 1
            num = round(100*ctr/len(ind), 2)
            mass = round(100*ctr*(i[0] + i[1])/m, 2)
            comp = np.vstack((comp, np.array([i[0], i[1], num, mass])))
            # print('z: %d\tn: %d\tnumber percent: %.2f\tmass percent: %.2f' %(i[0], i[1], num, mass))
            if(i[0] == 1):
                c[0] += mass
            if(i[0] == 2):
                c[1] += mass
            if(i[0] == 6):
                c[2] += mass
            if(i[0] == 7):
                c[3] += mass
            if(i[0] == 8):
                c[4] += mass
            eld = np.vstack((eld, i))
    ca = np.vstack((ca, c))

    eld = eld[2:]
    comp = comp[1:]
    for i in range(len(comp)):
        for j in range(i, len(comp)):
            temp = 0
            if(comp[i, 0] > comp[j, 0]):
                temp = comp[i].copy()
                comp[i] = comp[j]
                comp[j] = temp
    print(comp)
    return ca

space = 10
bound = space//10
core = round(space*0.4)
core_dim = 2*core + 1

step = 1
u = np.arange(-space, space + step, step, dtype=float)
v = np.arange(-space, space + step, step, dtype=float)
x, y = np.meshgrid(u, v)

p, q = len(v), len(u)

z = np.zeros((p, q))
n = np.zeros((p, q))
for i in range(bound, p-bound):
    for j in range(bound, q-bound):
        if(np.random.rand(1) < 0.75):
            z[i, j] = 1
            if(np.random.rand(1) < 0.25):
                n[i, j] = 1
a = z + n
en = 0 * a

print('\nINITIAL DISTRIBUTION')

num = 0
for i in range(p):
    for j in range(q):
        if(a[i, j] != 0):
            num += 1
m = sum(sum(a))
avgm = m/num

print('\nmass: %d' %m)
print('number of elements: %d' %num)
print('average element mass: %.2f' %avgm)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, density(a))
ax.set_zlim(0, 4)
plt.show()

t = 0
# time = np.arange(21)
time = np.array([])
cd = np.array([])
ct = np.array([])
ca = np.zeros(5)

flag = 1
# for t in time:
while(flag):
    print()
    print(t)
    ca = count(z, n, ca)
    if(ca[-1, 0] < 10):
        flag = 0
    ind = positions(a)
    cm = centreMass(a)

    grav = gravity(a, ind)
    cdens, ctemp = core_param(a, ind, cm)

    cd = np.append(cd, cdens)
    ct = np.append(ct, ctemp)

    if(ctemp >= 7):
        a = fusion(ind, cm, ctemp)

    R = mag(np.zeros(2) - cm)

    for i in range(len(ind)):
        j, k = ind[i, 0], ind[i, 1]
        pos = mag(ind[i] - cm)

        if(np.random.rand(1) < abs(grav[i, 0])):
            if(grav[i, 0] >= 0):
                l = 1
            else:
                l = -1
            if(a[j+l, k] < a[j, k]):
                z[j, k], z[j+l, k] = z[j+l, k], z[j, k]
                n[j, k], n[j+l, k] = n[j+l, k], n[j, k]
        else:
            if(grav[i, 1] >= 0):
                l = 1
            else:
                l = -1
            if(a[j, k+l] < a[j, k]):
                z[j, k], z[j, k+l] = z[j, k+l], z[j, k]
                n[j, k], n[j, k+l] = n[j, k+l], n[j, k]
        a = z + n
    t += 1
ca = ca[1:]
time = np.arange(t)

num = 0
for i in range(p):
    for j in range(q):
        if(a[i, j] != 0):
            num += 1
m = sum(sum(a))
avgm = m/num

print('\nmass: %d' %m)
print('number of elements: %d' %num)
print('average element mass: %.2f' %avgm)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, density(a))
ax.set_zlim(0,)
plt.show()

fig, ax = plt.subplots()
ax.plot(time, ca[:, 0], label='hydrogen')
ax.plot(time, ca[:, 1], label='helium')
ax.plot(time, ca[:, 2], label='carbon')
ax.plot(time, ca[:, 3], label='nitrogen')
ax.plot(time, ca[:, 4], label='oxygen')
ax.grid()
ax.legend()
ax.set_ylim(0,)
ax.set_xlabel('time')
ax.set_ylabel('mass concentration')
plt.show()

fig, ax = plt.subplots()
ax.plot(time, cd)
ax.grid()
ax.set_ylim(0,)
ax.set_xlabel('time')
ax.set_ylabel('core density')
plt.show()

fig, ax = plt.subplots()
ax.plot(time, ct)
ax.grid()
ax.set_ylim(0,)
ax.set_xlabel('time')
ax.set_ylabel('core temperature')
plt.show()

r, dprof = profile(a, density(a))

fig, ax = plt.subplots()
ax.scatter(r, dprof)
ax.grid()
ax.set_xlabel('radial coordinate')
ax.set_ylabel('density')
plt.show()
