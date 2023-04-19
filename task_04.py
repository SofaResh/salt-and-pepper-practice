def sort_list(lst):
    """
        >>> sort_list([])
        []
        >>> sort_list([2, 4, 6, 8])
        [8, 4, 6, 2, 2]
        >>> sort_list([1])
        [1, 1]
        >>> sort_list([1, 2, 1, 3])
        [3, 2, 3, 1, 1]
    """
    if len(lst) == 0:
        return []

    min_ind = []
    min_val = float('inf')
    max_ind = []
    max_val = float('-inf')

    for ind, elem in enumerate(lst):
        if elem < min_val:
            min_val = elem
            min_ind = [ind]
        elif elem == min_val:
            min_ind.append(ind)

        if elem > max_val:
            max_val = elem
            max_ind = [ind]
        elif elem == max_val:
            max_ind.append(ind)

    for ind in min_ind:
        lst[ind] = max_val

    for ind in max_ind:
        lst[ind] = min_val

    lst.append(min_val)

    return lst
