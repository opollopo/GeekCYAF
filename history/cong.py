def t1():
    print(1)


def t2():
    print(2)


def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)


def f(n):
    a, b = 0, 1
    for k in range(n):
        a, b = b, a+b
    return a


print(fib(5))
