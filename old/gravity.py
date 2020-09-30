import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d 

space = 5
bound = int(space/10)

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
            n[i, j] = np.round(np.random.rand(1))

a = z + n
dens = 0 * a
temp = 0 * a

print('\nINITIAL DISTRIBUTION')
print('\nmass number matrix: \n%s' %a)

m = sum(sum(a))

mag = lambda vec: np.sqrt(np.inner(vec, vec))

def centreMass(a):
    cm = np.array([0, 0], dtype=float)
    
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
    for i in range(len(ind)):
            f = np.zeros(2)
            for j in range(p):
                for k in range(q):
                    if(ind[i, 0] != j and ind[i, 1] != k):
                        pos1 = np.array([ind[i, 0], ind[i, 1]])
                        pos2 = np.array([j, k])
                        rvec = pos2 - pos1
                        f += (a[ind[i, 0], ind[i, 1]]*a[j, k]
                              *rvec/mag(rvec)**3)
            grav = np.vstack((grav, f))
    grav = grav[1:]
    for i in range(len(grav)):
        norm = abs(grav[i, 0]) + abs(grav[i, 1])
        grav[i, 0] /= norm
        grav[i, 1] /= norm
    return np.round(grav, 2)

dens1 = density(a)
# print('\ndensity matrix: \n%s' %dens1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, dens1)
ax.set_zlim(0, 4)
plt.show()

for time in range(1, 21):
    print(time)
    ind = positions(a)
    
    grav = gravity(a, ind)
    for i in range(len(grav)):
        r1 = np.random.rand(1)
        j, k = ind[i, 0], ind[i, 1]
        if(r1 <= abs(grav[i, 0])):
            if(grav[i, 0] >= 0):
                move = 1
            else:
                move = -1
            if(a[j+move, k] < a[j, k]):
                z[j, k], z[j+move, k] = z[j+move, k], z[j, k]
                n[j, k], n[j+move, k] = n[j+move, k], n[j, k]
        else:
            if(grav[i, 1] >= 0):
                move = 1
            else:
                move = -1
            if(a[j, k+move] < a[j, k]):
                z[j, k], z[j, k+move] = z[j, k+move], z[j, k]
                n[j, k], n[j, k+move] = n[j, k+move], n[j, k]
        a = z + n

print('\nAFTER GRAVITATIONAL COLLAPSE')
print('\nmass number matrix: \n%s' %a)

dens2 = density(a)
# print('\ndensity matrix: \n%s' %dens2)

cm = centreMass(a)
print('\ncentre of mass: %s' %cm)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, dens2)
ax.set_zlim(0, 4)
plt.show()
