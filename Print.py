''' Print function'''

# print in Python3 is a function used to print values of objects.

# Using multiple strings without separating comma will join/concatenate all of them.

print("Hello World"      "Joined")

print("Hello World" + "Joined")

# Both do the same thing -> Concatenation of strings.
# We overloaded + "

# Operator Overloading - Operators have different behaviors depending on the types of
# its arguments/operands.



print("Hello World" + " " +  "Not Joined")
# space " " is also a string. 




# print only considers the first quote signature as a beginning of string.
print("'Hello'")

# print ends with a new line too.



# Triple Quotes = Multiple lines

print("""1st Line
2nd Line
3rd Line """)

# The above should be in this format to be aligned.







''' Special Characters with backslash'''

print("first line \nSecond line")
# \n marks the beginning of new line.

print("first line \tSecond line")
# \t adds a tab.

print("first line \
Second line")
# \ tells python that it is a single lined string.





''' Escape Sequence'''

# To escape Quote Mismatch.
print("Hello He \"said\" and done.")

# to escape those quotes in between just use \"word\".
# \" before and after the word.
# \" stands for escaping " mismatch.



# Better way to escape Quotes is using a combination of ' and "

print('Hello He "said" and done.')



# Printing a single backslash
# \\

print("Hello there\\ I do have backslash!")



''' end keyword with print function'''

# print ends with a new line.

# end is a keyword that takes a value and ends the string with that value instead
# of a default newline character.
print("Hello", end = ".")
print("Hello", end = "World")

print("\n")

print("Hello", end = "")
print("Hello", end = "!")