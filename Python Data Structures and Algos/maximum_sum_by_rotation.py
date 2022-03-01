import array
from random import sample

sample_array = array.array('i', [4 , 5, 1, 2, 3])

n = len(sample_array)
sample_sum = 0 
count = 0
max = 0
sumarray = 0

for i in sample_array:
    sample_sum = sample_sum + count*i
    count = count + 1
    sumarray = sumarray + i

for x in range(1 , n):
    sample_sum = sample_sum + (sumarray - n*sample_array[n-x])
    if sample_sum >= max:
        max = sample_sum

print(max)
    