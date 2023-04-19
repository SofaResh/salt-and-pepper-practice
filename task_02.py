def coincidence(lst=None, rng=None):
    """
        >>> coincidence([1, 2, 3, 4, 5], range(3, 6))
        [3, 4, 5]
        >>> coincidence()
        []
        >>> coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))
        [1, 2, 2.5]
    """
    if lst is None or rng is None:
        return []

    return [elem for elem in lst if type(elem) in (int, float) and (rng.start <= elem < rng.stop)]
