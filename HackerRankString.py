''' You are given a string . 
Your task is to swap cases. In other words, convert all lowercase letters 
to uppercase letters and vice versa. '''

my_str = 'Www.HackerRank.com'

for i in my_str:
    
    if i.isupper():
        my_str = my_str.replace(i,i.lower())
    elif i.islower():
        my_str = my_str.replace(i,i.upper())
    else:
        continue
print(my_str)



#----------------------------------------------------------------

# Using a swapcase Method.
my_str = 'Www.HackerRank.com'
my_str = my_str.swapcase()
print(my_str)


#-----------------------------------------------------------------

''' Joining and Splitting the String '''

#join() is a method defined for string class.
# Takes a sequence_of_strings as input, joins the sequence with string given in form of iterables.
# Always returns a string.


# str.join(sequence_of_strings)

# sequence_of_strings can be list of strings, string itself, tuples of strings.

str_in = 'Www.HackerRank.com'

str_out = "-".join(str_in) # Join str_in elements with '-'
print(str_out)




# split is also a method of strings.
# It takes separator as an input.
# 
# Separates the string using separator and returns a List of separated parts.


# string.split(separator,max_split)

str_in = 'Www.HackerRank.com'

list_out = str_in.split(".")
print(list_out)


# to retrieve back 
str_out2 = ".".join(list_out) 
print(str_out2) 
# LIST CAN BE CONVERTED TO STRING USING join method of strings.
#-----------------------------------------------------------------------------




''' Mutations in String '''

# Strings are immutable.
# But we can bring changes in string via 2 methods -
# 1. Converting into mutable types ->> modifying ->> convert back to strings using join.
#2. Slicing and modifying.



# Change e to m
# Method 1
str_is = 'abcdefghijk'

list_temp = list(str_is)
#list is a built in function that takes in iterables and makes a list of successive values.

print(list_temp)

list_temp[4] = 'm'
str_is = "".join(list_temp)
print(str_is)

# Method 2

str_new = 'abcdefghijk'
str_new = str_new[:4] + 'm' + str_new[5:] 
print(str_new)


# So Generalise Method of string mutation
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

print(mutate_string(str_new,4,'e'))
    