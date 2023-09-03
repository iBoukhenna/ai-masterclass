# -*- coding: utf-8 -*-
"""Seaborn Tutorial in Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aytx8nzunPi7CjF_7RaCEZsmtPZ8GLxY

#Seaborn
*   Data Visualization Library

#Importing the Libraries
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""#Note : Seaborn has some built-in datasets"""

# total bill vs tip dataset
tips = sns.load_dataset('tips')

tips.head()

# setting a theme for the plots
sns.set_theme()

# visualize the data
sns.relplot(data=tips, x = 'total_bill', y = 'tip', col = 'time', hue='smoker', style='smoker', size='size')

# load the iris dataset
iris = sns.load_dataset('iris')

iris.head()

sns.scatterplot(x='sepal_length', y='petal_length', hue='species',data=iris)

sns.scatterplot(x='sepal_length', y='petal_width', hue='species',data=iris)

# loading the titanic dataset
titanic = sns.load_dataset('titanic')

titanic.head()

titanic.shape

"""#Count Plot"""

sns.countplot(x='class', data=titanic)

sns.countplot(x='survived', data=titanic)

"""#Bar Chart"""

sns.barplot(x='sex', y='survived', hue='class', data=titanic)

# house price dataset
from sklearn.datasets import fetch_california_housing
house_california = fetch_california_housing()
house = pd.DataFrame(house_california.data, columns=house_california.feature_names)
house['PRICE'] = house_california.target

print(house)

house.head()

"""#Distribution Plot"""

sns.distplot(house['PRICE'])

"""#Correlation

1.   Positive Correlation
2.   Negative Correlation

#Heat Map
"""

correlation = house.corr()

# constructing a Heat Map
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')