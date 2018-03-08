''' Functions are also objects '''

# They have type = function
# They can be used in assignment.
# They can be used as an argument.
# They can be an item of a Structured type in Python (list, tuple, dictionary).

# But function objects are just their names refering to the object.
# f refers to a function obj. Not f().

def ListofFunc(L,x):
    for f in L:
        print(f(x))

ListofFunc([abs,int],-4.50)   # I used function objects as an item of the list.

# A first class object is an entity that can be dynamically created, destroyed, passed to a function, 
# returned as a value, and have all the rights as other variables in the programming language have.

# In Python "EVERYTHING" is a first-class-object.


''' map function in Python '''

# map(function, iterables) = It takes a function and proper set of iterables and applies that function
# to each item of that iterable.

# If one iterable given, function is applied sequentially.
# If more than one iterables given, then function is applied in pairs parallely..



# Returns an iterable.


for i in map(abs,[-1,2,-3.5,-7]):
    print(i)
 
    


list_1 = []
for i in map(abs,[-1,2,-3.5,-7]):
    list_1.append(i)
    
print(list_1)


L1 = [17,20,30]
L2 = [80,10,20]

L3 = []
for i in map(min,L1,L2):   # 17,80 is 1st pair, 20,10 and 30,20 another.
    L3.append(i)

print(L3)


#---------------------------------------------------------------------------

def applyEachTo(L, x):
    ''' L is a list of function objects.
    x is any int/float '''
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result



#---------------------------------------------------------------------------
    
# Multiple Concatenation in Sequences.
    
l = [1,2,3]
print(l*3)

n = 'abc'
print(n*3)

n = (1,2)
print(n*3)

#---------------------------------------------------------------------------

# Range also follow indexing and Slicing.
# One indexing they give an integer.
# On Slicing they give a range object.


l = range(5)
print(l)

print(l[2])

print(l[1:4])

print(l[:])






