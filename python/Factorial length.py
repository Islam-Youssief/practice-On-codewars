#! /usr/bin/python

import math
def count(n):
	""" (int) -> int

    Count that takes an integer.

    Returns the number of digits in factorial(n)

    >>> count(5)
    3
    >>> count(50)
    65
    >>> count(500)
    1135
    """
        return int(math.ceil(math.log(2 * math.pi * n, 10) / 2 + n * math.log(n / math.e, 10)))



if __name__ == '__main__':
    import doctest
    doctest.testmod()