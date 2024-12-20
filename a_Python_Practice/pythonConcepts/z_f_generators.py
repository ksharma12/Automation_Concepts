print("--------------------------------generator function with yield--------------------------------")


# Generator Function in python :-
def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1


ctr = fun(5)
for n in ctr:
    print(n)

print("--------------------------------simple generator function--------------------------------")


# A simple generator function :-

# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def fun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for val in fun():
    print(val)

print("--------------------------------------simple return call----------------------------------")


def fun():
    return 1 + 2 + 3


res = fun()
print(res)
'''
Yield vs Return
yield is used in generator functions to provide a sequence of values over time. 
When yield is executed, it pauses the function, 
returns the current value and retains the state of the function. 
This allows the function to continue from the same point when called again, 
making it ideal for generating large or complex sequences efficiently.

return, on the other hand, is used to exit a function and return a final value. 
Once return is executed, the function is terminated immediately, 
and no state is retained. This is suitable for cases where a single result is needed from a function.
'''

'''
Python Generator Expression
Generator expressions are a concise way to create generators. 
They are similar to list comprehensions but use parentheses 
instead of square brackets and are more memory efficient.
'''

sq = (x * x for x in range(1, 6))
for i in sq:
    print(i)
