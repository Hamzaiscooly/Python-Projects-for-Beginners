# linear_search.py
# Search for a target item in a list using linear search

def linear_search(lst, target):
    for index, item in enumerate(lst):
        if item == target:
            return index  # Found the target, return its index
    return -1  # Not found

numbers = [4, 2, 7, 1, 9, 3]
target = 7
result = linear_search(numbers, target)

if result != -1:
    print(f"Found {target} at index {result}")
else:
    print(f"{target} not found in the list")
