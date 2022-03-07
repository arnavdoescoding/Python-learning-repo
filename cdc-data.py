from hashlib import new
import math 
import numpy as np 
import pandas as pd
import openpyxl 
new_counter_underhs = 0
new_counter_hs = 0
new_counter_incoll = 0
new_counter_coll = 0
def proportion(filename):
    df = pd.read_csv(filename)

    new_df = df['EDUC1']

    for item in new_df.values:
        if item == 4:
            new_counter_coll = new_counter_coll + 1
        elif item == 3:
            new_counter_incoll = new_counter_incoll + 1
        elif item == 2:
            new_counter_hs = new_counter_hs + 1
        elif item == 1:
            new_counter_underhs = new_counter_underhs + 1

    total = new_counter_underhs + new_counter_hs + new_counter_incoll + new_counter_coll
    ncu = new_counter_underhs/total
    nch = new_counter_hs/total
    ncc = new_counter_incoll/total 
    ncac = new_counter_coll/total

    final_dict = {"less than high school": ncu , "high school": nch, "more than high school but not college": ncc, "college": ncac}

    return final_dict











