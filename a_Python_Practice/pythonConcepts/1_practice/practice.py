x = lambda a, b, c: a + b + c
print(x(1, 2, 3))


def myfunc_args(*args):
    for n in args:
        print(n)


def myfunc_kwargs(**kwargs):
    for i, v in kwargs.items():
        print(i, v)


myfunc_args("keshav", "sharma", "arti", "pooja", "sk sharma")
myfunc_kwargs(a=1, b=2, c=3, d=4, e=5)
