''' Finding Common divisors and saving them in a tuple '''

def findDiv(a,b): # We wish to go to upto the smallest number to find the 'Common' divisor. 
    divisor = ()
    for i in range(1,(min(a,b)+1)):
        if a%i == 0 and b%i == 0:
            divisor = divisor + (i,) # Saving that into tupple.
    return divisor


print(findDiv(20,100))


''' Finding the min and max common Divisior, min >1 and max<=smallest number among the two '''

def findExtremeDiv(a,b):
    maxValue , minValue = None,None
    for i in range(2,(min(a,b)+1)):
        if a%i == 0 and b%i == 0:
            if minValue == None or i < minValue:
                minValue = i
            if maxValue == None or i > maxValue:
                maxValue = i
    return minValue,maxValue

min_Com_Div, max_Com_Div = findExtremeDiv(20,100) # findExtremeDiv will return a tuple. Using multiple assignment, Unpacking
                                                  # will happen.

print(min_Com_Div, max_Com_Div) # Now these 2 contain individual values.
                 