# Binary Search Python Project
# In this Kylie Ying tutorial, 
# you will learn how to implement the divide and conquer 
# algorithm called binary search. This is a common searching algorithm 
# which comes up in job interviews, which is why it is important to know 
# how to implement it in code.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if arr[mid] == target:
            return f"Element found at index {mid}"
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    
    return "Element not found"

# Example Usage:
sorted_list = [1, 3, 5, 7, 9, 11, 15, 18, 20]
target_value = 7
print(binary_search(sorted_list, target_value))
