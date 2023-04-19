def max_odd(lst):
    """
        >>> max_odd([1, 2, 3, 4, 4])
        3
        >>> max_odd([21.0, 2, 3, 4, 4])
        21
        >>> max_odd(['ololo', 2, 3, 4, [1, 2], None])
        3
        >>> max_odd(['ololo', 'fufufu'])

        >>> max_odd([2, 2, 4])

    """
    result = None
    for elem in lst:
        if isinstance(elem, (int, float)) and elem % 2 != 0:
            result = max(elem, result) if result is not None else int(elem)
    return result
