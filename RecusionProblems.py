''' Recursion Problems '''

#1. Write a function that takes in two numbers and recursively multiplies them together.

def RecurMul(a,b):
    if b == 1:
        
        return a
    else:
        
        return a + RecurMul(a,b-1)
    
print(RecurMul(2,3))


#2. Write a function using recursion to print numbers from n to 0.

def PrintN20(n):
    if n < 0:
        return 
    else:
        
        print(n)
        return PrintN20(n-1)
    
PrintN20(3)


#3.Write a function using recursion to print numbers from 0 to n 

def Print02N(n):
    if n!= 0:
         Print02N(n-1)    # Here I'm not returning anything from the function.
    print(n)
    
Print02N(3)






# 4. Write a function using recursion that takes in a string and returns a reversed copy of the string. The only
#    string operation you are allowed to use is string concatenation.



def reverse_string(s):
    if s: return s[-1] + reverse_string(s[0:-1])
    else: return s

print(reverse_string('hello'))