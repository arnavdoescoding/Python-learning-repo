import math 
import numpy as np 
import pandas as pd
import openpyxl 

df = pd.read_excel('IA MARKS.xlsx')
new_df = df.rename(columns={'Model.1':'Technical Make'})
new_df.columns = [x.lower().strip() for x in new_df.columns]
print(new_df)


