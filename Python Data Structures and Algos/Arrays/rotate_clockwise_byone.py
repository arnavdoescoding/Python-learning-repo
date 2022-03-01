import array
sample_array = array.array('i' , [1 , 2 , 3, 4 , 5 , 6 ,7])


def rotate_clockwise_by_one(arr):
    n = len(arr)
    arr1 = arr[: n]
    arr2 = arr[n : ]
    arr1.reverse()
    arr2.reverse()
    arr1.extend(arr2)
    arr1.reverse()
    print(arr1)


print(sample_array)
rotate_clockwise_by_one(sample_array)