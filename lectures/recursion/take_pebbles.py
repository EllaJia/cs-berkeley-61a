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