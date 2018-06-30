"""
# D. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
"""
import doctest


def both_ends(s):
    """
    >>> both_ends('a')
    ''
    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]


if __name__ == '__main__':
    doctest.testmod()
