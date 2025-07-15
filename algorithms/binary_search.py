# binary_search.py
# Efficient search in a sorted list using binary search

def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found

sorted_numbers = [1, 3, 5, 7, 9, 11]
target = 5
result = binary_search(sorted_numbers, target)

if result != -1:
    print(f"Found {target} at index {result}")
else:
    print(f"{target} not found in the list")
