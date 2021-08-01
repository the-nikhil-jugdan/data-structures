from functools import reduce


def factorial_recursive(num):
    if num > 0:
        return num * factorial_recursive(num-1)
    elif num == 0:
        return 1


print(factorial_recursive(5))

num = 5

print(reduce(lambda a, b: a*b, range(1, num+1)))
