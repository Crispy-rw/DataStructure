#/usr/bin/python3

"""
Implement the function fib(n) which returns the nth number in the fibonacci sequence, using only 0(1) space
"""


def fib(n):
    a = -1
    b = 1
    c = 0

    for _ in range(n):
        c = a + b
        a = b
        b = c

    return c



if __name__ == "__main__":
    print(fib(10))

