def subarrays(arr):
    n = len(arr)
    result = []
    
    # Loop for each starting point
    for i in range(n):
        # Loop for each ending point
        for j in range(i, n):
            # Append the subarray arr[i:j+1] to the result
            result.append(arr[i:j+1])
    return result

# Example usage
arr = [1, 2, 3, 4]
result = subarrays(arr)

print(result)