''' Swapping failed'''

x = 1   # x is pointing to 1 , x is a name and 1 an int object.
print(id(x))
y = 2    # y is pointing to 2.
print(id(y))

y = x  # y now points to the value held by x. The handle to 2 is lost now.

print(x,y)
print(id(x),id(y)) # Since both points towards 1 , their id is same as that of x.

x = y            # This will not make any difference because x and y pointing to the same object.
print(x,y)
print(id(x),id(y))



''' Swapping corrected'''

a = 1
b = 2
print(a,b)
print(id(a),id(b))

# Taking a temp variable to hold the values.
t = a
a = b
b = t

print(a,b)
print(id(a),id(b))

print("\n")
''' Super easy method to swap'''

#Python allows multiple assignment.

x, y = 2, 3           # x points to 2 and y points to 3

print(x,y)
print(id(x),id(y))

x, y = y, x   # First the right hand side is loaded by Python.     
# Now x points to object of y and y points to object of x.


print(x,y)
print(id(x),id(y))
