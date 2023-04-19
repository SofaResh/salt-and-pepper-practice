import re


def multiply_numbers(inputs=None):
    """
        >>> multiply_numbers()

        >>> multiply_numbers('ss')

        >>> multiply_numbers('1234')
        24
        >>> multiply_numbers('sssdd34')
        12
        >>> multiply_numbers(2.3)
        6
        >>> multiply_numbers([5, 6, 4])
        120
    """
    result = None
    nums = re.findall(r'\d+', str(inputs))
    nums = re.split(r'', str(nums))
    for i in nums:
        if '0' <= i <= '9':
            if result == None:
                result = int(i)
            else:
                result *= int(i)

    return result
