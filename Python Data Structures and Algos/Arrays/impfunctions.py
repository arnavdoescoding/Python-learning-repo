import array as myarray  
new_array = myarray.array('i', [1 , 3 , 5 , 7])

def printing_an_array(array1) :
    for i in range(0 , (len(array1))):
        print(array1[i], end= " ")

# 1.append function
new_array.append(4)
printing_an_array(new_array)

# 2.insert function 
new_array.insert(2, 10)
printing_an_array(new_array)

# 3.pop function 
print(new_array.pop(0))
printing_an_array(new_array)

# 4.index function  returns the index 
printing_an_array(new_array)
print(new_array.index(5))

# 5.reverse function 
new_array.reverse()
printing_an_array(new_array)

# 6.typecode function 
print(new_array.typecode)

# 7.itemsize function 
print(new_array.itemsize)

# 8.buffer_info function 
print(new_array.buffer_info())

# 9.count function 
print(new_array.count(5))
new_array.append(5)
new_array.append(5)
print(new_array.count(5))

# 10. extend(arr) function 
new_array2 = myarray.array('i', [11 , 12 , 13 , 14])
new_array.extend(new_array2)
printing_an_array(new_array)

# 11. fromlist functions 
list2 = [12 , 14 , 15]
new_array.fromlist(list2)
printing_an_array(new_array)

#12. tolist function 
print(new_array.tolist())







