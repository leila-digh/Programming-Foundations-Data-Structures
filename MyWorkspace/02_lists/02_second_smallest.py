def find_second_smallest(lst):
    # Bubble Sort, Compare adjacent elements & swap
    # print(lst)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if (lst[j] < lst[i]):
                temp = lst[j]
                lst[j] = lst[i]
                lst[i] = temp
    return lst[1]