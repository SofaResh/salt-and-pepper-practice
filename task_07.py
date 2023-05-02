def combine_anagrams(words_array):
    """
        >>> combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])
        [['cars', 'racs', 'scar'], ['for'], ['potatoes'], ['four'], ['creams', 'scream']]
    """
    sorted_words_array = [''.join(sorted(elem.lower())) for elem in words_array]

    result = {}

    for word, sorted_word in zip(words_array, sorted_words_array):
        if sorted_word in result:
            result[sorted_word].append(word)
        else:
            result[sorted_word] = [word]

    return list(result.values())
