# Lambda expression is anonymous(nameless) function
"""
A lambda function can take any number of arguments, but can only have one expression.
syntax >

         lambda arguments : expression

Why lambda functions :-
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument,
and that argument will be multiplied with an unknown number:
"""

x = lambda a: a + 10  # adding 10 to argument a and return result
print(x(5))
print(x(12))
print(x(20))
print(x(30))
print(x(50))

print("-------------------------------------------------------------------------------------------------")

# Multiply argument a with argument b and return the result:
x = lambda a, b: a * b
print(x(2, 3))
print(x(5, 8))

print("-------------------------------------------------------------------------------------------------")

# Add argument a, b, and c and return the result:
x = lambda a, b, c: a + b + c
print(x(2, 3, 4))
print(x(5, 6, 7))

# Using lambda as an anonymous function :-
"""
Say you have a function definition that takes one argument,
and that argument will be multiplied with an unknown number:
"""


def myfunc(n):
    return lambda a: a * n


"""
Use that function definition to make a function that always doubles the number you send in:
"""

mydoubler = myfunc(2)
print(mydoubler(11))

"""
use the same function definition to make a function that always triples the number you send in:
"""

mytrippler = myfunc(3)
print(mytrippler(11))
