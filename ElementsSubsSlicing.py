''' Appending and Substituting elements using Slicing in Lists '''

l = [1,2,3,4]

l[5:] = [5] # appending

print(l)

l[2:] = [10] # substituting and thus mutating
print(l)

# Lists follow indexing, slicing, concatenation, len(), iterables and mutables!


''' Extending Lists '''

# list.extend(iterable)
# Extend the list by appending all the "items" from the iterable. Modifies the list. Return type = None

list_1 = [1,2,3,4,5]
print(list_1)


list_1.extend([1,2,3])
print(list_1)

list_1.extend('str')
print(list_1)

list_1.extend((10,20,30))
print(list_1)

# So you can take in any iterable (namely string and tuples) and put all their items into the current list.
# So I mutated list.


''' del statement ''' 

# del is a keyword rather which when used in an expression of lists can help in 
# deleting elements using indexing and slicing and also can delete a name from namespace.
# Doesnot returns anything. just modifies the list.

l = [10,20,30,40,50]

del l[0]

print(l)

del l[1:3]

print(l)

del l[:] # delete the list[0:end+1]

print(l)

del l # delete the name l from the namespace

# Using the name l before declaring it again will give error now.


''' list() built in'''

# list(iterables) = takes in iterables. And makes every item of the iterable as the item of the list.

new_list = list('abc')
print(new_list)


new_list.extend(list((1,2,3)))

# I am updating new_list by extending it to add more elements from a list (1,2,3)
# list(1,2,3) converts the tuple (1,2,3) into list [1,2,3]
# that list then goes into extend, extend([1,2,3])
# list.extend() does its work.

print(new_list)




''' list.sort() and sorted(list) '''

# sort() is a method of list class. Modifies the current list. Return Type = None

# sorted() takes in any uniform iterable and does the sorting. Returns a new object. Doesnot modifies the current object.


lst = [51,20,78,93,2]

lst.sort()
print(lst)

newlst = [11,50,3,45,98,10]

b = sorted(newlst)

print(b)
print(newlst)

print(id(newlst),id(b))