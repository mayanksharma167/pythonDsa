array = [2,5,7,3,6,9,1,7]

def reverse(arr):
    first, last = 0, len(arr)-1
    while first<last:
        temp = arr[last]
        arr[last] = arr[first]
        arr[first] = temp
        
        first += 1
        last -= 1

    return arr

print(reverse(array))