''' Memoization '''

# Memoization -> memorizing the calculation results of processed input such as the results of function calls.
# If the same input or a function call with the same parameter values is used, the previously stored results
# can be used again and unnecessary calculation are avoided.
# for eg-> in recursion.

# Dictionaries can be used to store the results, Function object or argument mapped to its calculated value.


def memoization(function):
    memo = {} # Argument : value
    def helper(x):
        if x not in memo: # If Argument not in memo
            memo[x] = function(x) # Calculating that func call and adding it to memo.
        return memo[x] # return the pre calculated value of that function call.
    return helper

@memoization # Decorator. # This takes fibo() as its argument.
def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

print(fibo(200))

import time
start = time.time() #time.time() returns time at that point of instruction.
print(fibo(200))
end = time.time()
print("\n")
print('Time taken to calculate',end - start)

# Recursion without memoization might go to exponential (worst) time complexity.

