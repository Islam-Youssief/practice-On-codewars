#! /usr/bin/python
# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

# using set method
def is_pangram(s):
	""" (str) -> True/False

    Sentence that contains every single letter of the alphabet at least once.

    Return True if it is pangram, False if not.

    >>> is_pangram("Islam Youssief")
    False
    >>> is_pangram("ISLAM-YOUSSIEF")
    False
    >>> is_pangram("The quick, brown fox jumps over the lazy dog!")
    True
    """
    	return  not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())
    	return True if set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower())) else False
    	return len([l for l in list('abcdefghijklmnopqrstuvwxyz') if l in s.lower()]) == 26

# using string module
import string
def is_pangram2(s):
	""" (str) -> True/False

    Sentence that contains every single letter of the alphabet at least once.

    Return True if it is pangram, False if not.

    >>> is_pangram2("Islam Youssief")
    False
    >>> is_pangram2("ISLAM-YOUSSIEF")
    False
    >>> is_pangram2("The quick, brown fox jumps over the lazy dog!")
    True
    """
    	s = s.lower()
    	return all(letter in s for letter in string.lowercase)
    	return set(string.ascii_lowercase).issubset(s.lower())
    	return set(string.lowercase) & set(s.lower()) == set(string.lowercase)
    	return all(ch in s.lower() for ch in string.lowercase)

# using re module
import re
def is_pangram3(s):
	""" (str) -> True/False

    Sentence that contains every single letter of the alphabet at least once.

    Return True if it is pangram, False if not.

    >>> is_pangram3("Islam Youssief")
    False
    >>> is_pangram3("ISLAM-YOUSSIEF")
    False
    >>> is_pangram3("The quick, brown fox jumps over the lazy dog!")
    True
    """
    	return len(set(re.sub( '[^a-z]', '', s.lower() ))) == 26

# Testing ..
# pangram = "The quick, brown fox jumps over the lazy dog!"
# assert is_pangram(pangram) == True

if __name__ == '__main__':
    import doctest
    doctest.testmod()