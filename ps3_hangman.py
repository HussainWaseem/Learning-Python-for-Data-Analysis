# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

    
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
            string = string + ' _ '  # If still not guessed, then add _ and make it hidden.
    
    return string



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
    
    secretWord = chooseWord(wordlist).lower()   # string.lower()
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    
    print("-----------------")
    
    guess_left = 8
    lettersGuessed = []
    
    while guess_left > 0:
        
        print('You have ' +str(guess_left)+ ' guesses left.')
    
        print('Available Letters: ',getAvailableLetters(lettersGuessed))
        
        guess = input('Please guess a letter: ')
        guess = guess.lower()
        guess_left -= 1
        
        
        
        
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)                # We are appending first because getGuessedWord() 
                                                        # will look into list.
            print('Good Guess: ',getGuessedWord(secretWord, lettersGuessed))
            
            if isWordGuessed(secretWord, lettersGuessed):
                print('Congratulations, you won!')
                print('------------------')
                break
           
            
        elif guess in lettersGuessed:
            print('Oops! You have already guessed that letter: ',getGuessedWord(secretWord, lettersGuessed))
        
        elif guess not in secretWord:
            print('Oops! That letter is not in my word: ',getGuessedWord(secretWord, lettersGuessed))
        
        print('--------------------')
            
            
    if not isWordGuessed(secretWord, lettersGuessed):
        print('Sorry, you ran out of guesses. The word was ' +secretWord)








# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)


