# Task:
# --> You are given a space-separated list of numbers. Your task is to print a reversed NumPy array with the element type float.
# -> Input Format: A single line of input containing space-separated numbers.
# -> Sample Input: 1 2 3 4 -8 -10
# -> Sample Output: [-10.  -8.   4.   3.   2.   1.]


import numpy

def arrays(arr):
    arr=numpy.array(arr)
    arr=arr.astype(float)
    result=arr[::-1]
    return result
    
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
