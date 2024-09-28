"""
Linear search algorithm
"""
import random
key = 36

arr = [35, 5, 58, 5, 36, 68, 95, 82, 9, 88]

for i in range(len(arr)):
    if arr[i] == key:
        print(f"Element found at {i}")