''' Cube Root by Exhaustive Enumeration'''

x = int(input("Give your integer, I'll tell you its cube root : "))

answer = 0

while(answer**3 < abs(x)):
    answer += 1             # Here answer will only go upto cube range of x.
    
    
if answer**3 == abs(x):
        
    if x < 0:             # If x was negative, then cube root must be -ve too.
        answer = - answer  
    print(answer,"is the cube root.")
    
    
else :
    print("Given integer is not a perfect cube.")

    
# Exhaustive Enumeration uses a Decrementing function.
# It is non negative at first so the loop works.
# It decrements after each looping and finally becomes 0 or less so
# the loop terminates.
    
# For exhaustive technique, the loop gets exhausted and terminates for all
# integers.

# abs(x) - answer**3 = Decrementing function
    
    
    
''' Doing it with for loop '''


y = int(input("Give your integer, I'll tell you its cube root : "))

for ans in range(abs(y)+1):  # abs(y)+1 because the range will produce numbers from 0 to y.
    if ans**3 >= abs(y):
        break

if ans**3 != abs(y):
    print("Given integer is not a perfect cube.")
else:
    if y < 0:
        ans = -ans
    print(ans,"is the cube root.") # this print is not a part of if.

    
    
    
    
    
    
    
    
    
    
    