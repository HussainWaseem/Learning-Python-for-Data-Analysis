''' We can use the idea of bisection search to determine if a character is in a string, 
so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for (the "test character"). 
If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character. 
If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. 
(Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in a Str. 
char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value.

As you design the function, think very carefully about what the base cases should be. '''

def isIn(char,s):
    
    if s == '':
        return False     # base case 1 (Empty string)
    
    if len(s) == 1:
        return s == char  # base case 2 (string of len 1)
    
    guess = len(s)//2    # Recusrsive plot. Bisection Search.
    print('I"m making a guess. That is',s[guess])
    
    if char == s[guess]:  # if character to find is the middle one
        return True
    else:
        if char > s[guess]:     # if char is greater than the guess, search only forward.
            return isIn(char,s[(guess+1):])
        else:
            return isIn(char,s[:guess])


string,key = input("Give me any string -> "),input("Give me a key ->")

string = sorted(string)

string = ''.join(string)
print("String is ",string,",","key is",key)

print(isIn(key,string))


