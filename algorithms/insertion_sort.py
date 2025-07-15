# insertion_sort.py
# Builds the sorted list one item at a time by inserting elements at their correct position

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key

numbers = [12, 11, 13, 5, 6]
insertion_sort(numbers)
print("Sorted list:", numbers)
