'''
Q1: Count Stair Ways
Imagine that you want to go up a flight of stairs that has n steps, where n is a positive integer. You can take either one or two steps each time you move. In how many ways can you go up the entire flight of stairs?

You'll write a function count_stair_ways to answer this question. Before you write any code, consider:

- How many ways are there to go up a flight of stairs with n = 1 step? What about n = 2 steps? Try writing or drawing out some other examples and see if you notice any patterns.
- What is the base case for this question? What is the smallest input?
- What do count_stair_ways(n - 1) and count_stair_ways(n - 2) represent?
'''
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either one step or two steps at a time.
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)
    
'''
Q2: Count K
Consider a special version of the count_stair_ways problem where we can take up to k steps at a time. Write a function count_k that calculates the number of ways to go up an n-step staircase. Assume n and k are positive integers.

!!! The difference between counting partitions and this problem is, counting partitions doesn't care about sequence, but this one does.

Backgroun of Counting Partitions:
The number of partitions of a positive integer n, using parts up to size m, is the number of ways in whic n can be expressed as the sum of positive integer parts up to m in increasing order.
'''
def count_k(n, k):
    """Counts the number of paths up a flight of n stairs
    when taking up to k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    # 用走完的角度去理解：n==0的时候是走完楼梯的时候，n==1也确实可以return 1但是没有必要，因为之后还会recursive到n==0的情况
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        for i in range(1, k+1):
            total += count_k(n-i, k)
        return total

'''
Q3: Insect Combinatorics
An insect is inside an m by n grid. The insect starts at the bottom-left corner (1, 1) and wants to end up at the top-right corner (m, n). The insect can only move up or to the right. Write a function paths that takes the height and width of a grid and returns the number of paths the insect can take from the start to the end. (There is a closed-form solution to this problem, but try to answer it with recursion.)

In the 2 by 2 grid, the insect has two paths from the start to the end. In the 3 by 3 grid, the insect has six paths

Hint: What happens if the insect hits the upper or rightmost edge of the grid?
'''
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    # 我的思路是：看上方和右方剩下的格块
    # 答案里的表达：the recursive case is that there are paths from the square to the right through an (m, n-1) grid and paths from the square above through an (m-1,n) grid
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m-1, n) + paths(m, n-1)
    
'''
Q4: Max Product
Write a function that takes in a list and returns the maximum product that can be formed using non-consecutive elements of the list. All numbers in the input list are greater than or equal to 1.
'''
def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    if len(s) == 1:
        return s[0]
    else:
        return max(max_product(s[1:], s[0] * max_product(s[2:])))

'''
Q5:  Flatten
Write a function flatten that takes a list and returns a "flattened" version of it. The input list may be a "deep list" (a list that contains other lists).

In the following example, [1, [[2], 3], 4, [5, 6]] is a deep list because [[2], 3] and [5, 6] are lists. Note that [[2], 3] is itself a deep list.

>>> lst = [1, [[2], 3], 4, [5, 6]]
>>> flatten(lst)
[1, 2, 3, 4, 5, 6]

Hint: you can check if something in Python is a list with the built-in type function. For example:

>>> type(3) == list
False
>>> type([1, 2, 3]) == list
True
'''
def flatten(s):
    """Returns a flattened version of list s.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> deep = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(deep)
    [1, 2, 3, 4, 5, 6]
    >>> deep                                # input list is unchanged
    [1, [[2], 3], 4, [5, 6]]
    >>> very_deep = [['m', ['i', ['n', ['m', 'e', ['w', 't', ['a'], 't', 'i', 'o'], 'n']], 's']]]
    >>> flatten(very_deep)
    ['m', 'i', 'n', 'm', 'e', 'w', 't', 'a', 't', 'i', 'o', 'n', 's']
    """
    "*** YOUR CODE HERE ***"
    if len(s) == 1:
        if type(s[0]) == list:
            return flatten(s[0])
        else:
            return [s[0]]
    if type(s[0]) == list:
        return flatten(s[0]) + flatten(s[1:])
    else:
        return [s[0]] + flatten(s[1:])

# another solution
# def flatten(s):
#     """Returns a flattened version of list s.

#     >>> flatten([1, 2, 3])
#     [1, 2, 3]
#     >>> deep = [1, [[2], 3], 4, [5, 6]]
#     >>> flatten(deep)
#     [1, 2, 3, 4, 5, 6]
#     >>> deep                                # input list is unchanged
#     [1, [[2], 3], 4, [5, 6]]
#     >>> very_deep = [['m', ['i', ['n', ['m', 'e', ['w', 't', ['a'], 't', 'i', 'o'], 'n']], 's']]]
#     >>> flatten(very_deep)
#     ['m', 'i', 'n', 'm', 'e', 'w', 't', 'a', 't', 'i', 'o', 'n', 's']
#     """
#     lst = []
#     for elem in s:
#         if type(elem) == list:
#             lst += flatten(elem)
#         else:
#             lst += [elem]
#     return lst 