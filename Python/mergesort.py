def merge_sort(arr):
    """
    Implementation of the merge sort algorithm.
    This is a divide and conquer algorithm that:
    1. Divides input array into two halves
    2. Recursively sorts the two halves
    3. Merges the sorted halves

    Args:
        arr (list): List of comparable elements to be sorted

    Returns:
        list: A new sorted list containing the same elements
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # Base case: arrays of length 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr.copy()
    
    # Divide array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.
    
    Args:
        left (list): First sorted array
        right (list): Second sorted array
    
    Returns:
        list: Merged sorted array
    """
    result = []
    i = j = 0
    
    # Compare elements from both arrays and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left array, if any
    result.extend(left[i:])
    
    # Add remaining elements from right array, if any
    result.extend(right[j:])
    
    return result

# Test the implementation
if __name__ == "__main__":
    # Test case 1: Random array
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_arr)
    sorted_arr = merge_sort(test_arr)
    print("Sorted array:", sorted_arr)
    
    # Test case 2: Already sorted array
    test_arr = [1, 2, 3, 4, 5]
    print("\nOriginal array:", test_arr)
    sorted_arr = merge_sort(test_arr)
    print("Sorted array:", sorted_arr)
    
    # Test case 3: Array in reverse order
    test_arr = [5, 4, 3, 2, 1]
    print("\nOriginal array:", test_arr)
    sorted_arr = merge_sort(test_arr)
    print("Sorted array:", sorted_arr)
