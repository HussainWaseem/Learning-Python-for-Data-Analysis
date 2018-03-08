''' Bisection Search - A great Improvement over Exhaustive Enumeration and Approximation '''


''' Square root of Positive Numbers '''

x = int(input("Give your Integer : "))
answer = 0
low = 1
high = x  # search bound = (low,high) = (1,x) read as 1 to x.
guess = 0
epsilon = 0.01
answer = (high+low)/2 # I start my guess right at the midpoint of my search bound.

while abs(answer**2 - x) >= epsilon: # While my guess is not that close to answer
    print("low = " + str(low) + " high = " + str(high) + " answer = " + str(answer))
    
    if answer**2 > x: # if my guess was larger than expected. Then I have to search backwards.
        high = answer
    else:           # # if my guess was smaller than expected. Then I have to search forwards. 
        low = answer 
    answer = (high+low)/2 # Since I updated high and low, now we got to make a new guess.
    guess += 1         
    
# When I exit the loop, I'm pretty sure I have found my answer.
print("Number of Guesses : ",guess)
print("Approximate Sqaure root is :",answer)

# Way too fast!!

# We check at every guess that whether our answer is larger/smaller than expected.
# If larger, we need to search only backwards.
# So we push the high to the place we are(answer).

# If smaller, we need to search only forward.
# So we push the low to the place we are(answer).
 
# Finally when we get an answer which is close enough, we exit the loop.

# NOTE - We are cutting half the search bound in every guess we make.
# We thow away the half search bound every time.
# Thats the reason we have to make very less and accurate guesses!



# Earlier using Exhaustive Enumeration we did the same problem in some 30k steps. Doing sequentially/linearily.
# Now we did it in 13 minimal steps.!!
# Because we are not going sequentially from beginning to the answer.
# We are just making smart guesses now.
# If we improve our guess making mechanism more then we will improve on time more than this implementation.





#----------------------------------------------------------------------
''' For fractional numbers whose root doesnot lie in the search bound '''
x = float(input("Give your Fraction : "))
answer = 0
low = x    # Here we make a change
high = 2*x  # here too. Actually we are changing our search bound from (1,x) to (x,2x) 
guess = 0
epsilon = 0.01
answer = (high+low)/2 # I start my guess right at the midpoint of my search bound.

while abs(answer**2 - x) >= epsilon: # While my guess is not that close to answer
    print("low = " + str(low) + " high = " + str(high) + " answer = " + str(answer))
    
    if answer**2 > x: 
        high = answer
    else:          
        low = answer 
    answer = (high+low)/2 
    guess += 1         
    

print("Number of Guesses : ",guess)
print("Approximate Sqaure root is :",answer)

# Rather than searching in the normal bound, I search in the next mirror bound.
# For fractions between 0 and x. Its root lies between x and 2x.
# So I search between x and 2x.
#------------------------------------------------------------------------------


''' Square Roots of Negative numbers is a complex number- Cheap trick '''

x = int(input("Give your Negative Integer : "))
x = abs(x) # I have to use positive x just like I used in positive number.
answer = 0
low = 1
high = x
guess = 0
epsilon = 0.01
answer = (high+low)/2 

while abs(answer**2 - x) >= epsilon: 
    print("low = " + str(low) + " high = " + str(high) + " answer = " + str(answer))
    
    if answer**2 > x: 
        high = answer
    else:          
        low = answer 
    answer = (high+low)/2 
    guess += 1         
    

print("Number of Guesses : ",guess)
print("Approximate Sqaure root is :" + str(answer) + 'i')

# NOTE - Negative number and positive numbers are mirror images on number line,
# So I will find the root of positive number but at last will make the root mirror
# itself on the negative side by using i (sqrt(-1)).

# Negative numbers have complex roots.


# ------------------------------------------------------------------


''' Cube Roots of Negative numbers is a negative number '''

# If used "cheap trick" you can make the final answer turn negative.
# But neatly you can change the bound you were searching and also if else conditions.


x = int(input("Give your Negative Integer : "))
answer = 0
high = 0  # Think of a negative number line.
low = x      # low is set to x since x is negative. search bound = (x,0)
guess = 0
epsilon = 0.01
answer = (high+low)/2 

while abs(abs(answer**3) - abs(x)) >= epsilon: # we are putting abs internally 
                                     # because here we are only concerned about
                                    # difference in the guess and the correct answer.
    print("low = " + str(low) + " high = " + str(high) + " answer = " + str(answer))
    
    if abs(answer**3) > abs(x):  # We will find an answer more closer to zero.
        low = answer
    else:          
        high = answer  # We will find answer farther away from 0
    answer = (high+low)/2 
    guess += 1         
    

print("Number of Guesses : ",guess)
print("Approximate Sqaure root is :",answer)



#------------------------------------------------------------------------

# Bisection Search has a complexity of log(base2)N.
# Because every time the search bound is reduced by 1/2.

# N is the number to be searched. (In our case the answer).
# Eg = log(base2)128 = 7.
# So to search 128 in a given bound. We need only 7 steps.