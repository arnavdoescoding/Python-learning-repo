import array
a = [ 1 , 2 , 3 , 4 , 5 , 6 , 7]
d = 2
sample_array = array.array('i' , a)
print(sample_array)
array1 = sample_array[: d]
array2 = sample_array[d: ]
array1.reverse()
array2.reverse()
array1.extend(array2)
array1.reverse()
sample_array = array1
print(sample_array)