''' In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
The computer makes guesses, and you give it input - is its guess too high or too low?
Using bisection search, the computer will guess the user's secret number!

Here is a transcript of an example session:

Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83 ''' 





print("Please think of a number between 0 and 100! It must be an Integer")

low = 0
high = 100

game = True

while(game == True):
    answer = (high+low)//2   # Everytime I run through the loop, I'm calculating midpoint 
                              # of the search bound and asking.
    print("Is your secret number",answer)
    print("\n")
    
    print("Enter 'h' to indicate the guess is too high.\
    Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    print("\n")
    x = input("Enter Here : ")
   
    if x == 'c':           # the moment I find the right answer, I break out of the loop.
        game = False
    elif x == 'h':           # If my guess was too high, I adjust my high to number
                             # to look only backwards.
        high = answer
        
    
    elif x == 'l':      # ... adjust my low to answer to look forwards.
        low = answer
        
    else:
        print("Sorry, I did not understand your input, Retry entering.")
        x = input()    # retaking input and again asking.
    
print("Game over. Your secret number was",answer) # Finally giving the correct output.


# NOTE - we have used floor division (to just welcome whole numbers/integers.)
# So that we don't have to deal with fractions.

                
        
    
    
    
    
    
    
    
    
    
    
    
    
