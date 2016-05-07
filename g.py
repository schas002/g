def p(a):
    print a

i = input

ri = raw_input

def pr(n):
    if n < 2:
        return False
    trial = 2
    while trial * trial <= n:
        if n % trial == 0:
            return False
    else:
        # loop fell through without finding a factor
        return True
