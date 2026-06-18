def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Calculate the middle index
        mid = left + (right - left) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
            
        # If target is smaller, ignore right half
        else:
            right = mid - 1
            
    # Target was not present in the list
    return -1

# Example Usage:
numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_val = 23

result = binary_search_iterative(numbers, target_val)
print(f"Element found at index: {result}")  # Output: 5
