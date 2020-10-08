import numpy as np

def temp(a, cm):
    dim = 4
    core = a[cm[0]-dim:cm[0]+dim+1, cm[1]-dim:cm[1]+dim+1]

    dens = core.sum()/core.size
    maxim = core.max()

    t = 10*dens/maxim
    return t
