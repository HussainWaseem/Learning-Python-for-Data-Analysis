''' Floating point representation'''

# 1. Normal notation
new_var = 5.0
print(type(new_var))

# All the data types are classes in Python.

# Scientific Notation

new_var = 2.5e2 # stands for 2.5 * 10^2
print(new_var)  # just prints the normal floating notation
print(type(new_var))



''' Complex Numbers'''

new_var = 3+5j    # Note its j not i as in mathematics.

print(type(new_var)) # class = complex

print(new_var.real) # Both returns in floating point notation

print(new_var.imag) # real and imag are methods of complex class.


''' Boolean'''

new_var = True # 'T' should be Upper case.

print(type(new_var))  # class = bool



''' ASCII - Numerical representation of a str class'''
# In Python there is no 'char' type

new_var = 'a'

print(type(new_var))  # class = str

print(ord(new_var))  # ord returns the ASCII value of a str letter!



''' Converting str to int and float'''

# TYPE CASTING - Changing types

new_var = "1234"

new_var = int(new_var)

print(type(new_var))  # becomes int
print(new_var)


new_var = "5678"

new_var = float(new_var)

print(type(new_var))  # becomes float
print(new_var)



''' Numeric value to string'''

new_var = 1234

new_var = str(new_var)

print(type(new_var)) # becomes str
print(new_var)



new_var = 324.0

new_var = str(new_var)

print(type(new_var)) # becomes str and 324'.0' this last decimal part also remains.
print(new_var)



''' Working with date and time in Python'''

import datetime  # importing a module

print(datetime.datetime.now())  # returns the present time.

print(str(datetime.datetime.now().date()))   # Just prints the date





''' No Rounding to Nearest Integer'''

float_numb = 3.5

print(int(float_numb))  # returns 3. Does no roundoff. Truncates the entire decimal part. 




''' print returns a None type'''

print(print())  # returns None. It justs prints!!

# In Shell, 3+5 gives OUT[] but print(3+5) doesnot.
# OUT[] is due to a returned value.

print(type(print))  # is a built_in_function




''' Python uses Higher level of type as default (float)'''

# adding int and float gives float.

print(5+3.25) #8.25