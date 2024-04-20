'''
Q1: Extending Rationals:
    Fill in the following code to implement the rational ADT from lecture.
'''
from math import gcd

def make_rat(num, den):
    """Creates a rational number, given a numerator and denominator.

    >>> a = make_rat(2, 4)
    >>> numer(a)
    1
    >>> denom(a)
    2
    """
    "*** YOUR CODE HERE ***"
    if den == 0: raise ValueError("Denominator cannot be zero!")
    
    g = gcd(num, den)
    if den < 0:
        den = -den
        num = -num
    
    return (num // g, den // g)

def numer(rat):
    """Extracts the numerator from a rational number."""
    "*** YOUR CODE HERE ***"
    return rat[0]

def denom(rat):
    """Extracts the denominator from a rational number."""
    "*** YOUR CODE HERE ***"
    return rat[1]

'''
Q2: Divide
    Next, we'll be implementing two additional functions to handle operations between rational numbers.
    First, implement div_rat(x,y), which returns the result of dividing rational number x by rational number y.
'''
def div_rat(x, y):
    """The quotient of rationals x/y.
    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = div_rat(a, b)
    >>> numer(c)
    9
    >>> denom(c)
    20
    """
    "*** YOUR CODE HERE ***"
    return make_rat(numer(x) * denom(y), denom(x) * numer(y))

'''
Q3: Less Than
    Finally, implement lt_rat(x, y), which returns True if and only if rational number x is less than rational number y.
'''
def lt_rat(x, y):
    """Returns True iff x < y as rational numbers; else False.
    >>> a, b = make_rat(6, 7), make_rat(12, 16)
    >>> lt_rat(a, b)
    False
    >>> lt_rat(b, a)
    True
    >>> lt_rat(a, b)
    False
    >>> a, b = make_rat(-6, 7), make_rat(-12, 16)
    >>> lt_rat(a, b)
    True
    >>> lt_rat(b, a)
    False
    >>> lt_rat(a, a)
    False
    """
    "*** YOUR CODE HERE ***"
    return  numer(x) * denom(y) < numer(y) * denom(y)

# Tree ADT Implementation
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the tree's list of branches is empty, and False otherwise."""
    return not branches(tree)

'''
Q5: Height
    Write a function that returns the height of a tree. Recall that the height of a tree is the number of non-root nodes in the longest path from the root to a leaf.
'''
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t): return 0
    
    return 1 + max(height(i) for i in branches(t))