# -----------------------------------------------Types of Conversion-----------------------------------------------
# 1. Implicit Conversion (Automatically)
# 2. Explicit Conversion (Manually)

# -----------------------------------------------Explicit conversion---------------------------------------------
# The line `a = "1"` is assigning the string value "1" to the variable `a`.
a = "1"
b = "2"
c = a + b  # 12 because string + string = string
c = int(a) + int(b)  # first typecast a and b into integer type then store it in c
print(c)  # 3

# ------------------------------------------------Implicit conversion----------------------------------------------
a = 1
print(type(a))  # <class 'int'>
b = 2.5
print(type(b))  # <class 'float'>
c = a + b
print(c)  # 3.5
print(type(c))  # <class 'float'>
# Here, the integer variable `a` is converted into a float type implicitly by Python itself and then the addition is performed.
