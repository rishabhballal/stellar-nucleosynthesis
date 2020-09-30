import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

from positions import particle_positions
from centre_of_mass import centre_of_mass
import density


mag = lambda vec: np.sqrt(np.inner(vec, vec))
