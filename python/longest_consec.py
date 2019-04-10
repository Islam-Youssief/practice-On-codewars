#! /usr/bin/python
def longest_consec(s, k):
    """ (list,int) -> str

    Consecutive strings : follow one after another without an interruption.

    Return the first longest string consisting of k consecutive strings taken in the array

    >>> longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
    'abigailtheta'
    >>> longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)
    'oocccffuucccjjjkkkjyyyeehh'
    >>> longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0)
    ''
    """
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""
    return max(("".join(s[i:i+k]) for i in range(len(s)-k+1)), key=lambda x: len(x)) if s and k > 0 and k <= len(s) else ""

def longest_consec2(strarr, k):
    """ (list,int) -> str

    Consecutive strings : follow one after another without an interruption.

    Return the first longest string consisting of k consecutive strings taken in the array

    >>> longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
    'abigailtheta'
    >>> longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)
    'oocccffuucccjjjkkkjyyyeehh'
    >>> longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0)
    ''
    """
    if k <= 0 or k > len(strarr):
        return ''
        
    end_idx = len(strarr) - k + 1
    substrings = [''.join(strarr[i:i+k]) for i in range(0, end_idx)]
    return max(substrings, key=len) 


def longest_consec3(strarr, k):
    """ (list,int) -> str

    Consecutive strings : follow one after another without an interruption.

    Return the first longest string consisting of k consecutive strings taken in the array

    >>> longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
    'abigailtheta'
    >>> longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)
    'oocccffuucccjjjkkkjyyyeehh'
    >>> longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0)
    ''
    """
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ''

    longest = index = 0
    for i in range(n - k + 1):
        length = sum([len(s) for s in strarr[i: i + k]])
        if length > longest:
            longest = length
            index = i

    return ''.join(strarr[index: index + k])



def longest_consec4(strarr, k):
    """ (list,int) -> str

    Consecutive strings : follow one after another without an interruption.

    Return the first longest string consisting of k consecutive strings taken in the array

    >>> longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
    'abigailtheta'
    >>> longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)
    'oocccffuucccjjjkkkjyyyeehh'
    >>> longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0)
    ''
    """
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()