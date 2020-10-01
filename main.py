import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import matrix
import density


mag = lambda vec: np.sqrt(np.inner(vec, vec))
