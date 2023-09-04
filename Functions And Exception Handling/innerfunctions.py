# In Python Inner Functions are the functions which are defined inside another function.


# Example 1: How to define Inner Functions in Python?
def outerFunction(text):
    def innerFunction():
        print(text)

    innerFunction()


outerFunction("Hey!")


# Example 2: How to access Inner Function?
def outerFunction(text):
    def innerFunction():
        print(text)

    return innerFunction


myFunction = outerFunction("Hey!")
myFunction()
