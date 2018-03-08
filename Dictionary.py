''' Checking multiples items for a person in multiple lists '''


def getGrade(name_list,grades_list,course_list,student):
    grade,course = '',''
    i = ''
    i = name_list.index(student)  # I'm finding the student in the names and giving its corresponding results in other lists.
    grade = grades_list[i]
    course = course_list[i]
    return grade,course        # This is saved as a tuple

print(getGrade(['A','B','C','D'],['A+','B+','B','C'],['TA101','CS231','CS201','CS109'],'B'))

# But these operations will get messy when there is large data. More lists and more info in each list.


''' Idea of Dictionary - A Structured type in Python '''

# Dictionary - Data Structure of form {key1: value1, key2: vlaue2} (key-> value mapping)
# (Dictionary is not a sequence but a mapping (non-sequence))

# We can index dictionary. Find its length. Iterate over it.


# keys should be unique. keys should be immutable like strings,constants,tuples.
# values can be mutable as well as immutable.
# Therefore you can overwrite(change) a value linked to a key but can't change a key.

# values are objects and keys are names.

#Dictionaries can be indexed (with taking key as argument), but they can't be sliced.

# Dictionary is an unordered collection just like set. This is the reason we can't index set at all but
# we have to use keys instead of position to index dictionary.


# Indexing in dictionaries using key.

d = {1:'a',2:'b',3:'c'}

print(type(d)) # class = dict
print(d[2])

d[4] = 'd' # Adding a key-value pair.
print(d)

del d[3] # Deleting using a key.

print(d)

print(len(d)) # key-value pair makes up one item.


# Membership test using keys! 
print(1 in d)
print(5 in d)

# Overwriting values

d[1] = 'Hello' # Now 1 maps to 'Hello' and not 'a'.
print(d)




# Calling d.keys()/values()/items() will return a DICTIONARY VIEW OBJECT (which is an iterable).
# They are just dynamic view of the keys/values/itempair of the dictionary.
# They are not a copy.
# They change as dictionary changes(Thats why dynamic)

# It supports operations like membership test and iteration(can be used in for loop),
# but its contents are not independent of the original dictionary


print(d.keys()) # just keys
print(d.values()) # just values
print(d.items())  # pairs

print(type(d.keys())) # These have their own types = dict_keys/values/items.


for i in d.values():
    print(i)


d[2] = 'New'

for i in d.values():
    print(i)

# Any change in d will change the view object.
    
print('New' in d.values()) # True









''' Mutating list when it is a value given to a dictioanry '''

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')     #animals['d'] returns a list ['donekey']. In this list we append 'dog' and 'dingo'.
animals['d'].append('dingo')



#--------------------------------------------------------------------------------------




def how_many(d):
    '''
    d: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    Counting multiple values differently if they are combined in a list.
    '''
    total = 0
    for i in d.values():
        total = total + len(i)
    return total

new = {'a': ['aardvark'],
 'b': ['baboon'],
 'c': ['coati'],
 'd': ['donkey', 'dog', 'dingo']}

print(how_many(new))

# Works fine.
# Goes to each value(that is a list), count the length of the list and adds it to total.
# In this way total numbers of values are returned.


#-----------------------------------------------------------------------------------------


def biggest(d):
    '''
    d: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    current = 0
    for i in d.values():  # iterating over lists
        if len(i) > current: 
            current = len(i) # Storing largest length of the list of values.
    
    tup = d.items() # getting tuples (key,vlaue)
    for i in tup:
        if len(i[1]) == current: # if len of the list in the tuple was the largest that I stored
            z = i[0] # then give me that key
            break
    if z!= None:
        return z # If I have stored a valid key return that
    else:
        return None # otherwise return None.
    
print(biggest(new))


#-----------------------------------------------------------------------------------------