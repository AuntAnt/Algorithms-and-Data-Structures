def linear_search(lst, search_item):
    low = 0
    search_result = False

    while low < len(lst) and not search_result: #search_result is False:
        if lst[low] == search_item:
            search_result = True
        else:
            low += 1
    return search_result


lst = [45, 1, 76, 12, 86, 12, 9, 3, 145, 70, 42]
search_item = int(input("Enter item which you want find: "))
result = linear_search(lst, search_item)

if result:
    print("Item found")
else:
    print("Item not found")
