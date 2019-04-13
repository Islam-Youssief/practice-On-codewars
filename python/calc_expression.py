#! /usr/bin/python
"""
Your job is to create a calculator which evaluates expressions in Reverse Polish notation.
For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.
For your convenience, the input is formatted such that a space is provided between every token.
Empty expression should evaluate to 0.
Valid operations are +, -, *, /.
You may assume that there won't be exceptional situations (like stack underflow or division by zero).
more info : https://en.wikipedia.org/wiki/Reverse_Polish_notation
"""

import operator
ops = {
  "+": (lambda a, b: a + b),"-": (lambda a, b: a - b),
  "*": (lambda a, b: a * b),"/": (lambda a, b: a / b)
}

def calc(expr):

    """ (str) -> int

    Evaluates expressions in Reverse Polish notation.

    Returns a number as the evaluation result.

    >>> calc("3")
    3.0
    >>> calc("1 3 +")
    4.0
    >>> calc("1 3 -")
    -2.0
    >>> calc("4 2 /")
    2.0
    """
    stack = []
    [stack.append(eval("{1}{2}{0}".format(stack.pop(), stack.pop(), e)) if e in ('+', '-', '/', '*') else e) for e in expr.split()]
    return float(stack.pop()) if stack else 0

def calc2(expression):
    """ (str) -> int

    Evaluates expressions in Reverse Polish notation.

    Returns a number as the evaluation result.

    >>> calc2("3")
    3.0
    >>> calc2("1 3 +")
    4.0
    >>> calc2("1 3 -")
    -2.0
    >>> calc2("4 2 /")
    2.0
    """
    if not(expression):
        return 0 
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token in ops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = ops[token](arg1, arg2)
            stack.append(result)
        else:
            stack.append(float(token))
    return stack.pop()

def calc3(expr):
    """ (str) -> int

    Evaluates expressions in Reverse Polish notation.

    Returns a number as the evaluation result.

    >>> calc3("3")
    3.0
    >>> calc3("1 3 +")
    4.0
    >>> calc3("1 3 -")
    -2.0
    >>> calc3("4 2 /")
    2.0
    """
    stack = [0]
    for token in expr.split(" "):
        if token in ops:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(ops[token](op1,op2))
        elif token:
            stack.append(float(token))
    return stack.pop()

def calc4(expr):
    """ (str) -> int

    Evaluates expressions in Reverse Polish notation.

    Returns a number as the evaluation result.

    >>> calc4("3")
    3.0
    >>> calc4("1 3 +")
    4.0
    >>> calc4("1 3 -")
    -2.0
    >>> calc4("4 2 /")
    2.0
    """
    OPS = {'+': lambda x, y: y + x, '-': lambda x, y: y - x, '*': lambda x, y: y * x, '/': lambda x, y: y / x}
    if not expr:
        return 0
    stack = []
    [stack.append(*map(OPS[sign], [stack.pop()], [stack.pop()])) if sign in OPS else stack.append(float(sign)) for sign in expr.split(' ')]
    return stack[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
