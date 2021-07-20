#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)


# set the bins for data
bins = np.arange(0, 110, 10)
# set ticks 10 t0 10
plt.xticks(bins)
# set histogram
plt.hist(student_grades, edgecolor='black', bins=bins)
# set limits
plt.xlim(left=0, right=100)
plt.ylim(bottom=0, top=30)
# set labels
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Project A')
plt.show()
