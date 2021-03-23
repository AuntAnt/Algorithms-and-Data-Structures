def bubble_sort(lst):
    for num in range(len(lst) - 1, 0, -1):
        for i in range(num):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


lst = [45, 1, 76, 0, 86, 12, 9, 3, 145, 70, 42]
print("Original: ", lst)

result = bubble_sort(lst)
print("Sorted: ", result)
