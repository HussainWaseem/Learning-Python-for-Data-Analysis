''' Experimenting with functions, Return types and Functions as arguments '''

def f1():
    print("Inside f1")

def f2(y):
    print("Inside f2")
    return y
def f3(z):
    print("Inside f3")
    return z()

print(f1())                  # first f1() is called, so the program counter is given to f1.
                             # So it first prints Inside f1. Secondly there is no return type. 
                             # It returned None type, that is then printed by the print becasue now p-counter is at print.

print(5+f2(2))       # firstly f2(2) is called.
                    # It first prints out Inside f2 then returned y. In this case 2.
                   # that 2 and 5 then got added. P-counter points at print, which then prints 7.

print(f3(f1))       # firstly f3(f1) is called. It printed Inside f3. Then it returned z(), in this case f1().
                   # Thats means p-counter now returns/points to f1().
                  # It first prints Inside f1. Secondly there is no return type. 
                 # It returned None type, that is then printed by the print becasue now p-counter is at print.
print("\n")
#------------------------------------------------------------------------
                             
def g(x):
    def h():
        x = 'abc'
    
    x = x + 1                     # g takes x from global scope, creates its own x object.
                                   # makes that local x as 4.
    print("In g(x) x is ",x)        # this x is printed 4.
    
    h()                         # now a call to h() is made.
                              # h() has its own scope. In that scope it has its own x.
                           # that x is set to 'abc'.
    return x             # But when we exited h() its scope got deleted, that x binded to 
                            # abc also got dumped.
# return is in the scope of g(), so it returns x of g that is 4.
x = 3
z = g(x)                             # z is assigned to returned value of g(x) that is 4
                     
print("value of z =",z)
print("global value of x =",x)  # this x is of global scope. It prints 3.


print(g) # prints the function object or Memory address of function object.

# print(h) can't call h explicitely because it is not defined in global scope.


#-------------------------------------------------------------------------------


''' Comparison of functions '''

# We can't compare 2 function objects.

#------------------------------------------------------------------------------

x = 12             # Firstly the prog counter starts here, x binded to 12.
def g(x):            # then it goes here, g() is defined in the global scope.
    x = x + 1     # Python doesnot evaluates a function until its called.
    def h(y):
        return x + y
    return h(6)
g(x)                    # then it goes here and a function call is made.
 
# As soon as the parameter x is given to g.
# The x = 12 defined in global scope gets binded to x defined in local scope.

# Now we are inside g (local scope).
# x local becomes 13.

# now prog counter enter h(). Another localscope is created for h().
# return x+y returns a garbage value because y is not defined.

# As soon as Python returns from a function its scope is destroyed.
# scope of h() got destroyed.

# Again h(6) is called. And we have to return the value of h(6)
 # x is 13 that h() inherits from g(x) in the local scope. y =6.

#returns 13+6 = 19
#-------------------------------------------------------------------------
 
 
 
''' Keyword Arguments '''
 
def printName(firstname,lastname,reverse):
    if reverse:
        print(lastname,firstname)
    else:
        print(firstname,lastname)
        
printName('Waseem','Hussain',False)
printName('Waseem','Hussain',True)

print('\n')



# Suppose I want to keep some ARGUMENTS WITH DEFAULT VALUE.

def printName(firstname,lastname,reverse = False):
    if reverse:
        print(lastname,firstname)
    else:
        print(firstname,lastname)
 
# Using positional Arguments.       
printName('Waseem','Hussain') # Here I'm leaving the last argument. 
                              # So Py will use the default value.

printName('Waseem','Hussain',True)  # Overwriting the default value.



# Using keyword arguments.
print('\n')
printName(firstname = 'Waseem',lastname = 'Hussain')  

printName(lastname = 'Hussain',firstname = 'Waseem') # I can change the order.

printName(firstname = 'Waseem', reverse = True,lastname = 'Hussain')                             


# With keyword arguments you can change the order of arguments passed in to f.


print('\n')

''' Using Keyword and Positional Arguments together '''

# This will give me an error.
           # printName('Waseem',reverse = True, 'Hussain')

# WHY? When Keywrd args and positional args are used together, Keywrd args should 
# not come before any positional args.
# Here reverse is a keywrd arg used before 'Hussain'.

printName('Waseem', 'Hussain',reverse = True)
printName('Waseem',lastname ='Hussain',reverse = True)

# Also an error will popup when you accidently passed the same argument many times.
                #printName('Waseem',firstname ='Eric',reverse = True)


# Here 'waseem' binds to the firstname due to its position.
# But again 'Eric' wants to bind to firstname, that'll show an error.
# Error = Multiple values for argument firstname.
                
                
                
#-----------------------------------------------------------------------------

''' Inheriting values '''

def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

print(foo(2))
 
# Step 1 = foo is defined in global space.
# Step 2 = foo() is called. Within the local space 2 is binded to x.

# Step 3 = bar is defined within the foo(). bar has its own local space.
# Step 4 = Py will not evaluate bar() until an unless a reference(call) is made to it by its parent function.

# Step 5 = call made -> bar(3,x) -> here x is being explicitly called in the scope of foo().
# Therefore x of foo() is taken.
                                                                     
# So x = 2. bar(3,2) = 3 + 2 = 5. 
# 5 is returned.                
                
                
                
def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)          # Here no explicit call to x is made.
                           # So when in bar() z is binded with 3 and x to default 0. 3+0 = 3 is returned.

print(foo(5))                


# Its the function default that matters if you don't explicitly pass it a value.

# bar(3) passes a value for z but nothing for x.