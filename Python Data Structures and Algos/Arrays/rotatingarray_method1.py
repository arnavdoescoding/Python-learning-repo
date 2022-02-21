
# Creating a Temporary Array
import array
list1 = [ 31, 11, 56, 3, 7, 10]
new_array = array.array('i' , list1)


index_plus_one = int(input('Enter the number of elements to be rotated: '))
array2 = new_array[index_plus_one : ]
array1 = new_array[: index_plus_one ]
print(new_array)
print(array1)
print(array2)
array2.extend(array1)
new_array = array2

print(new_array)

