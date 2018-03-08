''' Decimal to Binary '''

# If we take a decimal number, and keep on taking its modulo by 2. We will keep on getting its remainder.
# But everytime we take modulo, we do floor div of that number by 2 too, this shifts all bits to right.
# This gives me the next remainder.

# The remainder will be our binary. Since we are taking mod 2 then remainder must be 0 and 1.

# We do this until our number gets decreased to 0.



# In short ->> num mod 2  and num//2 .


num = int(input("Give your decimal : "))

if num < 0:
    num = abs(num)
    isNeg = True
elif num > 0:
    isNeg = False
    isPos = True
    
if num == 0:
    print("Binary is 0")

result = ''
while num > 0:
    result = str(num%2) + result # this num%2 will give us binary digits from backside. 
                                  # We'll be concatenating each time.
    num = num // 2  # decreasing number.
    
if isNeg == True:
    print("Binary is",-result)

elif isPos == True:
    print("Binary is",result)
    
    
    
    
    
    