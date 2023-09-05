# Namespace and Scope
# In Python Namespace is a system to have a unique name for each and every object in Python. An object might be a variable or a method. Python itself maintains a namespace in the form of a Python dictionary. Let’s go through an example, where we have a variable “a” and a method “func()” and we are going to check their namespace.
# Different Types Of Namespace
# There are mainly two types of namespace:
#
# Local Namespace
# Global Namespace
# Local Namespace
# Local Namespace is created whenever a function is called, and it ceases to exist once the function is returned. Hence, the Local Namespace is temporary. Local variables are created in Local Namespace.
#
# Example
def func():
    a = 10
    print(locals())


# Global Namespace
# The Global Namespace contains all the variables and methods which are accessible to the whole program. The Global Namespace is created when our program starts execution, and it ends when the program terminates. Global variables are created in Global Namespace.
#
# Example
a = 10


def func():
    global a
    a = 20
    print(globals())


# Syntax:
# dir(object)
#
# Example
a = 10


def func():
    pass


print(dir())
print(dir(func))
print(dir(a))
# Output
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'func']
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
# Scope
# Scope refers to the coding region from which particular Python object is accessible. Hence one cannot access any particular object from anywhere from the code, the accessing has to be allowed by the scope of the object.
#
# Python Scope follows the LEGB Rule:
#
# Local Scope
# Enclosing Scope
# Global Scope
# Built-in Scope
# Local Scope
# Any variable declared inside the function’s body is known as the local variable. This variable is present in the Local Scope of a function and not outside the function. They have a local scope.


# Example
def func():
    a = 10
    print(a)


func()
print(a)
# Output
# 10
