'''
Q1: Warm Up: Recursive Multiplication
These exercises are meant to help refresh your memory of the topics covered in lecture.

Write a function that takes two numbers m and n and returns their product. Assume m and n are positive integers. Use recursion, not mul or *.
'''
def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return m
    else:
        return multiply(m, n - 1) + m
    
'''
Q4: Is Prime

Write a function is_prime that takes a single argument n and returns True if n is a prime number and False otherwise. Assume n > 1. 

We implemented this in Discussion 1 iteratively, now time to do it recursively!
'''
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 2: return True
    
    def check_all(i):
        if i == 2:
            return True
        elif n % i == 0:
            return False
        else:
            return check_all(i - 1)
    return check_all(n - 1)
    
    
'''
Q5: Recursive Hailstone
Recall the hailstone function from Homework 1. First, pick a positive integer n as the start. 
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. Repeat this process until n is 1. 
Write a recursive version of hailstone that prints out the values of the sequence and returns the number of steps.
'''
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    steps = 1
    def transform(n, steps):
        print(n)
        if n == 1:
            return steps
        elif n % 2:
            return transform(3 * n + 1, steps + 1)
        else:
            return transform(n // 2, steps + 1)
    return transform(n, steps)
    # The method in solution can save more memory space. Try not write a separate function inside.
    
    
'''
Q6: Merge Numbers
Write a procedure merge(n1, n2), which takes numbers with digits in decreasing order and returns a single number with all of the digits of the two in decreasing order. 
Any number merged with 0 will be that number (treat 0 as having no digits). Use recursion.
'''
def merge(n1, n2):
    """Merges two numbers by digit in decreasing order.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    n1_last, n2_last = n1 % 10, n2 % 10
    n1_remain, n2_remain = n1 // 10, n2 // 10
    
    if n1_last == 0:
        return n2
    elif n2_last == 0:
        return n1
    elif n1_last <= n2_last:
        return n1_last + 10 * merge(n1_remain, n2)
    else:
        return n2_last + 10 * merge(n1, n2_remain)