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

'''
Q6: Find Path
    Write a function find_path that takes in a tree t with unique labels and a value x. It returns a list containing the labels of the nodes along the path from the root of t to the node labeled x.

    If x is not a label in t, return None. Assume that the labels of t are unique.

    For the following tree, find_path(t, 5) should return [2, 7, 6, 5].
'''
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        # In this way, we can go to the chilren first, and then decide if the parents will be added into the list
        path = find_path(b, x)  # if there's a "x" in the branch, it will return, but if there's not, it's not gonna return anything
        if path:
            return [label(t)] + path
        
'''
Q7: Sprout Leaves
    Define a function sprout_leaves that takes in a tree, t, and a list of leaf labels, leaves. It produces a new tree that is identical to t, but where each old leaf node has new branches, for each label in leaves.
'''
def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return tree(t, [tree(val) for val in leaves])
    return tree(label(t), [sprout_leaves(b, leaves) for b in branches(t)])

'''
Q8: Perfectly Balanced
    Part A: Implement sum_tree, which returns the sum of all the labels in tree t.
    Part B: Implement balanced, which returns whether every branch of t has the same total sum and that the branches themselves are also balanced.
    
    Hint: If we ever need to select a specific branch, we will need to break index into our branches list!

    Challenge: Solve both of these parts with just 1 line of code each.
'''
def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return label(t)
    return label(t) + sum(sum_tree(b) for b in branches(t))


def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    "*** YOUR CODE HERE ***"
    num = len(branches(t))
    sum_branch = 0
    
    for i in range(num):
        if sum_branch == 0:
            sum_branch = sum_tree(branches(t)[i])
        else:
            if sum_branch != sum_tree(branches(t)[i]):
                return False
        if not balanced(branches(t)[i]):
            return False
        
    return True
        