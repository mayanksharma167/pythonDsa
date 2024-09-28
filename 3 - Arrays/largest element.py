"""
LARGEST IN ARRAY
"""
from array import array

arr = [90, 97, 17, 45, 91, 51, 65, 88, 36, 45, 48, 8, 72, 65, 62, 84, 97, 60, 69]

def largest(array):
    large = array[0]
    for i in range(len(array)):
        if array[i] > large:
            large = array[i]
    return large

def smallest(array):
    small = array[0]
    for i in range(len(array)):
        if array[i] < small:
            small = array[i]
    return small

print(largest(arr))
print(smallest(arr))