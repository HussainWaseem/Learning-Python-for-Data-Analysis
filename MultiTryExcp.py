''' divising elements of a list by element calculated by list[index] '''



def fancy_divide(numbers,index):
    try:
        denom = numbers[index]         
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
 
# remember - else clause is only executed when try is ececuted successfully.
        # if try gets an exception, then exception clause is executed and else clause is not executed.
        # finally is executed after try/else/exception.
        
# We are catching just the index error.
# If we get a ZeroDivisionError then first the finally clause will be executed then the error will be casted by
# python shell.
        
        
# Correct input
fancy_divide([0, 2, 4], 1)

# Index Error -
fancy_divide([0, 2, 4], 4)

# ZeroDivisionError

fancy_divide([0, 2, 4], 0)



# MAKING SOME IMPROVEMENT IN THE ABOVE PROGRAM,
# IF INDEXERROR IS CATCHED THEN WE AGAIN CALL THE FUNCTION BUT WITH A REDUCED INDEX.
# ALSO WE ADDED A ZERODIVISIONERROR.

def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")
        
# Correct input
fancy_divide([0, 2, 4], 1)

# Index Error -
fancy_divide([0, 2, 4], 4) # But in this case, multiple calls will be made to the function itself.
                           # and everytime the function is called, in one of the calls 
                           # where there is no error try-else and finally has to be executed.
                           # So statements will be printed accordingly for that function call.
                           # And finally clause will be executed for all the previous calls. Printing 0 multiple times.

# ZeroDivisionError
fancy_divide([0, 2, 4], 0)








# Nesting try blocks.


def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")

# When an exception is raised, firstly the inner except clause is checked.
# if exception not handled by the inner except clause then the outer block is checked.
# If not handled by that then an error is raised in Python shell.

        
# Correct input
fancy_divide([0, 2, 4], 1)

# Index Error -
fancy_divide([0, 2, 4], 4)

#ZeroDivisionError
fancy_divide([0, 2, 4], 0)




# Whenever an exception is "raised" in a try block, information(string) regarding that exception is saved by Python
# in an exception object known only to python.

# If we want to get access to that object we can.

# using -> raise<exception> as obj

def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")  # HERE 0 IS THE REQUIRED INFO OF THE RAISED EXCEPTION
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom        # But a ZeroDivisionError is also raised here.
    except Exception as ex:
        print(ex)
        


# When ZeroDivisionError is raised within finally clause, it first searches whether there is any inner except block
# to catch it. But no. So the exception is catched outside, because there is a ZeroDivisionError catch block.
        


# So here we got 2 exceptions. One raised manually and it has info 0.
# One raised due to wrong input , and it is ZeroDivisionError.
        
# Since 0 is raised by Exception 
# And in except clause we are catching with Exception only.
# And except clause catches the latest exception.
        
# So Exception now has ZeroDivisionError as the new info.
# ex is the object which has error info.


#ZeroDivisionError
fancy_divide([0, 2, 4], 0)



def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)

# Now here, our latest exception will be 0.
#ZeroDivisionError
fancy_divide([0, 2, 4], 0)


#---------------------------------------------------------------------------------------
while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except Exception as obj:  # An exception is raised by Python when we enter a wrong input (Eg - 'a')
                               # the control goes to except block to handle the error. Except block saves the info
                               # of error into obj.
        print(obj)
print("Well Done!")

# raising the error can be done in try/else/finally block.
# in except you have to handle the error.



# REMEMBER - When there are multiple except blocks at same level, only one of them is executed.