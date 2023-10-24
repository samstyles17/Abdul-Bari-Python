original_list = [3, 2, 1, 10, 6, 3, 1]
k = 3

# Generate all subarrays of size k
subarrays = [original_list[i:i + k] for i in range(len(original_list) - k + 1)]

# Find subarray with least sum
min_sum_subarray = min(subarrays, key=lambda x: sum(x))

print("Subarray with least sum of elements:", min_sum_subarray)
