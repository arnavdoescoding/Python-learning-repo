import numpy as np


def merge(inp_arr):
    size = len(inp_arr)
    if size > 1 :
        midpt = size // 2
        left_arr = inp_arr[: midpt]
        right_arr = inp_arr[midpt:]

        merge(left_arr)
        merge(right_arr)

        p = 0
        q = 0
        r = 0 

        left_size = len(left_arr)
        right_size = len(right_arr)

        while p < left_size and q < right_size:
            if left_arr[p] < right_arr[q]:
                inp_arr[r] = left_arr[p]
                p +=1
            else:
                inp_arr[r] = right_arr[q]
                q+=1

            r=+1

        while p < left_size:
            inp_arr[r] = left_arr[p]
            p+=1
            r+=1

        while q < right_size:
            inp_arr[r] = right_arr[q]
            q+=1
            r+=1



inp = [4, 1, 6 , 7 , 9, 11, 0, 13]

merge(inp)
print(inp)



