import re


def is_palindrome(a):
    """
        >>> is_palindrome("A man, a plan, a canal -- Panama")
        True
        >>> is_palindrome("Madam, I'm Adam!")
        True
        >>> is_palindrome(333)
        True
        >>> is_palindrome(None)
        False
        >>> is_palindrome("Abracadabra")
        False
    """
    a = re.sub(r'\W', '', str(a))
    a = a.replace(' ', '')
    a = a.lower()

    i = 0
    j = len(a) - 1
    while i < j:
        if a[i] != a[j]:
            return False
        i += 1
        j -= 1

    return True
