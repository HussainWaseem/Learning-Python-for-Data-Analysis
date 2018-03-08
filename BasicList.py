''' Introducing Lists'''
# List = Compound Data Type (Can contain multiple type of objects within it).

''' Defining List'''
# Compound data type
list_1 = [1,2,3,4]
list_2 = ['a','b','c']
list_3 = [True, False]
list_4 = [None, 1, 'a', True]


# Nesting of lists
list_5 = [list_1, list_2, list_3, list_4]
print(list_5)

print("\n")

# Accessing (indexing) elements

print(list_1[0])
print(list_2[2])
print(list_3[1])


print("\n")


# Accessing sub list
print(list_5[0])
print(list_5[0][0])

print("\n")


# Slicing of Lists
print(list_1[0:3])

print(list_2[:3])

print(list_5[2:])

a = list_1[:] # Produces a Shallow copy of list.
print(a)
print(id(a),id(list_1))

print("\n")


# len function on list

print(len(list_5)) # Note list_5 is a nested list. Each individual list is 
                   # taken as one element here.



#----------------------------------------------------------
''' Difference between x+=1 and x = x+1 method '''   

#They are almost same for integers and floats, but for lists:

#lis = lis+['foo'] creates a new list by concatenating lis and ['foo'] and then assigns the result to lis



#lis += ['foo'] is equivalent to lis.extend([foo])or lis.append('foo')               
   
a = [1,2,3]
print(id(a))

a = a + [3,4,5]
print(a)
print(id(a)) # New list object created. a has lost the handle to previous list object.                  
                   

a = [1,2,3]
print(id(a))

a += [3,4,5]
print(a)
print(id(a)) # Same list object.


                   
                   
                   
                   
                   
                   