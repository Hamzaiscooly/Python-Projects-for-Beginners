# bubble_sort.py
# Simple sorting algorithm that repeatedly swaps adjacent elements if they are in the wrong order

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # Swap
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("Sorted list:", numbers)
