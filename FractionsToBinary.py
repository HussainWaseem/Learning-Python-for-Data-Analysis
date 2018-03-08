''' Fractions to Binary '''

# Method ->> Fractions -> decimals using 2**x multiplication -> Then converting decimal to binary.
          # -> Then dividing the resultant binary by 2**x (Or right shift x times) to get the outcome.         
  
num = float(input("Give your fraction : "))  # we have to take a float. 
x = 0

if num < 0:
    num = abs(num)
    isNeg = True
    
elif num > 0:
    isPos = True
    
if num == 0:
    isZero = True



while (num - int(num) != 0):  # Checking if my num is not a whole number keep multiplying it with power of 2.
    num = num * (2**x)
    x += 1
print(num)   # printing the number too to see what whole number we get at the end of loop.

result = 0
mylist = []        # We take an empty list.
while num > 0:
    result = int((num%2))    # we take int, because num was in float. But we want remainders/bits in either 0/1.
    print(result)            # Printing the binaries too.
    mylist.append(str(result))  # creating a string list (Why?). But all the bits are from back to front order
                                # Since modulo gives bits from back to front.
    
    num = num // 2  

mylist.reverse()     # reversing the list to get correct binary order.

result = "".join(mylist)   # we had to use join() thats why we took string list. (Answer to Why!)
result = int(result)        # Now the result was in string taken out from join(). So we convert it into int.
result  = result * (10**-x)  # Now finally right shifting it the number of times we multiplied by pow of 2.

if isNeg == True:
    print("Binary is",-result)

elif isPos == True:
    print("Binary is",result)

elif isZero == True:
    result = 0
    print("Binary is",result)

