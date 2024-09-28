array = [2,5,7,3,6,9,1,7]

def pairs(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            print(f"({arr[i]},{arr[j]})", end=" ")
        print()

pairs(array)