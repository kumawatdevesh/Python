from numpy import *
from array import *

vals = array('i', [1, 3, 5, 2, 4])

for i in vals:
    print(i)


# user input

arr = array('i', [])

n = int(input('enter the length of array'))

for i in range(n):
    x = int(input('enter th enumber'))
    arr.append(x)

print(arr)

val = int(input('enter number to search'))

for e in arr:
    if (e==val):
        print('number is present')
        
        
print(arr.index(val))
print(max(arr))
print(concatenate([arr, vals]))
