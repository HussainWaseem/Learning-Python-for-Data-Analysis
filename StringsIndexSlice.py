''' Successive Concatenation'''

print("eric"*3)
print("eric "*3)

# Overloaded * - On the basis of the operand(object) it is operated with, it changes its functionality.


''' Length of a String'''
print(len("eric"))   # len just returns the length of the string including space. 
# We used print because len just returns.
# len is a function which takes string literals/ string objects as arguments.

# print(len(25)) won't work. len() only works for a sequence and dictioanry is an exception.


''' Indexing String'''

# Positive Indexing -> begins with 0.

print('waseem'[0])

name = 'waseem'
print(name[0])

#print(name[5]) will give out of bound error. Invalid index.

# both are exactly the same.


# Negative Indexing -> begins with -1 from the end of the word.

print("waseem"[-1])
print(name[-2])




''' Slicing Strings'''
# Indexing = getting individual indexed string literal
# Slicing =  getting a substring!

print(name[0:4])
print(name[:4])  # both are same. But this explicitely denotes beginning to 3rd.
print("\n")

print(name[0:6])
#(Start included, end excluded)

print(name[0:10]) # Note this will also work even though the index is out of bound.

print(name[0:2] + name[2:6])
# slicing and concatinating slices.

print(name[3:6])
print(name[3:]) # this denotes, 3rd to end of string.

print(name[:2] + name[2:])
# In first slice 0th,1st char.
# In second slice 2nd to end of string.
# s[:i]+s[i:]=s always


print(name[-5:])
# Look here you can give the start index -ve but it always move from left to right.

print(name[:])
# creates a shallow copy of name.

print("\n")
print(name[:-1])
# starts from 0th index and goes till -1st index.





''' Slicing and hopping'''

a = "HelloWorld"

print(a[0:10:2]) # cover the complete word with hop of 2.
print(a[::2]) # copy the entire word with a hop of 2

# s[startindex : endindex : hop]

print(a[::-1]) # hop of -1 that is backtrack





'''Membership test'''
print('lloW' in a)
print("Waseem" not in a)



''' One way to keep strings together - Keep them in a bracket'''

test_str = ('Hello world'
            'I am only one string.' )
print(test_str)
print(type(test_str))  # its a string.


