''' Square root using guess and check method '''

''' y is the sq root of x. 
recipe for deducing square root of a number x (16)
1)Start with a guess, g
2)If g*gis close enough to x, stop and say g is the answer
3)Otherwise make a new guess by averaging g and x/g
4)Using the new guess, repeatprocess until close enough''' 

x = int(input("Give me an integer : "))
guess = int(input("Enter your guess ")) # loop variable
epsilon = 0.01

while abs(guess*guess - x) >= epsilon: # We are taking abs(since guess*guess can be negative.) Run the loop until accuracy
                                        # less than epsilon.
    guess = (guess + x/guess)/2
    print(guess)
    
print("Approximate guess of sq root is ",guess)

# Note here guess is a loop variable.
# guess is initialized outise the loop, used for the terminating condition, values is constantly changing inside the loop.

#-----------------------------------------------------------------------------------

# ints and floats are very easily casted into others.
# You can cast bool types into ints,float ans strings and vice versa.

bool(2)
bool('a')  # other types to bool, Empty seq and 0 will return false, else true. 
bool(0.0)
bool('')

str(True)
int(True)  # True = 1 or 1.0.
float(True)

# NOTE - While casting string to float and int, ValueError is shown if the string is any character.
# If string is in numeric form then it is casted.

float('a')  # ValueError for both.
int('a')



float('1234')
int('1234')  #works.

# NOTE - In python, str type is always superior to ints or floats. Therefore str > int or str> float gives True.

print('a'> 4)
print('a' > 4.0)
print('a'< 4.0)



# Python returns true if you are comparing a float and int having the same value.
print(5*2 == 5.0*2.0)
print(5.000 == 5)
#---------------------------------------------------------------------------------


''' Write a program that examines three variables—x, y, and z—
and prints the largest odd number among them. If none of them are odd, it
should print a message to that effect.'''

 
listodd = []
for i in range(3):
    x = int(input("Enter an Integer : "))
    if x %2 !=0:
        listodd.append(x)
if listodd:
    print(max(listodd))
else:
    print("No odd found!")

#------------------------------------------------------------------------------
    
s = 'abcdef'

print(s[::1] == s[0:len(s):1]) # Going from start to end.

print(s[::-1] == s[-1:-(len(s)+1):-1]) # Reverse, going from end to start 

#------------------------------------------------------------------------------

# DICTIONARY IS A COLLECTION BUT NOT A SEQUENCE. ITS A MAPPING FROM KEY TO OBJECT.

#-----------------------------------------------------------------------------------


s = 'hello'

print('e' in s)
print('e' not in s)

print((not('e' in s)) == ('e' not in s)) # This is True.

#---------------------------------------------------------------------------

# NOTE - for loop's loop variable is not local to it if a global variable is also present with that name.


num = 10
for num in range(5):
    print(num)
print(num)
# In this case the value of num got changed to 4 from 10

#------------------------------------------------------------

# To check how many times bob appears in the string.

s = 'bobobob'
count = 0
for i in range(len(s)):
    if s[i:].startswith('bob'): # slice and check for every index
        count += 1
print(count)
#----------------------------------------

# To check how many times bob appears in the string.

Str, sub = input(),input()
count = 0
while sub in Str:
    i = Str.find(sub)
    Str = Str[:i] + Str[i+1:]  # We created a new string object and changed the reference of Str to this new object.
    count += 1
print(count)

#------------------------------------------------------------------------------

def checkio(text):
    count = 0
    max_count = 0
    letter = ''
    x = ''
    
    text.lower() # converting every letter to lower case
    
    
    for i in range(len(text)):
        count = 0
        for j in text:
            if j in 'abcdefghijklmnopqrstuvwxyz':
                if text[i] == j:
                    count += 1
                    letter = j
        if count > max_count:
            max_count = count
            x = letter
            
        elif count == max_count:
                if letter < x:
                    x = letter
    
            
    
    return x
    
print(checkio("HEllo"))

 