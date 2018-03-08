''' Approximation Algorithm Technique '''

# For those problems whose answer can't be represented exactly. So we approximate
# the answer.

# For that we need a close enough asnwer.
# So we iterate at very close steps.
# The difference betwen the actual and approximate answer should be very less.
# Therefore Decrementing function should also be very less.


''' Square root of a negative number or a number who is not a perfect square '''

epsilon = 0.01  # this is the close enough difference between approx and correct.
guess = 0         # number of guesses made.
iterate = epsilon**2   # very small increment in answer to check all possible approx.
answer = 0.0

x = int(input("Give your number : "))
while abs(answer**2 - x ) >= epsilon and answer <=x :
    guess += 1
    answer += iterate

if abs(answer**2 - x) >= epsilon:
    print("Failed to find square root")
else:
    print("Close enough sq root is",answer)
print("Total number of guesses",guess)

# As epsilon decreases, the number of iterations increases.
# Therefore program becomes slow.
# But we get more accurate answer.

# But if epsilon/iteration is large,
# Program takes lesser number of guesses thus making it fast.
# But Program might miss a possible approx and will give wrong output.


#---------------------------------------------------------------







''' Exhaustive Enumeration works only if the answer lies in the search interval '''

''' Square root of a negative number or a number who is not a perfect square '''

epsilon = 0.01  # this is the close enough difference between approx and correct.
guess = 0         # number of guesses made.
iterate = epsilon**2   # very small increment in answer to check all possible approx.
answer = 0.0

x = float(input("Give your Fraction : "))
while abs(answer**2 - x ) >= epsilon and answer**2 <=x :
    guess += 1
    answer += iterate

if abs(answer**2 - x) >= epsilon:
    print("Failed to find square root")
else:
    print("Close enough sq root is",answer)
print("Total number of guesses",guess)


# We made 2 changes here.
# int to float of input
# answer <=x to answer**2<=x

# Why? - If we have an answer for eg "0.5" as the sq root of 0.25.
# Our answer is out of bound of our search which is from 0 to 0.25.

# So to increase search bounds (in fractions) we increase the bound of second condition.


# No. of guesses (No of times we go through the loop)
# = answer/iterating step.  

# Since we have to reach the answer. The moment we reach the answer, the loop breaks.

# Simply we can understand ->> If we want to reach 24. We have a step of 2 each time.
# If we start with 0.
# we take 24/2 = 12 guesses to reach 24.

# 12 times loop ran. 2 steps per loop. 24 is our answer.

#------------------------------------------------------------------


# THINKS TO REMEMBER -

# IF OUR PROGRAM GIVES "FAILED OUTPUT"
# THEN WE SHOULD TRY TO MODIFY OUR EPSILON TO MORE SMALLER.
# BECAUSE WE MIGHT BE MISSING THE POSSIBLE APPROXIMATION.

# WE SHOULD ALSO TRY TO REDUCE OUR STEPS TO MORE SMALLER.

#-------------------------------------------------------------------


# Disadvantages of Exhaustive Enum and Approximation =

# 1. With exhaustive enumeration, we only can give representable answers.
# 2. We might not find the correct answer in approximate technique.
# 3. Program becomes a lot slower if we want to find the correct answer.