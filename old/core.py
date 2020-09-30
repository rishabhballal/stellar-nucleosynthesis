import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d 

space = 10
bound = 2
core_dim = 3
core = (core_dim-1)/2

step = 1
u = np.arange(-space, space + step, step, dtype=float)
v = np.arange(-space, space + step, step, dtype=float)
x, y = np.meshgrid(u, v)

p, q = len(v), len(u)

z = np.zeros((p, q))
n = np.zeros((p, q))
for i in range(bound, p-bound):
    for j in range(bound, q-bound):
        z[i, j] = np.random.randint(2)
        if(np.random.rand(1) < 0.25):
            n[i, j] = 1

a = z + n
dens = 0 * a

print('\nINITIAL DISTRIBUTION')
print('\nmass number matrix: \n%s' %a)

num = 0
for i in range(p):
    for j in range(q):
        if(a[i, j] != 0):
            num += 1
m = sum(sum(a))
avgm = m/num

print('\nmass: %d' %m)
print('number of particles: %d' %num)
print('average particle mass: %.2f' %avgm)

mag = lambda vec: np.sqrt(np.inner(vec, vec))

def centreMass(a):
    cm = np.array([0, 0], dtype=int)
    
    s1, s2 = 0, 0
    for i in range(int((p-1)/2)):
        if(np.array_equal(a[i], np.zeros(q))):
            s1 = i+1
    for i in range(int((p-1)/2), p):
        if(np.array_equal(a[i], np.zeros(q))):
            s2 = i
            break
    
    cm1 = np.array(np.zeros(s1))
    for i in range(s1, s2):
        cm2 = 0
        for j in range(q):
            cm2 += (a[i, j]*j)/sum(a[i])
        cm1 = np.append(cm1, np.round(cm2))
    cm1 = np.append(cm1, np.zeros(p-s2))
    
    cm3 = 0
    for i in range(s1, s2):
        cm3 += (sum(a[i])*i)/m
    cm[0] = np.round(cm3)
    
    cm4 = 0
    for i in range(s1, s2):
        cm4 += (sum(a[i])*cm1[i])/m
    cm[1] = np.round(cm4)
    
    return cm

def density(a):
    for i in range(1, p-1):
        for j in range(1, q-1):
            dens[i, j] = (a[i-1, j-1] + a[i-1, j] + a[i-1, j+1] 
                          + a[i, j-1] + a[i, j] + a[i, j+1] 
                          + a[i+1, j-1] + a[i+1, j] + a[i+1, j+1])/9
            dens[i, j] = np.round(dens[i, j], 2)
    return dens

def positions(a):
    ind = np.zeros(2, dtype=int)
    for i in range(p):
        for j in range(q):
            if(a[i, j] != 0):
                ind = np.vstack((ind, np.array([i, j])))
    return ind[1:]

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

def pressure(a, ind):
    dens = density(a)
    cm = centreMass(a)
    
    cdens = 0
    for i in range(int(cm[0] - core), int(cm[0] + core + 1)):
        for j in range(int(cm[1] - core), int(cm[1] + core + 1)):
            cdens += dens[i, j]
    cdens /= core_dim**2
    print('\ncore dens : %.4f' %avg)
    
    maxim = 0
    for i in range(p):
        for j in range(q):
            if(a[i, j] > maxim):
                maxim = a[i, j]
    
    rad = 1 - (cdens/maxim)
    print('radiation : %.4f' %rad)
    
    ctemp = (1 - rad)*8
    print('core temp : %.2f' %ctemp)
    
    ax.scatter(time, avg, color='C0')
    ax.scatter(time, rad, color='C1')
    ax.scatter(time, ctemp, color='C3')
    
    return ctemp, cm

def profile(a, dstr, title):
    cm = centreMass(a)
    
    fig, ax = plt.subplots()
    
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
    ax.scatter(rm, profile, color='k')
    ax.grid()
    ax.set_xlabel('radial coordinate')
    ax.set_ylabel(title)
    plt.show()

dens = density(a)
cm = centreMass(a)

avg = 0
for i in range(int(cm[0] - core), int(cm[0] + core + 1)):
    for j in range(int(cm[1] - core), int(cm[1] + core + 1)):
        avg += dens[i, j]
avg /= core_dim**2

maxim = 0
for i in range(p):
    for j in range(q):
        if(a[i, j] > maxim):
            maxim = a[i, j]

rad = 1 - (avg/maxim)
ctemp = (1 - rad)*8

fig, ax = plt.subplots()
ax.scatter(0, avg, color='C0', label='core dens')
ax.scatter(0, rad, color='C1', label='radiation')
ax.scatter(0, ctemp, color='C3', label='core temp')

for time in range(1, 21):
    ind = positions(a)
    
    grav = gravity(a, ind)
    ctemp, cm = pressure(a, ind)
    R = mag(np.zeros(2) - cm)
    
    for i in range(len(ind)):
        j, k = ind[i, 0], ind[i, 1]
        pos = mag(ind[i] - cm)
        pr = 1 - pos/R
        if(np.random.rand(1) < pr):
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
    print(a)

ax.grid()
ax.set_ylim(0,)
ax.set_xlabel('iterations')
ax.legend()
plt.show()

profile(a, density(a), 'density')