#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

names = ['Farrah', 'Fred', 'Felicia']
# slice matrix by rows
apples = fruit[0, :]
bananas = fruit[1, :]
oranges = fruit[2, :]
peaches = fruit[3, :]

# colum width
width = 0.5

plt.bar(names, apples, width=width, label='apples', color='red')
plt.bar(names, bananas, width=width, label='bananas',
        bottom=apples, color='yellow')
plt.bar(names, oranges, width=width, label='oranges',
        bottom=apples + bananas, color='#ff8000')
plt.bar(names, peaches, width=width, label='peaches',
        bottom=apples + bananas + oranges, color='#ffe5b4')


plt.yticks(np.arange(0, 81, 10))
plt.legend(loc="upper right")

plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')

# Display legend
plt.legend()
plt.tight_layout()
plt.show()
