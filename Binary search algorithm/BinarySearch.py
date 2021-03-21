def binary_search(lst, search_item):
    low = 0
    high = len(lst) - 1
    search_result = False

    while low <= high and not search_result:
        middle = (low + high) // 2
        guess = lst[middle]
        if guess == search_item:
            search_result = True
            return search_result
        if middle > search_result:
            high = middle - 1
        else:
            low = middle + 1
    return search_result


lst = [45, 1, 76, 12, 86, 12, 9, 3, 145, 70, 42]
search_item = int(input("Enter item which you want find: "))

result = binary_search(lst, search_item)

if result:
    print("Item found")
else:
    print("Item not found")
