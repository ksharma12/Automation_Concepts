x = lambda a, b: a + b
print(x(23, 34))


def my_func(a, b):
    return lambda c, a, b: a * b * c


mydoubler = my_func(23, 34)
print(mydoubler(12, 23, 34))
