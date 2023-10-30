"""
Q5: Make Keeper

Implement make_keeper, which takes a positive integer n and returns a function f that takes as its argument another one-argument 
function cond. When f is called on cond, it prints out the integers from 1 to n (including n) for which cond returns a true 
value when called on each of those integers. Each integer is printed on a separate line.
"""
def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"
    def f(cond):
        for i in range(1, n + 1):
            if cond(i): print(i)
    return f

"""
Q6: Currying

Write a function curry that will curry any two argument function.
"""
def curry(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = curry(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = curry(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> curry(mod)(123)(10)
    3
    """
    "*** YOUR CODE HERE ***"
    def f(x):
        def g(y):
            return func(x, y)
        return g
    return f

"""
Q7: Make Your Own Lambdas

For the following problem, first read the doctests for functions f1, f2, f3, and f4. Then, implement the functions to conform 
to the doctests without causing any errors. Be sure to use lambdas in your function definition instead of nested def statements. 
Each function should have a one line solution.
"""
def f1():
    """
    >>> f1()
    3
    """
    "*** YOUR CODE HERE ***"
    return 3

def f2():
    """
    >>> f2()()
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda : 3

def f3():
    """
    >>> f3()(3)
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda x: x

def f4():
    """
    >>> f4()()(3)()
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda : lambda x: lambda : x