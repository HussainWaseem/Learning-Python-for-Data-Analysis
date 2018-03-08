''' Exception handling '''

# An exception is an error that happens during the execution of a program.

# Error handling = saving the state of execution at the moment the error occurred 
# and interrupting the normal flow of the program to execute a special function or piece of code, 
# which is known as the exception handler.

# The code to be executed is put in try block.

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("You entered a wrong type. Try Again.")
print("Well Done!")

# The loop will run until we put in a correct value and break out of loop.
# Every time the wrong input is given, the error occurs at the line n = int(n)
# As soon as error occurs, the control is sent to except block.
# Which checks if ValueError then it prints the required statement.  

# So instead of Python printing a ValueError, we handled that error.  


# A try statement may have more than one except clause for different exceptions. 
# But at most one except clause will be executed.
# Just like continuous if and elif and else clause. Only one gets executed.

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("a/b",a/b)
except ValueError:
    print("Change Your Input.")
except TypeError:
    print("Change Your Type.")
except:
    print("Try again.")
    

# If Multiple Exceptions have to be handled in same way then we can collect all 
# exceptions in a tuple.
    

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("a/b",a/b)
except (ValueError,TypeError):
    print("Change Your Input.")
    
    
# ValueError is raised when a built-in operation or function receives an argument 
# that has the right type but an inappropriate value.
    
# TypeError occurs when the type of the input is wrong.




# Raising an Exception = Raising an Error when you want!
    # raise <exception>(arguments)
    
    
def getRatio(L1,L2):
    ''' It takes in 2 lists and returns
    the ratio of corresponding items in 2 lists '''
    ratio = []
    for index in range(len(L1)):
        try:
            ratio.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratio.append(float('NaN')) # NaN = Not a number. You can generate this object using float('NaN') or
                                                            # using math.nan
        except: # if any other error is there then
            raise ValueError("Function called with bad argument")
            
    return ratio
    
# Will raise ValueError when we try to access an invalid index, When we give wrong data in the list, or any other error.
getRatio([4,5,6,7],[1,2,3,4]) # Works fine

getRatio(['a',1,2,3],[7,8,True,'3']) # ValueError 

getRatio([1,2,3,4,5],[2,3]) # For index 2 and above L2 don't exist. But since the loop is run for len(L1), it still runs
                             # and ValueError is raised.
 
    
#--------------------------------------------------------------------------
                             
                             
''' Define a function which takes in a list inside which there is are 2other lists wrapped in a single list. 
The first list contains comma separated part of a student's name.
The next list contains comma separated marks he scored in multiple subjects. 
Return me a list which contains the first 2 lists as it is but also a 3rd list
which has the avg marks.

Note - Handle ZeroDivisionError in case when a student has not appeared for any exam
and his marks list is empty. '''


def get_stats(L):
    new_list = []
    for sub_list in L:
        new_list.append([sub_list[0],sub_list[1],avg(sub_list[1])])
    
    return new_list

def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:               # We get a ZeroDivisionError when len(grades) == 0, that is when a 
                                             # student has his grade list empty.
        print("No marks recorded for some students")
        return 0.0

L1 = [[['Waseem', 'Hussain'],[10,20,30,40]],
       [['XYZ', 'ABC'], [30,20,10,0]],
       [['tyu'],[]]]
       

print(get_stats(L1))