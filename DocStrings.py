''' Ways to retrieve DocString '''

# For functions, docstring are on the 1st logical line inside the function block.

def hello_name(name):
    ''' Says hi to your name '''
    
    return "Hello " + str(name)

print(hello_name("Waseem"))

print(hello_name.__doc__)
# f.__doc__


# Note - The convention followed for a docstring is ->
# a multi-line string where the first line starts with a
# capital letter and ends with a dot.
# Then the second line is blank followed by any detailed
# explanation starting from the third line. 

#-----------------------------------------------------------------------

''' Renaming a function '''

nameChanged = hello_name

print(nameChanged("Eric"))