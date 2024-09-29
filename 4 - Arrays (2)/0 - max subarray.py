# Example usage
array = [1, -2, 3, -4]

def sub_arrays(arr):
    result = []
    max_sub = float('-inf')
    for i in range(0,len(arr)):
        for j in range(i, len(arr)):
            subarray = arr[i:j+1]
            sum_sub = sum(subarray)
            print(f"subarray: {subarray}: Sum => {sum_sub}")

            if sum_sub>max_sub:
                max_sub = sum_sub
    return max_sub

print("\nMax sub array sum is: ",sub_arrays(array))
