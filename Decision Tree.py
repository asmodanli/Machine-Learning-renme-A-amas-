# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 22:35:33 2018

@author: Sena
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("D:\DATAI\ML\decision-tree-regression-dataset.csv", sep = ";", header = None)

x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)

#%%

from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor()

tree_reg.fit(x,y)

tree_reg.predict(6)
x_new = np.arange(min(x),max(x),0.01)
y_head = tree_reg.predict(x)
#%%%

plt.scatter(x,y,color = "red")

plt.plot(x_new,y_head, color = "green")

plt.xlabel("Tribün level")

plt.ylabel("Fiyat")


plt.show()























#%%
