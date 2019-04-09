#! /usr/bin/python

# using list comprehension
def find_it(seq):
    """ (list) -> int

    Given an array of numbers.

    Return int that appears an odd number of times.

    >>> find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
    5
    >>> find_it([2,2,3,4,5,6,7,7,6,7,7,6,7])
    3
    >>> find_it([1,2,1,2,3,3,2,3,4,5,1,2,4,5])
    1
    """
    return [i for i in seq if seq.count(i)%2!=0][0] 
    return [x for x in seq if seq.count(x) % 2][0]

# using usual for
def find_it(seq):
    """ (list) -> int

    Given an array of numbers.

    Return int that appears an odd number of times.

    >>> find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
    5
    >>> find_it([2,2,3,4,5,6,7,7,6,7,7,6,7])
    3
    >>> find_it([1,2,1,2,3,3,2,3,4,5,1,2,4,5])
    1
    """
    for i in seq:
        if seq.count(i)%2!=0:
            return i


# using collections
import collections

def find_it(seq):
    """ (list) -> int

    Given an array of numbers.

    Return int that appears an odd number of times.

    >>> find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
    5
    >>> find_it([2,2,3,4,5,6,7,7,6,7,7,6,7])
    3
    >>> find_it([1,2,1,2,3,3,2,3,4,5,1,2,4,5])
    1
    """
    if len( seq ) == 0:
        return None
    seqCounter = collections.Counter(seq)
    for i in seqCounter:
        if seqCounter[i] % 2 == 1:
            return i

# using collection as a dictionary values
from collections import Counter
def find_it(l):
    """ (list) -> int

    Given an array of numbers.

    Return int that appears an odd number of times.

    >>> find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
    5
    >>> find_it([2,2,3,4,5,6,7,7,6,7,7,6,7])
    3
    >>> find_it([1,2,1,2,3,3,2,3,4,5,1,2,4,5])
    1
    """
    return [k for k, v in Counter(l).items() if v % 2 != 0][0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()