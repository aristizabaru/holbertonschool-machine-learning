#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

plt.plot(y, color='r')
# adjust the limits of the axis
plt.xlim(left=0, right=10)
plt.show()
