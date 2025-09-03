"""
Before seeing what a closure is, we have to first understand what nested functions and non-local variables are.
Nested functions in Python
A function that is defined inside another function is known as a nested function.
Nested functions are able to access variables of the enclosing scope.
------------------------------- CLOSURES---------------------------------------------------------------
closures in Python help to invoke functions outside their scope.
The function innerFunction has its scope only inside the outerFunction.
But with the use of Python closures, we can easily extend its scope to invoke a function outside its scope.
"""


def outerfunction(text):
    print("this is outer function", text)

    def innerfunction(*colors):
        for n in colors:
            print(n)
        print("this is inner function", text)

        def innerinnerfunction(**colortypes):
            for key, value in colortypes:
                print(key, value)
            print("this is inner inner function", text)

        return innerinnerfunction()

    return innerfunction


# main function -->
if __name__ == '__main__':
    myfunction1 = outerfunction("Hi!")
    myfunction1("red", "blue", "orange")




