
def binary_search(arr, key):
    low = 0
    high = len(arr)-1
    ## mid ko while ke andar defiine kro because it changes with every iteration.
    while low<=high:
        mid = (high+low)//2

        # if mid becomes target
        if arr[mid] == key:
            return mid
        # if mid<key , means the key lies on the right side.
        elif arr[mid] < key:
            low = mid+1
        #if mid>key, means the key lies on the left half.
        else:
            high = mid-1
    return -1



# Example usage
arr = [3, 10, 19, 23, 29, 35, 41, 50, 62, 77]
target = 19


result = binary_search(arr, target)
print(f"{target} is present at index {result}.")
