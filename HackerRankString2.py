''' String validation

You are given a string . 
Your task is to find out if the string  contains:
alphanumeric characters, alphabetical characters, digits, lowercase
and uppercase characters. 

Output Format

first line, print True if  has any alphanumeric characters, else print False. 
second line, print True if  has any alphabetical characters, elseprint False. 
third line, print True if  has any digits, else print False. 
fourth line, print True if  has any lowercase characters, else print False. 
fifth line, print True if  has any uppercase characters, else print False. '''

string = input("Give me the string : ")
alpha = 0
digit = 0
lower = 0
upper = 0

for i in string:
    if i.islower():
        lower += 1
        
    if i.isupper():
        upper += 1
        
    if i.isalpha():
        alpha += 1
        
    if i.isdigit():
        digit += 1

if alpha >= 1 or digit >=1: # for alphanumeric
    print("True")
else:
    print("False")

if alpha >=1:         # for any alphabet
    print("True")
else:
    print("False")

if digit >=1:        # for any digit
    print("True")
else:
    print("False")

if lower >= 1:     # for any lower case
    print("True")
else:
    print("False")
    
if upper >= 1:     # for any upper case
    print("True")
else:
    print("False")
    
    
#---------------------------------------------------------------
    
''' Python any function '''

# any(iterable)
# Return True if any element of the iterable is true.
#If the iterable is empty, return False. 

def any(iterable):
    for element in iterable:
        if element:           # checking if element == True
            return True
    return False

#--------------------------------------------------------------
    
# List Comprehension
# [ append value for loop]
my_list = [i for i in range(5)]
print(my_list)
# for i in range append i to the list


''' Using any() function and List comprehension to do above problem'''

s = input("Give string : ")
print(any([i.isalnum() for i in s])) # any takes in iterable. 
                                    # We are giving list.
print(any([i.isalpha() for i in s]))
print(any([i.isdigit() for i in s]))
print(any([i.islower() for i in s]))
print(any([i.isupper() for i in s]))            

# first the list is generated consisting of bool values.
# then any() evaluates the list.
# it returns true or false.
# then print() takes in the returnd bool value and prints it.



