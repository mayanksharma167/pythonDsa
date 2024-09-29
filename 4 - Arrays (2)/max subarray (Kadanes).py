def max_subarray_sum(arr):
    max_sum = float('-inf')  # Initialize to the smallest possible value
    current_sum = 0  # This will store the sum of the current subarray

    for num in arr:
        current_sum = current_sum+num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum


# Example usage
array = [-2, -3, 4, -1, -2, 1, 5, -3]
result = max_subarray_sum(array)
print(f"Maximum subarray sum: {result}")
