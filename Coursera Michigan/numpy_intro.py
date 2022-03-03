import math
from this import d
import numpy as np # Stored as a list of lists

#creating arrays

a = np.array([[1 ,2 , 3], [1 ,2, 3]])
print(a)   # Prints array

print(a.ndim)    # Prints the dimensions in array, like a matrix

print(a.shape)  # Prints a tuple in the form of (rows,coloumns)

# numpy also accepts floats, in a mix of floats and integers, it'll convert everything to a suitable form

np_type = a.dtype

# Returns a numpy array of ones and zeros

a = np.ones((3 , 3))
a = np.zeros((3 , 3))

# Random int and rand
b = np.random.randint((2 ,3))

# creating a squence of numbers. First number inclusive, second is exclusive
d = np.arange(10 , 100 , 10)

#For floats , we use linspace function. here, last argument represents number of terms, both inclusive

e = np.linspace(0 , 1 , 10)
print(e)