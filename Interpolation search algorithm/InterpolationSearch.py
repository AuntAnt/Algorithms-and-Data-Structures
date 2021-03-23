def interpolation_search(lst, search_item):
    low = 0
    high = len(lst) - 1
    search_result = False

    while (low <= high and search_item >= lst[low]) and search_item <= lst[high] and not search_result:
        middle = low + int(((high - low) / (lst[high] - lst[low])) * (search_item - lst[low]))
        guess = lst[middle]
        if guess == search_item:
            search_result = True
            # return search_result
        if guess < search_item:
            low = middle + 1
        else:
            high = middle - 1
    return search_result


lst = [45, 1, 76, 12, 86, 12, 9, 3, 145, 70, 42]
# lst = [3, 5, 11, 12, 15, 23, 25, 34, 67, 86]
search_item = int(input("Enter item which you want find: "))

result = interpolation_search(lst, search_item)

if result:
    print("Item found")
else:
    print("Item not found")
