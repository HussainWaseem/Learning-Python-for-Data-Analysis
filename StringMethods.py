''' Commonly used String Methods '''

# Common Sequence Operations

#1. Membership test

s = 'abc'
print('a' in s)
print('b' not in s)

#2. len()

print(len(s))

#3. index(sub,[start],[end])   -> Raises ValueError if sub is not found.

print(s.index('b'))

#4. count(item)

a = 'aaaabbbccc'
print(a.count('a'))

#5. Slicing, Indexing, Concatenation

#6. min () and max()

string = 'Hello World'

print(min(string))  # space is taken as minimum (if present).
print(max(string))

new = 'abcdef'
print(min(new)) #a
print(max(new)) #f


#-----------------------------------------------------------------------------------


# Sequence of same type can be compared!!

# In particular, tuples and lists are compared lexicographically by comparing corresponding elements.
# This means that to compare equal, every element must compare equal and the two sequences must be of the same type
# and have the same length.

print('abc' > 'a')

print('H' > ' ')

print('ABCD' > 'abcd')

print('New' < 'nEW')

#--------------------------------------------------------------------------------------------

''' More special string Methods '''
# NOTE - EVERY METHOD WILL RETURN A STRING. NOT MODIFYING THE ORIGINAL STRING (Since a string is immutable obj).

# str.capitalize()

s = 'new game'

print(s.capitalize())    # Note - Since we are not making the name s rebind to a new returned object, s will be same.




# str.endswith(suffix,[start[end]])

print(s.endswith('me'))
print(s.endswith('e'))

print(s.endswith('game'))

print(s.endswith('new game'))



# str.startswith(prefix[, start[, end]])
# Returns True if string starts with the prefix, otherwise return False.



print(s.startswith('new'))



# str.find(sub[, start[, end]])

# Returns the lowest index in the string where substring sub is found, else returns -1.

print(s.find('m'))

print(s.find('k'))




# str.isalnum().  isalpha(),  isdigit(), islower(), isupper(), isnumeric(),

# str.isidentifier() -> Checks for valid identifier name

s = '2abc'
print(s.isidentifier())



# str.join(iterable)   -> takes in only 'string iterable' and joins each item of iterable by str.

print('-'.join(['a','b','c']))
print('-'.join('abc'))





# str.split(sep= None,max= -1)   -> if max split is not given, then will be splitted for all mentions of sep.
                               # -> returns a list

print('hello world'.split(' '))

# If I'm splitting at any character, then that character will not be a part of the list.


print('    1 2 3    '.split())
# If sep is not mentioned then -> consecutive whitespace are regarded as a single separator,
# and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace.






# str.lower() and str.upper() -> returns a lower case and upper case copy of the string.



# str.replace(old, new[, count]) -> Replaces old with new for the number of count given (from starting).

new = 'seven eight'

print(new.replace('eight','ten'))



# str.swapcase()
# Returns a copy of the string with uppercase characters converted to lowercase and vice versa.


# str.title() -> hello world -> Hello World
# Returns a titlecased version of the string 


