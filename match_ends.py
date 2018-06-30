"""
# C. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
"""

import doctest


def match_ends(x):
    """
    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    return sum(1 for s in x if len(s) >= 2 and s[0] == s[-1])


if __name__ == '__main___':
    doctest.testmod()
