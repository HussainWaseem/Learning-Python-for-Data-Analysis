''' Requirements :

Here are the requirements for your game:


The game must be interactive; the flow of the game should go as follows :

At the start of the game, let the user know how many letters the computer's word contains For eg  _ _ _ _

Ask the user to supply one guess (i.e. letter) per round.

The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.
eg _ _ a _

After each round, you should also display to the user the partially guessed word so far, 
as well as letters that the user has not yet guessed.

Some additional rules of the game:
A user is allowed 8 guesses. Make sure to remind the user of how many guesses s/he has left after each round. 
Assume that players will only ever submit one character at a time (A-Z).

A user loses a guess only when s/he guesses incorrectly.

If the user guesses the same letter twice, do not take away a guess - 
instead, print a message letting them know they've already guessed that letter and ask them to try again.

The game should end when the user constructs the full word or runs out of guesses. 
If the player runs out of guesses (s/he "loses"), reveal the word to the user when the game ends. '''


''' Sample Output

The output of a winning game should look like this...

	Loading word list from file...
	55900 words loaded.
	Welcome to the game, Hangman!
	I am thinking of a word that is 4 letters long.
	-------------
	You have 8 guesses left.
	Available letters: abcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Good guess: _ a_ _
	------------
	You have 8 guesses left.
	Available letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Oops! You've already guessed that letter: _ a_ _
	------------
	You have 8 guesses left.
	Available letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: s
	Oops! That letter is not in my word: _ a_ _
	------------
	You have 7 guesses left.
	Available letters: bcdefghijklmnopqrtuvwxyz
	Please guess a letter: t
	Good guess: ta_ t
	------------
	You have 7 guesses left.
	Available letters: bcdefghijklmnopqruvwxyz
	Please guess a letter: r
	Oops! That letter is not in my word: ta_ t
	------------
	You have 6 guesses left.
	Available letters: bcdefghijklmnopquvwxyz
	Please guess a letter: m
	Oops! That letter is not in my word: ta_ t
	------------
	You have 5 guesses left.
	Available letters: bcdefghijklnopquvwxyz
	Please guess a letter: c
	Good guess: tact
	------------
	Congratulations, you won! '''
    
    
    
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, The word computer has selected.
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    match = 0
    count = len(secretWord) # Total number of letters to be matched.
    for char in secretWord:
        if char in lettersGuessed:
            match += 1                # If letter matched, Increment.
    if count == match:
        return True
    else:
        return False

print(isWordGuessed('apple',['a','j','p','e','k','l']))
# returns True.
# Works fine.    
    
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    string = ''
    for char in secretWord:
        if char in lettersGuessed:
            string = string + char  # If character is already guessed, add it and make it appear.
        else:
            string = string + '_'  # If still not guessed, then add _ and make it hidden.
    
    return string

print(getGuessedWord('apple',['e', 'i', 'k', 'p', 'r', 's']))

#returns _pp_e
# Works fine.






def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    case = string.ascii_lowercase  # ascii_lowercase is just a string object containing all lower case in alph-order
                                   # defined in string module.
    
    for char in lettersGuessed:
        i = case.find(char)
        case = case[:i] + case[i+1:]  # Just removing that char from available letters.
        
    return case

print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))

# Works fine, Returns alphabetically ordered letters which are not yet being guessed.    












def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up. '''


    print("Welcome to the game, Hangman!")
    secretWord = chooseWord(wordlist):
    print("I am thinking of a word that is "+str(len(secretWord)+" letters long.")
    print('-----------------')
    
    guess_left = 8
    lettersGuessed = []
    
    while guess_left > 0:
        
        print('You have ' +str(guess_left)+ ' guesses left.')
    
        print('Available Letters: ',getAvailableLetters())
        
        guess = input('Please guess a letter: ')
        guess_left -= 1
        
        
        
        
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)                # We are appending first because getGuessedWord() 
                                                        # will look into list.
            print('Good Guess: ',getGuessedWord())
            
            if isWordGuessed():
                print('Congratulations, you won!')
                print('------------------')
                break
           
            
        elif guess in lettersGuessed:
            print('Oops! You have already guessed that letter: ',getGuessedWord())
        
        elif guess not in secretWord:
            print('Oops! That letter is not in my word: ',getGuessedWord())
        
        print('--------------------')
            
            
    if not isWordGuessed():
        print('Sorry, you ran out of guesses. The word was ' +secretWord)


