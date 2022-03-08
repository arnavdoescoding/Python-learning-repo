import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt


dataset = pd.read_csv('wrestling_data.csv')
world_champions = dataset[: 141]
world_champions.to_excel('rasslin.xlsx')
names = world_champions[['name', 'reign' , 'days']]
rank = names.sort_values('days' , ascending=False)
rank_non_repetitive = rank.drop_duplicates('days')

name_series = rank_non_repetitive['name']
reign_series = rank_non_repetitive['reign']
days_series = rank_non_repetitive['days']
name_list = name_series.values
reign_list = reign_series.values
day_list = days_series.values

plt.plot(day_list ,reign_list)
plt.title('WWF WORLD HEAVYWEIGHT CHAMPIONS')
plt.ylabel('Reign Number')
plt.xlabel('No. Of Days')
plt.tight_layout()
plt.show()