''' Aliasing = Giving different names to the same object '''
''' Cloning = Creating 2 different objects but completely identical. '''

# Aliasing 
lst = [1,2,3,4]
lst2 = lst
print(lst2)
print(id(lst),id(lst2))

# Any change in one is seen in both.
lst.append(5)
print(lst,lst2)

#----------------------------------------------------------------------

# Cloning

lst3 = [1,2,3,5,6]
lst4 = lst3[:] # Cloning can be of 2 types = Shallow Copying and Deep Copying.

# Shallow Copying, 2 different objects. 

print(lst3,lst4)
print(id(lst3),id(lst4))
# Change is one is not seen in both.

#----------------------------------------------------------------------

# Some serious problems that Aliasing causes in Nested lists.

list1 = [10,20,30]

list2 = [40]

list3 = [list1] # Note, list3 has nested list. List of list1

print(list3)

list3.append(list2)
print(list3)    # Now again I have 2 nestings.

# Since I have referenced list3 to list1 and list2.
# If I make any changes to list1 and list2, list3 will see it too.!!

list1.remove(20)

print(list1)
print(list3) # 20 got removed from both of them. Because they were pointing to the same list object.

list2.extend([60])

print(list2)
print(list3)  # 60 got added to both of them!!


# SO TO AVOID SUCH PROBLEMS, ALWAYS MAKE A CLONE/COPY OF THE LIST. AND USE ITS FREELY.

#----------------------------------------------------------------------

''' Concatenation doesnot changes the current object '''

# Strings and tuples are in itself immutables so they won't change at all.
# But lists do concatenate, but a new object is formed.
# If a name is given to it then okay, otherwise it remains nameless and unaccessible.

l = [1,2,3]
y = [5,6,7]

print(l+y)
print(l)
print(y)

c = l+y
print(c)


#----------------------------------------------------------------------


''' Use Clones of lists if you want to make changes to the original lists while iteration over the current list '''

#------------------------------------------------------------------------


''' is operator, == operator. Differences. '''

# is operator -> checks if 2 objects have the same identity, i.e. share the same memory location.

# Are they the same object?? (Since each object has a unique identity and if 2 objects have the same identity then they
# must be the same object).


# is checks for the same memory locaion (or same object)
# == just checks for the same value. (Clones will return True)


l = [1,2,3]
# Aliasing, so they refer to the same object.
print(y is l)
print(l is y)
y = l
print(l == y and y == l) #This is also true, if they're same object! They've the same value too.


l = [2,3,4]
y = l[:]
# Cloning, So they refer to different objects.

print(y is l)
print(l is y)
print(l == y and y == l) # Only this returns True, Since they have same value.




# is operator has some inconsistencies.
# It shows different results when used in file mode and shell due to performance issues.

# Use is only in file mode.



h = 20
z = 20
print(id(h),id(z)) # Note , h=20, z=20 both point to same object.

# But the same is not true for Lists.

h = [1,2,3]
z = [1,2,3]
print(id(h),id(z))  # Different objects.

