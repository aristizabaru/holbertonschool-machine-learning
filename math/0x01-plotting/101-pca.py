#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

lib = np.load("pca.npz")
data = lib["data"]
labels = lib["labels"]

data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)

# create figure
fig = plt.figure()
# create subplot
ax = fig.add_subplot(111, projection='3d')
# get colums for x, y, and z
x = pca_data[:, 0]
y = pca_data[:, 1]
z = pca_data[:, 1]
ax.scatter(x, y, z, c=labels, cmap=plt.cm.plasma)
ax.set_xlabel('U1')
ax.set_ylabel('U2')
ax.set_zlabel('U3')
ax.set_title('PCA of Iris Dataset')
plt.show()
