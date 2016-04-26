def p(a):
    print a

i = input

ri = raw_input

def pr(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        # loop fell through without finding a factor
        return True
