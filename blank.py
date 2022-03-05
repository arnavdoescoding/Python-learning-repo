from operator import index
import numpy as np
import math
import pandas as pd

age_data = [ 20 , 51 , 49]
name_data = ['Arnav', 'Baba', 'Mom']
s = pd.Series(age_data , index= name_data)
print(s)