''' Comparing FLoats '''

# Floats are stored as floating points numbers in the memory.
# They have a precision upto 53 decimal places.

# So x = 0.1 and y = 0.1 may not have same representation due to some approximation by the end of precision.
# So x == y will give False

x = 0.0
count = 0
for i in range(10):
    x += 0.1
    count += 1 
    
print(count)  # gives 10 times the loop ran
if x == 1.0:
    print("x is",x)
else:
    print("x is",x)  # but x is actually 0.99999999 and not 1.0
    
#------------------------------------------------------------------------------------------------------------
x = 0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1   # 0.1 added 10 times should give 1.0

y = 1.0

z = 0.1*10 # should give 1.0

print(x,y,z)   # x = 0.9999, y = z = 0.1

print(x == y) # False

print(y == z)  # True

#-------------------------------------------------------------------------------------------------------

# Therefore Float comparison should only be done line abs(x-y) < epsilon rather than x == y
# If yes then both are approximately equal.

# print() automatically rounds numbers to some significant digits.
# 0.1 has 53 decimal precision. print(0.1) prints 0.1. It rounds.

# While rounding print does approximations. This leads to different values.

