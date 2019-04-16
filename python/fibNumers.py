#! /usr/bin/python

"""
The Fibonacci numbers are the numbers in the following integer sequence (Fn):
> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as
> F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
> F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:
```
[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
```

depending on the language if F(n) * F(n+1) = prod.
If you don't find two consecutive F(m) verifying `F(m) * F(m+1) = prod` you will return
```
[F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
```

F(m) being the smallest one such as F(m) * F(m+1) > prod.

## Examples
```
productFib(714) # should return [21, 34, true],
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return [34, 55, false],
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
```
"""
def productFib(prod):
    """ (int) -> list

    Takes a number say n then searching two Fibonacci numbers F(n) and F(n+1)
    verifying > F(n) * F(n+1) = prod.

    Returns an array represents the result as descriped on the problem.

    >>> productFib(4895)
    [55, 89, True]
    >>> productFib(5895)
    [89, 144, False]
    """
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]

def productFib2(prod):
    """ (int) -> list

    Takes a number say n then searching two Fibonacci numbers F(n) and F(n+1)
    verifying > F(n) * F(n+1) = prod.

    Returns an array represents the result as descriped on the problem.

    >>> productFib2(4895)
    [55, 89, True]
    >>> productFib2(5895)
    [89, 144, False]
    """
    func = lambda a, b: func(b, a+b) if a*b < prod else [a, b, a*b == prod]
    return func(0, 1)

def productFib3(prod, f1=0, f2=1):
    """ (int) -> list

    Takes a number say n then searching two Fibonacci numbers F(n) and F(n+1)
    verifying > F(n) * F(n+1) = prod.

    Returns an array represents the result as descriped on the problem.

    >>> productFib3(4895)
    [55, 89, True]
    >>> productFib3(5895)
    [89, 144, False]
    """
    return [f1, f2, True] if prod == f1 * f2 else [f1, f2, False] if prod < f1 * f2 else productFib3(prod, f2, f1+f2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
