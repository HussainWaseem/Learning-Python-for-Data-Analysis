''' GCD using iteration '''

''' The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

Write an iterative function, gcdIter(a, b), that implements this idea. 

One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, 
and iteratively reduce this test value by 1 until you either reach a case where the test divides 
both a and b without remainder, or you reach 1. ''' 

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a>b:
        test = b
    else:
        test = a
    while( test > 1):
        if a % test == 0 and b % test == 0:
            break
        else:
            test -= 1
    return test

#-------------------------------------------------------------------------------------------------
    

''' GCD using Recursion '''
''' A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. 
Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b) '''


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:  # Algo works fine only when in gcd(x,y) x>y.
        pass
    else:
        a,b = b,a  # swap if b > a.
    
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
    
    
# NOTE - If we don't use the return keyword in the last else part. Then after successive calls
        # to the function my last popping off function will not return anything to the previous function call and so on.
        # So the return value ill be None overall.
# By using return I will be returning a solved value from every function.