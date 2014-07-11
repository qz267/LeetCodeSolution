__author__ = 'zheng'


def fib(n):
    if n < 0:
        raise ValueError('Should not less than 0!')
    if n == 1 or n == 0:
        return n
    x, y = 0, 1
    while(n):
        x, y, n = y, x+y, n-1
    return x


print fib(-1)
print fib(1)
print fib(100)