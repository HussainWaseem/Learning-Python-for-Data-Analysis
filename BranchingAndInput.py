''' Simple comparison using Branching'''

# Introducing input.
# If the input function is called, the program flow will be stopped
# until the user has given an input
# and has ended the input with the RETURN key.

# Input takes everything as String!

x = int(input("Enter x : ")) # type casting with input.
y = int(input("Enter y : "))
z = int(input("Enter z : "))


if x < y and y < z:     # Here if x< y is not true then it wont check further.
    print("x is the least")
    
elif y < z:           # This will be checked only if x <y is false. 
    print("y is the least")

else:                 
    print("z is the least")
    
    
    
''' Working Input wth Type casting'''    

# Integer as input, Type casting to float.
#THIS WILL WORK as input data is not lost. 

new_var = 3
print(float(new_var))





new_var = 3
new_var2 = float(input("Enter an Int : "))

print(new_var2)



#Float as input, type casting to integer. THIS WON'T WORK
# To save the truncation of input data.

print(int(input("Enter a float : ")))