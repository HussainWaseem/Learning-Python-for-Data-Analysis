''' Functions as Methods of Objects '''

# String Object has many methods defined for it.
# Remember as Strings are immutables so everytime a string is manipulated, actually a new string object is returned.


#1. str.capitalize()

# Return a copy of the string with its first character capitalized and the rest lowercased.

string = 'abc'
print(string.capitalize)   # Here I've not used (). So this will return a function object.
#<built-in method capitalize of str object at 0x000000FC9CA35E30>

print(string.capitalize()) # Abc


#2. str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found. returns -1 if not found.
# Indexing starts with 0.
string = 'abcdefcdef'

print(string.find('cde')) #2


# 3. str.replace(old, new[, count])
# Return a copy of the string with all occurrences of substring old replaced by new. 
# If the optional argument count is given, only the first count occurrences are replaced

string = 'I am Python. Python is beautiful language. Python 3.6'

print(string.replace('Python','PyReplaced',2)) # Only replaces first 2 occurunces of 'Python'.


#4. str.startswith(prefix[, start[, end]])
# Return True if string starts with the prefix, otherwise return False

string = 'Hello World'
print(string.startswith('He'))



# DIFFERENCE BETWEEN str.index() and str.find()

string = 'hello'

print(string.index('llo'))
print(string.find('llo'))

# Both index and find can search for a substring.
# But if substring not found, index generates a ValueError. find will return -1.

print(string.find('W'))
print(string.index('W'))

#----------------------------------------------------------------------------

