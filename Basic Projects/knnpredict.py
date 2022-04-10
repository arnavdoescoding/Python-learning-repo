import pip
import pandas as pd 
import matplotlib.pyplot as mp
import mglearn as mg 

X , y = mg.datasets.make_forge()
mg.discrete_scatter(X[:,0], X[: , 1], y)

