# ---------------------------------------- METHOD OVERLOADING ------------------------------------
from multipledispatch import dispatch


# Python does not support method overloading but there are few ways through which we can achieve this
# using multiple dispatch decorator

@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result)


@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)


@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)


print(product(2, 4, 6))
print(product(2.2, 4.6, 6.8))
print(product(6, 9))
