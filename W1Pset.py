''' Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5 '''

my_str = input("Give a string : ")
count = 0
for letter in my_str:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count += 1

print("Number of vowels:",count)


#---------------------------------------------------------------------------------


''' Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2 '''


new_str = input("Give me a string in lower case : ")

countBob = 0
for i in range(len(new_str)):
    if new_str[i:].startswith('bob'):    # startswith is a method of string which checks
                                        # if a string starts with given value or not.
        countBob += 1
print("Number of times bob occurs is: " + str(countBob))

# The loop will run over for every letter.
# And will check for every letter that whether the letter follows bob or not.



# ---------------------------------------------------------------------------------


''' Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
occur in alphabetical order. For example, if s = 'azcbobobegghakl',
then your program should print

Longest substring in alphabetical order is: beggh


In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc '''


s = input("Enter string in lower case : ")

current_str, longest_str = s[0],s[0]

for i in range(len(s)-1):  # Running for one less because if at last then have nothing to compare
                           # ahead.
    if s[i] < s[i+1]:
        current_str += s[i+1] # I concatenate
        if len(current_str) > len(longest_str): # I'm not updating the longest string
                                      # if the size is same. Therefore the earliest will be saved.
            longest_str = current_str
    else:
        current_str = s[i+1]   # Otherwise I move on to check for another set of substring.
        
    







