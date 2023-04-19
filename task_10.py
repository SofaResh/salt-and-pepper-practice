import re


def count_words(string):
    """
        >>> count_words("A man, a plan, a canal -- Panama")
        {'a': 3, 'man': 1, 'plan': 1, 'canal': 1, 'panama': 1}
        >>> count_words("Doo bee doo bee doo")
        {'doo': 3, 'bee': 2}
    """
    frequency = {}
    string = string.lower()
    string = re.findall(r'\b[a-z]{1,}\b', str(string))
    for word in string:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency
