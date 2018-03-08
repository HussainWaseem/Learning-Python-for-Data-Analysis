''' Newton Raphson '''

# Exhaustive Enum = In this we were using guesses but we were going all the way from beginning to end.
# And we were only looking for correct or wrong answers. No approximation.


# Approximation = It was an improvement over Exhaustive Enum in a way that now we can make more correct guesses 
# and can give an approximate answers to those which are not representable.
# But due to correctness, we have to take a very small epsilon and steps.
# No. of guesses we made was in the order of answer/steps, it took a lot of time.

# Bisection Search = It was a massive improvement over both of the above in terms of speed.
# We were approximating as well as making smart guesses.
# We were at each guess looking for the correct search bound by leaving half of the range.

# Newton Raphson Method = Well it tells us that if we improve our guesses in each iteration ,we might reach our 
# goal much earlier, even earlier than bisection search.
# we were using Approximation, but our steps were not in the order of epsilon**2.
# But we were making guesses which were more smart and calculated.

''' Square root using Newton Paphson Method '''

x = int(input("Give your Integer : "))
answer = x/2
epsilon = 0.01
guess = 0

while abs(answer**2 - x) >= epsilon:
    answer = answer - ((answer**2)-x)/(2*answer) # this is newton's betterement method of guess for Sq Root.
    guess += 1

print("Number of guesses made:",guess)

print("Approximate Sq root is:",answer)

# If I remove this betterment of guess method, and set the answer to increment of epsilon and run this program.
# then this program will run too slow!!
