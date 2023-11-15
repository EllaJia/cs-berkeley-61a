def current_digit_process(x, digit):
    transform_x = x * 2
    if transform_x >= 10 and digit % 2 == 0:
        return transform_x // 10 + transform_x % 10
    else:
        return transform_x

def add_sum(n, digit):
    if n < 10:
        return n
    else:
        rest_n, last_n = n // 10, current_digit_process(n % 10, digit)
        return add_sum(rest_n, digit + 1) + last_n
    
def check_sum(y):
    if add_sum(y, 1) % 10 == 0: return True
    return False