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
        trial += 1
    # loop fell through without finding a factor
    return True

#usage:
#f(48) returns [2,2,2,2,3]
#f(-5) returns 120
def f(n):
    if n<0:
        n = -n
        result = 1
        for i in range(2,n+1):
            result *= i
        return result
    if n<2:
        return []
    trial = 2
    output = []
    while n > 1:
        while n % trial == 0:
            output += [trial]
            n //= trial
        trial += 1
    if n > 1:
        return output + [n]
    else:
        return output

g = math.gamma
