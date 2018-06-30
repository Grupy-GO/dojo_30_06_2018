"""
# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
"""
import doctest


def front_x(words):
    """
    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """

    return list(sorted(words, key=lambda s: '0' + s if s.startswith('x') else s))
    #
    # x_words = [w for w in words if w.startswith('x')]
    # o_words = [w for w in words if not w.startswith('x')]
    # return list(sorted(x_words)) + list(sorted(o_words))


if __name__ == '__main__':
    doctest.testmod()
