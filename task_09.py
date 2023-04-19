def connect_dicts(dict1, dict2):
    """
        >>> connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5})
        {'c': 11, 'b': 12}
        >>> connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15})
        {'d': 11, 'c': 12, 'a': 13}
        >>> connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15})
        {'c': 11, 'b': 12, 'a': 15}
    """
    new_dict = {}
    sum1 = 0
    sum2 = 0
    for value1 in dict1.values():
        sum1 = sum1 + value1
    for value2 in dict2.values():
        sum2 = sum2 + value2

    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            if value1 > 10 and value2 > 10:
                if key1 == key2 and sum1 == sum2:
                    new_dict[key2] = value2
                elif key1 == key2 and sum1 > sum2:
                    new_dict[key1] = value1
                elif key1 == key2 and sum1 < sum2:
                    new_dict[key2] = value2
                elif key1 not in new_dict:
                    new_dict[key1] = value1
                    new_dict[key2] = value2
    return dict(sorted(new_dict.items(), reverse=True))
