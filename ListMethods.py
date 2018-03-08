''' Some popular Lists Methods '''

# 1. list.sort() = Modifies the uniform typed-list. Return type = None.

a = [80,45,96,74,100]
print(id(a))
a.sort()
print(a)
print(id(a))   # both ids are same. Therefore it only modifies the old list. Doesnot creates a new object.

print(a.sort()) # Returns None. Since s.sort() returns a None type.
#--------------------------------------------------------------------------------------------------


# 2. list.append(item) = Modifies the current list. Return type = None.

print(id(a))
a.append(65) # ppends 65 to the existing list.
print(a)

print(id(a))

a[len(a):] = [66] # Another way to append. (Whenever you slice a list, you get a list object).
print(a)

# Note - a[len(a):] = 66 , This won't work. The left hand side results in a list but the right hand side is an int.

#--------------------------------------------------------------------------------------------

#3. list.insert(index,item) = Modifies the list. Return type = None.

a.insert(0,145) # 145 at 0th index
print(a)

a.insert(len(a),500) # insert at the end = append
print(a)

#--------------------------------------------------------------------------------------------

# 4. list.remove(item) = Modifies the list. Return type = None.
a.remove(74)
print(a)
print(a.remove(500))
print(a)
# Just removes one element (the first occurence of item)
#--------------------------------------------------------------------------------------------

#5. list.pop([i]) = Pops the item at the given index and returns the item.
                  # if i not given as an argument then return the last item (The item at the end of the list).

print(a.pop(5))
print(a)
print(a.pop())
print(a)

# Difference between pop() and remove() = both remove the items form the list.
# But remove() doesnot returns anything. pop() returns the item.
# remove() takes item as argument.
# pop() takes index as an argument.
# pop()'s argument is optional, but remove()'s is mandatory.

#--------------------------------------------------------------------------------------------

#6. list.count(item) = Returns the number of time item appears in the list.
# A similar function can be written.

def count(lst,item):
    c = 0
    for i in lst:
        if i == item:
            c += 1
        else:
            pass
    return c

b = [5,5,5,2,5,4,5,5,5]
print(count(b,5))    # returns 7


#--------------------------------------------------------------------------------------------

#7. list.reverse() = Modifies the list by reversing it. Return Type = None.

a.reverse()
print(a)
print(a.reverse()) # return type = None

#--------------------------------------------------------------------------------------------

# 8. list.copy() = Returns a Shallow copy of a list.

# Shallow list - A list without a nested structure.
# shallow copying -> Copying a Shallow list.

# Slicing operater can create only a shallow "COPY" of the list.

c = [1,2,3]
d = c[:] # c and d point to 2 different objects.

# d is a shallow copy of c.
print(id(c))
print(id(d))


list_3 = [1,2,[3,4,5]]
# First let me explain the memory situation of list_3.
# list_3 points to a list object whose 1st and 2nd element points to integer objects 1 and 2. 
#And 3rd element points to
# a list object [3,4,5]

list_4 = list_3[:]
print(id(list_3))
print(id(list_4))

# Here what has happened is -> list_4 has new copies of 1st and 2nd element.
#But for the 3rd element that is a sublist "Only a referecne" is created to that sublist for list_4.

# So the 3rd element of list_3 and list_4 "points to the same list object -> [3,4,5]"

# So any changes made using one name ONLY FOR 3RD ELEMENT is seen by other name too.
# This defies the concept of copying.

print(list_3)
print(list_4)


list_4[0] = 'a'
print(list_4)
print(list_3)
# Since we are modifying the copied part, isolation is maintained.


list_4[2][0] = 'b'
print(list_4)
print(list_3)
# We modified the referenced part -> Both the lists see the change.


#--------------------------------------------------------------------------------------------


# 9. list.clear() = Modifies the same list. Deletes all the items within it. Return type = None.

print(id(a))
a.clear()
print(a)
print(id(a))


#--------------------------------------------------------------------------------------------
#10. list.index(item,[start,[end]]) = Returns the index of the first encountered item given. start/end optional.

# indexing starts from 0

h = [1,2,3,4,2]
print(h.index(2))