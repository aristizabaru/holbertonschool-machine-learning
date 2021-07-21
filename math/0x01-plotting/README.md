# 0x01. Plotting

## About

This is an educational project exploring concepts about **Plotting** towards a formation in Machine Learning.

## Table of contents

- [Requirements](#requirements)
  - [Installing Matplotlib 3.0](#installing-matplotlib-3)
  - [Dependencies](#dependencies)
- [Topics](#topics)
- [Read or watch](#read-or-watch)
- [Files](#files)
  - [0. Line Graph](#0-line-graph)
  - [1. Scatter](#1-satter)
  - [2. Change of scale](#2-change-of-scale)
  - [3. Two is better than one](#3-two-is-better-than-one)
  - [4. Frequency](#4-frequency)
  - [5. All in One](#5-all-in-one)
  - [6. Stacking Bars](#6-stacking-bars)
  - [7. Gradient](#7-gradient)
  - [8. PCA](#8-pca)

## Requirements

- Python 3.6.14

### Installing Matplotlib 3.0

```
pip install --user matplotlib==3.0
pip install --user Pillow
sudo apt-get install python3-tk
```

### Dependencies

Please refer at the [requirements.txt](../../requirements.txt) file at the root of this repository.

## Topics

- What is a plot?
- What is a scatter plot? line graph? bar graph? histogram?
- What is `matplotlib`?
- How to plot data with `matplotlib`
- How to label a plot
- How to scale an axis
- How to plot multiple sets of data at the same time

## Read or watch

Before start please read or watch this concepts.

- [Plot (graphics)](https://en.wikipedia.org/wiki/Plot_%28graphics%29)
- [Scatter plot](https://en.wikipedia.org/wiki/Scatter_plot)
- [Line chart](https://en.wikipedia.org/wiki/Line_chart)
- [Bar chart](https://en.wikipedia.org/wiki/Bar_chart)
- [Histogram](https://en.wikipedia.org/wiki/Histogram)
- [Pyplot tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
- [matplotlib.pyplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html)
- [matplotlib.pyplot.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
- [matplotlib.pyplot.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)
- [matplotlib.pyplot.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)
- [matplotlib.pyplot.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)
- [matplotlib.pyplot.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html)
- [matplotlib.pyplot.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html)
- [matplotlib.pyplot.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html)
- [matplotlib.pyplot.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)
- [matplotlib.pyplot.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)
- [matplotlib.pyplot.subplot2grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html)
- [matplotlib.pyplot.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html)
- [matplotlib.pyplot.xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xscale.html)
- [matplotlib.pyplot.yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html)
- [matplotlib.pyplot.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html)
- [matplotlib.pyplot.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html)
- [mplot3d tutorial](https://matplotlib.org/2.0.2/mpl_toolkits/mplot3d/tutorial.html)
- [additional tutorials](https://matplotlib.org/stable/tutorials/index.html)

**Extra**

- [Corey Shafer's Matplotlib Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_)
- [Diagrama de dispersión (spanish content)](https://www.youtube.com/watch?v=KwtuSe1JAVQ)
- [Coeficiente de corelación lineal (spanish content)](https://www.youtube.com/watch?v=aKsjilxc5ww)
- [¿Cómo trazar un diagrama de dispersión (spanish content)](https://www.youtube.com/watch?v=31OwPATTjrc)
- [El gráfico de líneas (spanish content)](https://www.youtube.com/watch?v=D70LOsWSsBs)
- [¿Qué son y cómo elaborar gráficos de barras? (spanish content)](https://www.youtube.com/watch?v=cPrq6wTFQbQ)
- [Histogramas - Ojiva y polígonos de frecuencia (spanish content)](https://www.youtube.com/watch?v=eY2xqiT_FF4)
- [Escala logarítmica (spanish content)](https://www.youtube.com/watch?v=DBz5dsoZm_w)
- [Stacked Bar Graph | Matplotlib](https://www.youtube.com/watch?v=fOJycZMxuoQ)
- [Developing Advanced Plots with Matplotlib : Plotting with 3D Axes](https://www.youtube.com/watch?v=wJQIGXSq504)

## Files

This project (lesson) is conceived to be carried out step by step, that is why the description of the files is presented as a statement.

### 0. Line Graph

**[0-line.py](0-line.py)**

Complete the following source code to plot `y` as a line graph:

- `y` should be plotted as a solid red line
- The x-axis should range from 0 to 10

```
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# your code here
```

![alt plot](./graphs/1.png)

### 1. Scatter

**[1-scatter.py](1-scatter.py)**

Complete the following source code to plot `x ↦ y` as a scatter plot:

- The x-axis should be labeled `Height (in)`
- The y-axis should be labeled `Weight (lbs)`
- The title should be `Men's Height vs Weight`
- The data should be plotted as magenta points

```
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

# your code here
```

![alt plot](./graphs/2.png)

### 2. Change of scale

**[2-change_scale.py](2-change_scale.py)**

Complete the following source code to plot `x ↦ y` as a line graph:

- The x-axis should be labeled `Time (years)`
- The y-axis should be labeled `Fraction Remaining`
- The title should be `Exponential Decay of C-14`
- The y-axis should be logarithmically scaled
- The x-axis should range from 0 to 28650

```
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# your code here
```

![alt plot](./graphs/3.png)

### 3. Two is better than one

**[3-two.py](3-two.py)**

Complete the following source code to plot `x ↦ y1` and `x ↦ y2` as line graphs:

- The x-axis should be labeled `Time (years)`
- The y-axis should be labeled `Fraction Remaining`
- The title should be `Exponential Decay of Radioactive Elements`
- The x-axis should range from 0 to 20,000
- The y-axis should range from 0 to 1
- `x ↦ y1` should be plotted with a dashed red line
- `x ↦ y2` should be plotted with a solid green line
- A legend labeling `x ↦ y1` as `C-14` and `x ↦ y2` as `Ra-226` should be placed in the upper right hand corner of the plot

```
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# your code here
```

![alt plot](./graphs/4.png)

### 4. Frequency

**[4-frequency.py](4-frequency.py)**

Complete the following source code to plot a histogram of student scores for a project:

- The x-axis should be labeled `Grades`
- The y-axis should be labeled `Number of Students`
- The x-axis should have bins every 10 units
- The title should be `Project A`
- The bars should be outlined in black

```
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# your code here
```

![alt plot](./graphs/5.png)

### 5. All in One

**[5-all_in_one.py](5-all_in_one.py)**

Complete the following source code to plot all 5 previous graphs in one figure:

- All axis labels and plot titles should have a font size of `x-small` (to fit nicely in one figure)
- The plots should make a 3 x 2 grid
- The last plot should take up two column widths (see below)
- The title of the figure should be `All in One`

```
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

# your code here
```

![alt plot](./graphs/6.png)

### 6. Stacking Bars

**[6-bars.py](6-bars.py)**

Complete the following source code to plot a stacked bar graph:

- `fruit` is a matrix representing the number of fruit various people possess
  - The columns of `fruit` represent the number of fruit `Farrah`, `Fred`, and `Felicia` have, respectively
  - The rows of `fruit` represent the number of `apples`, `bananas`, `oranges`, and `peaches`, respectively
- The bars should represent the number of fruit each person possesses:
  - The bars should be grouped by person, i.e, the horizontal axis should have one labeled tick per person
  - Each fruit should be represented by a specific color:
    - `apples` = red
    - `bananas` = yellow
    - `oranges` = orange (`#ff8000`)
    - `peaches` = peach (`#ffe5b4`)
    - A legend should be used to indicate which fruit is represented by each color
  - The bars should be stacked in the same order as the rows of `fruit`, from bottom to top
  - The bars should have a width of `0.5`
- The y-axis should be labeled `Quantity of Fruit`
- The y-axis should range from 0 to 80 with ticks every 10 units
- The title should be `Number of Fruit per Person`

```
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# your code here
```

![alt plot](./graphs/7.png)

### 7. Gradient

**[100-gradient.py](100-gradient.py)**

Complete the following source code to create a scatter plot of sampled elevations on a mountain:

- The x-axis should be labeled `x coordinate (m)`
- The y-axis should be labeled `y coordinate (m)`
- The title should be `Mountain Elevation`
- A colorbar should be used to display elevation
- The colorbar should be labeled `elevation (m)`

```
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

x = np.random.randn(2000) * 10
y = np.random.randn(2000) * 10
z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

# your code here8.png
```

![alt plot](./graphs/8.png)

### 8. PCA

**[101-pca.py](101-pca.py9.png)**

Principle Component Analysis (PCA) is a vital procedure used in data science for reducing the dimensionality of data (in turn, decreasing computation cost). It is also largely used for visualizing high dimensional data in 2 or 3 dimensions. For this task, you will be visualizing the [Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set) . You will need to download the file [pca.npz](https://holbertonintranet.s3.amazonaws.com/uploads/misc/2020/1/cdec57e313874348ba9a.npz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210721%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210721T014923Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=b1ed805647db921d6d98afbfc594cf87be88b96b936e466ca5a390b5f8b2573b) to test your code. You do not need to push this dataset to github. Complete the following source code to visualize the data in 3D:

```
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

# your code here
```

- The title of the plot should be `PCA of Iris Dataset`
- `data` is a `np.ndarray` of shape `(150, 4)`
  - `150` => the number of flowers
  - `4` => petal length, petal width, sepal length, sepal width
- `labels` is a `np.ndarray` of shape `(150,)` containing information about what species of iris each data point represents:
  - `0` => Iris Setosa
  - `1` => Iris Versicolor
  - `2` => Iris Virginica
- `pca_data` is a `np.ndarray` of shape `(150, 3)`
  - The columns of `pca_data` represent the 3 dimensions of the reduced data, i.e., x, y, and z, respectively
- The x, y, and z axes should be labeled `U1`, `U2`, and `U3`, respectively
- The data points should be colored based on their labels using the `plasma` color map

![alt plot](./graphs/9.png)
