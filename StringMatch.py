''' Write a function that accepts two strings as arguments
and returns True if either string occurs anywhere in the other, and False
otherwise. Hint: you might want to use the built-in str operation in. '''

def string_match(str1,str2):             # str1 and str2 are parameters
    if str1 in str2 or str2 in str1:
        return True
    else:
        return False
    
x,y = input("String1 = :"),input("String2 = :")

print(string_match(x,y))            # I've to use print because the function call doesnot
# x and y are arguments.           # prints the output by itself (no print used).

print(type(string_match))
# class = function.
# function has its own class.