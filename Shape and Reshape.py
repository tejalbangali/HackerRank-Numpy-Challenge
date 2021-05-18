# --> You are given a space-separated list of nine integers. Your task is to convert this list into an X NumPy array.
# -> Input Format: A single line of input containing space-separated integers.

# -> Sample Input: 1 2 3 4 5 6 7 8 9
# -> Sample Output: [[1 2 3]
#  [4 5 6]
#  [7 8 9]]


import numpy as np

arr=input().strip().split(' ')


arr= np.array(arr)
arr=arr.astype(int)
arr=np.reshape(arr,(3,3))
print(arr)
