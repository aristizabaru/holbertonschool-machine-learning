#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size

np.random.seed(5)

x = np.random.randn(2000) * 10
y = np.random.randn(2000) * 10
z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

plt.scatter(x, y, c=z, cmap='viridis')
# set the bar in position
cbar = plt.colorbar()
# set labels
cbar.set_label('elevation (m)')
plt.xlabel('x coordinate (m)')
plt.ylabel('y coordinate (m)')

plt.title('Mountain Elevation')
plt.show()
