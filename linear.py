def linear_search(data_list, target):
    """
    Iterates through data_list to find the target.
    Returns the index if found, otherwise returns -1.
    """
    for index, element in enumerate(data_list):
        if element == target:
            return index  # Match found, return the index immediately
            
    return -1  # Loop finished without finding the target

# --- Example Usage ---
numbers = [4, 10, 5, 70, 23, 80]
target_value = 23

result = linear_search(numbers, target_value)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")



