''' Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made ALL possible substrings. 
Substrings don't need to have a meaning.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

Input Format

A single line of input containing the string . 
Note: The string  will contain only uppercase letters: 

Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

Sample Input

BANANA
Sample Output

Stuart 12    
    
    
'''


s = input("Give String : ")
con = 0
vow = 0

for i in range(len(s)):
    if s[i] == 'A' or s[i] == 'E' or s[i] == 'I' \
    or s[i] == 'O' or s[i] == 'U':
        vow = vow + len(s) - i
    else:
        con = con + len(s) - i

if vow > con:
    print("Kevin",vow)
elif con > vow:
    print("Stuart",con)
else:
    print("Draw")
    
    
    


















