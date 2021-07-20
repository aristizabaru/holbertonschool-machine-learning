#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)


# set font
plt.rcParams.update({'font.size': 6})
# set grid
grid = plt.GridSpec(3, 2, wspace=0.3, hspace=0.8)
# set tittle
plt.suptitle('All in One', fontsize=17)

# linear plot
plt.subplot(grid[0, 0])
plt.plot(y0, color='r')
plt.xlim(left=0, right=10)

# scatter
plt.subplot(grid[0, 1])
plt.scatter(x1, y1, color='m', marker='.')
plt.xlabel('Height (in)')
plt.ylabel('Weight (lbs)')
plt.title("Men's Height vs Weigh")

# linear plot log
plt.subplot(grid[1, 0])
plt.plot(x2, y2)
plt.xlim(left=0, right=28650)
plt.yscale('log')
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of C-14')

# linear plot log x 2
plt.subplot(grid[1, 1])
plt.plot(x3, y31, color='r', linestyle='--', label='C-14')
plt.plot(x3, y32, color='g', label='Ra-226')
plt.xlim(left=0, right=20000)
plt.ylim(bottom=0, top=1)
plt.legend()
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of Radioactive Elements')

# histogram
plt.subplot(grid[2, 0:])
bins = np.arange(0, 110, 10)
plt.xticks(bins)
plt.hist(student_grades, edgecolor='black', bins=bins)
plt.xlim(left=0, right=100)
plt.ylim(bottom=0, top=30)
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Project A')


plt.show()
