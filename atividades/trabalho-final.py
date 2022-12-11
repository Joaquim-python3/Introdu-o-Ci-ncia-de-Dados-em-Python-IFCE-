import numpy as np
from sklearn.datasets import load_digits, load_diabetes
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import Perceptron, LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split

data = pd.read_csv('https://raw.githubusercontent.com/alissonSCA/dataset/master/dt_lin.csv')
x = data['x'].values
y = data['y'].values
dt2 = data.drop('Unnamed: 0', axis=1)
dt2.to_numpy()
xi = dt2['x'].values
yi = dt2['y'].values
lr = LinearRegression()
lr.fit(xi.reshape(-1, 1), yi)
y_pred = lr.predict(xi.reshape(-1,1))
np.sum(y_pred == y)
print(mean_squared_error(yi,y_pred, squared=False))
plt.scatter(xi,yi)
z = np.polyfit(xi, yi, 1)
p = np.poly1d(z)
plt.plot(xi,p(xi),"r--")
