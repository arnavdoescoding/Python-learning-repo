import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl


df = pd.read_csv('FuelConsumption.csv')  #Reads the dataset
df.head()

df.describe()  #Summarizes the data

cdf = df['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']
cdf.head()

viz = cdf['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB']
viz.hist()
plt.show()