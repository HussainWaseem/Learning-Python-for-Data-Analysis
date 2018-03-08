# Python's for statement iterates over the items of any sequence or iterable (list,tuple,string,dictionary(mapping)) 
# in the order that they appear in the sequence.

''' For using Range'''

# In a nutshell, range() generates successive Values . 
# which is generally used TO ITERATE over with for loops.

# There's many use cases.
# Often you will want to use this when you want to perform an action X number of times,
# where you may or may not care about the index. 

# Other times you may want to iterate over a list (or another iterable object),
# while being able to have the index available. Using membership functionality.


# All parameters must be integers.
# All parameters can be positive or negative.
# If we are giving a negative parameter, We have to use a negative step too.


'''range(stop)'''

for element in range(5):  # last integer is not included.
    print(element)


print("\n")


# ------------------------------------------------------------------------

''' range([start], stop)'''

for element in range(3,8):
    print(element)

print("\n")
 


#---------------------------------------------------------------------------


'''range([start], stop, [step])'''

for element in range(3,10,2):
    print(element)
print("\n")    
    
# Negative step

for element in range(10,3,-2):
    print(element)    
print("\n")    
    

for element in range(3,10,-2):
    print(element)              # Won't work but won't show any error. Just that there will be
                                # no iteration happening. Since wrong collection given. 
    
    
 #--------------------------------------------------------------------------


my_list = [1,2,3,4]

for i in range(len(my_list)):    # len will be 4. 
    print(my_list[i])
    
print("\n")    
# Python 3.x, the range() function got its own type
    
a = range(5)
print(a)
print(type(a))  # class = range

#---------------------------------------------------------------------



num = 10

print(num)
for num in range(5):
    print(num)

print(num)
# num defined out of for's scope is used within too.
# num is updated to 4 since num has only one scope (main scope)


#--------------------------------------------------------------------------
print("\n")
''' Range checking the variable only for 1st iteration'''

x = 4
for j in range(x):
    for i in range(x):
        print(i)
        x = 2
    print("\n")

# When we first enter the outer loop x is 4.
# Now for tht loop x will not change

# when we enter the innermost loop, x is set to 4.
# But when we exit x has now a value of 2.
        
# Remember - range generates all the values at the very first iteration.
# Therefore every time you go through the outer loop after 1st iteration,
# range won't check x.
        
# But when you go to the innermost loop. It is running afresh.
# Therefore x is set to 2 at 1st iteration.



#------------------------------------------------------------------------
    
'''Let s be a string that contains a sequence of decimal numbers
separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints
the sum of the numbers in s.'''

total = 0.0
my_str = input("Enter decimal numbers separated with comma : ")

my_list = my_str.split(",")  # I splitted the numbers and stored them as string
                             # in a list.

for each in my_list:
    total = total + float(each)   # casted each element of list to float
print("total sum is",total)  # Found the total.



