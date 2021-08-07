# 0x01. Classification

## About

This is an educational project exploring concepts about **Probability** towards a formation in Machine Learning.

## Table of contents

- [Requirements](#requirements)
  - [Dependencies](#dependencies)
- [Topics](#topics)
- [Read or watch](#read-or-watch)
- [Files](#files)
  - [0. Initialize Poisson](#0-initialize-poisson)
  - [1. Poisson PMF](#1-poisson-pmf)
  - [2. Poisson CDF](#2-poisson-cdf)
  - [3. Initialize Exponential](#3-initialize-exponential)
  - [4. Exponential PDF](#4-exponential-pdf)
  - [5. Exponential CDF](#5-exponential-cdf)
  - [6. Initialize Normal](#6-initialize-normal)
  - [7. Normalize Normal](#7-normalize-normal)
  - [8. Normal PDF](#8-normal-pdf)
  - [9. Normal CDF](#9-normal-cdf)
  - [10. Initialize Binomial](#10-initialize-binomial)
  - [11. Binomial PMF](#11-binomial-pmf)
  - [12. Binomial CDF](#12-binomial-cdf)

## Requirements

- Python 3.6.14

### Dependencies

Please refer at the [requirements.txt](../../requirements.txt) file at the root of this repository.

## Topics

- What is probability?
- Basic probability notation
- What is independence? What is disjoint?
- What is a union? intersection?
- What are the general addition and multiplication rules?
- What is a probability distribution?
- What is a probability distribution function? probability mass function?
- What is a cumulative distribution function?
- What is a percentile?
- What is mean, standard deviation, and variance?
- Common probability distributions

## Read or watch

Before start please read or watch this concepts.

- [Probability](https://en.wikipedia.org/wiki/Probability)
- [Basic Concepts](https://onlinestatbook.com/2/probability/basic.html)
- [Intro to probability 1: Basic notation](https://www.youtube.com/watch?v=TkU3BvDAOtQ)
- [Intro to probability 2: Independent and disjoint](https://www.youtube.com/watch?v=GnWHt9nqwBA)
- [Intro to Probability 3: General Addition Rule; Union; OR](https://www.youtube.com/watch?v=TyAaVGR4MrA)
- [Intro to Probability 4: General multiplication rule; Intersection; AND](https://www.youtube.com/watch?v=wB-ZG9bgPXY)
- [Permutations and Combinations](https://onlinestatbook.com/2/probability/permutations.html)
- [Probability distribution](https://en.wikipedia.org/wiki/Probability_distribution)
- [Probability Theory](https://intranet.hbtn.io/rltoken/n9XfTIJ16hSMNpIdMS-WmA)
- [Cumulative Distribution Functions](https://www.oreilly.com/library/view/think-stats-2nd/9781491907344/ch04.html)
- [Common Probability Distributions: The Data Scientist’s Crib Sheet](https://medium.com/@srowen/common-probability-distributions-347e6b945ce4)
- [NORMAL MODEL PART 1 — EMPIRICAL RULE](https://www.youtube.com/watch?v=xgolpGrAZWo&list=PLFGZup_HuWTtIs0Xbzt7vDoFrnZxN4VXT&index=22)
- [Normal Distribution](https://www.mathsisfun.com/data/standard-normal-distribution.html)
- [Variance](https://en.wikipedia.org/wiki/Variance)
- [Variance (Concept)](https://www.youtube.com/watch?v=2eP14USYwtg)
- [Binomial Distribution](https://onlinestatbook.com/2/probability/binomial.html)
- [Poisson Distribution](https://onlinestatbook.com/2/probability/poisson.html)
- [Hypergeometric Distribution](https://onlinestatbook.com/2/probability/hypergeometric.html)

**As references**

- [numpy.random.poisson](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.poisson.html)
- [numpy.random.exponential](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.exponential.html)
- [numpy.random.normal](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.normal.html)
- [numpy.random.binomial](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.binomial.html)
- [erf](https://mathworld.wolfram.com/Erf.html)

**Extra**

_Matemóvil (youtube channel)_

- [Estadística | Introducción a la Estadística](https://www.youtube.com/watch?v=gl9EEbT7viM&list=PL3KGq8pH1bFTdYhAMbC0XHRpe_njRSctM) (spanish content)
- [Estadística | Variables estadísticas](https://www.youtube.com/watch?v=Tb3sgUSd2SQ&list=PL3KGq8pH1bFSLAzS3dccWo7Lgucaj09Km) (spanish content)
- [Estadística | Tabla de frecuencias](https://www.youtube.com/watch?v=iPEt789ewVM&list=PL3KGq8pH1bFSVLbLye45H3w1vzIQ0rDCi) (spanish content)
- [Estadística | Gráficas estadísticas](https://www.youtube.com/watch?v=L2F2VkzsZwU&list=PL3KGq8pH1bFRRxYgLYqS7_BIR2QyjdcPT) (spanish content)
- [Estadística | Media, Mediana y Moda](https://www.youtube.com/watch?v=jiceVfALmV0&list=PL3KGq8pH1bFQenma5Ofy1bmr0yJQlNZWX) (spanish content)
- [Estadística | Técnicas de conteo: principio de adición y multiplicación (suma y producto)](https://www.youtube.com/watch?v=BeA6saiK-_8&list=PL3KGq8pH1bFSVoVsMfKPenEiSKtfDNv4K) (spanish content)
- [Estadística | Análisis combinatorio: permutaciones y combinador](https://www.youtube.com/watch?v=QXO3u6Ak4rU&list=PL3KGq8pH1bFTkIi5Xbs9Ul9f05JZrxrzV) (spanish content)
- [Estadística | Variaciones, Combianciones y Permutaciones](https://www.youtube.com/watch?v=ynxsVxVZ9Vw&list=PL3KGq8pH1bFQ3tbm4wxhfZpUVtcPZXqG3) (spanish content)
- [Estadística | Distribución normal](https://www.youtube.com/watch?v=T7_ktqfVseU&list=PL3KGq8pH1bFQrSms9uTOpPk0euoHnx7mK) (spanish content)
- [Estadística | Probabilidades](https://www.youtube.com/watch?v=0lxZMaoeUno&list=PL3KGq8pH1bFQ5ZdTbz7DRXMDWv_wFvE1K) (spanish content)
- [Distribución de Poisson | Intro](https://www.youtube.com/watch?v=PMX75m4-s9A&pp=sAQA) (spanish content)
- [Distribución de Poisson | Ejercicio 1](https://www.youtube.com/watch?v=x9jF11I5x-g&pp=sAQA) (spanish content)
- [Distribución de Poisson | Ejercicio 2](https://www.youtube.com/watch?v=MbevsnWYb5o&pp=sAQA) (spanish content)
- [Distribución de Bernoulli | Intro](https://www.youtube.com/watch?v=olGbPzIGJ4M&t=219s) (spanish content)
- [Media (valor esperado) y varianza de una variable aleatoria de Bernoulli](https://www.youtube.com/watch?v=qWpV4TQRk9I) (spanish content)
- [Variables aleatorias discretas y continuas](https://www.youtube.com/watch?v=_wonmKS4Blk) (spanish content)
- [Función de distribución acumulativa de una variable aleatoria discreta](https://www.youtube.com/watch?v=OftL6S127wc) (spanish content)

_Matemáticas profe Alex (youtube channel)_

- [Estadística | Conceptos básicos](https://www.youtube.com/watch?v=Xq3thcQqwbc&list=PLeySRPnY35dFF5D9g_zi07yPKGXui4GII) (spanish content)
- [Estadística | Tabla de frecuencias](https://www.youtube.com/watch?v=a4cI02iW_zQ&list=PLeySRPnY35dFcEmQDGrPxwJVXiIeu_9cl) (spanish content)
- [Estadística | Media, mediana y moda](https://www.youtube.com/watch?v=fOuRqk1nzgY&list=PLeySRPnY35dFkzBgleLJ5WVFbGdkmCik5) (spanish content)
- [Estadística | Cuartiles, Deciles y Percentiles](https://www.youtube.com/watch?v=suSz9RXFNTs&list=PLeySRPnY35dG_Wo7ngNsT60lvahhW8UQy) (spanish content)
- [Estadística | Varianza y desviación](https://www.youtube.com/watch?v=hLmsEFNaOgY&list=PLeySRPnY35dE25b7mIEUlsMCQqlhJFhyG) (spanish content)
- [Estadística | Combianciones, Permutaciones y Variaciones](https://www.youtube.com/watch?v=ec8TQjfQrGY&list=PLeySRPnY35dFF_kWyWL893posL7DNlFHa) (spanish content)
- [Estadística | Probabilidad](https://www.youtube.com/watch?v=tQh29_Noo9w&list=PLeySRPnY35dEtzvR4hUhigwTCHQcxP28l) (spanish content)

_Other_

- [Distribuciones de Probabilidad (Discreta y Continua)](https://www.youtube.com/watch?v=NFfpUbGlm_c) (spanish content)
- [Distribucion Normal Estandarizada](https://www.youtube.com/watch?v=_gyrWRyh6Qg) (spanish content)
- [The Poisson Distribution and Poisson Process Explained](https://towardsdatascience.com/the-poisson-distribution-and-poisson-process-explained-4e2cb17d459)
- [Gallery of Distributions](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm)

## Files

This project (lesson) is conceived to be carried out step by step, that is why the description of the files is presented as a statement.

### Mathematical Approximations

For the following tasks, you will have to use various irrational numbers and functions. Since you are not able to import any libraries, please use the following approximations:

- π = 3.1415926536
- e = 2.7182818285
- ![alt erf](./images/erf.gif)

### 0. Initialize Poisson

**[poisson.py](poisson.py)**

Create a class `Poisson` that represents a poisson distribution:

- Class contructor `def __init__(self, data=None, lambtha=1.):`
  - `data` is a list of the data to be used to estimate the distribution
  - `lambtha` is the expected number of occurences in a given time frame
  - Sets the instance attribute lambtha
    - Saves `lambtha` as a float
  - If `data` is not given, (i.e. `None` (be careful: `not data` has not the same result as `data is None`)):
    - Use the given `lambtha`
    - If `lambtha` is not a positive value or equals to 0, raise a `ValueError` with the message `lambtha must be a positive value`
  - If `data` is given:
    - Calculate the `lambtha` of `data`
    - If `data` is not a `list`, raise a `TypeError` with the message `data must be a list`
    - If `data` does not contain at least two data points, raise a `ValueError` with the message `data must contain multiple values`

```
alexa@ubuntu-xenial:0x03-probability$ cat 0-main.py
#!/usr/bin/env python3

import numpy as np
Poisson = __import__('poisson').Poisson

np.random.seed(0)
data = np.random.poisson(5., 100).tolist()
p1 = Poisson(data)
print('Lambtha:', p1.lambtha)

p2 = Poisson(lambtha=5)
print('Lambtha:', p2.lambtha)
alexa@ubuntu-xenial:0x03-probability$ ./0-main.py
Lambtha: 4.84
Lambtha: 5.0
alexa@ubuntu-xenial:0x03-probability$
```
