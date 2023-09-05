# _ and __ in  python
# _ is used to indicate that a variable is private. It is just a convention and does not actually make the variable private.
#
# __ is used to indicate private variables in a subclass. It stores the variable name as _<className>__<variableName>. So, it can be accessed outside the class using this name.
#
# Example
class MyClass:
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", world!"


mc = MyClass()
print(mc.__superprivate)
print(mc._semiprivate)
print(mc.__dict__)
print(mc._MyClass__superprivate)
