def fac(n):
    if n<2:
        return 1
    return n * fac(n-1)

def perm(n):
    return fac(n)

def perm_reps(n, a):
    tmp = 1
    for item in a:
        tmp *= fac(item)
    return fac(n)/tmp
