'''
Problem:

    Consider a two-player game in which there are n initial pebbles on a table. The players take turns, removing either one or two pebbles from the table, and the player who removes the final pebble wins. Suppose that Alice and Bob play this game, each using a simple strategy:

    - Alice always removes a single pebble
    - Bob removes two pebbles if an even number of pebbles is on the table, and one otherwise
    
    Given n initial pebbles and Alice starting, who wins the game?
'''

def alice(n):
    if n == 0 or n == 1:
        print("Alice wins!")
    else:
        return bob(n-1)
    

def bob(n):
    if n == 0 or n == 1 or n == 2:
        print("Bob wins!")
    else:
        if n % 2: return alice(n-2)
        return alice(n-1)