''' Write a recursive Python function that has a
parameter representing a list of integers and returns the maximum
stored in the list. Thinking recursively, the maximum is either the
first value in the list or the maximum of the rest of the list,
whichever is larger. If the list only has 1 integer, then its maximum
is this single value, naturally. '''


def RecurMax(listn):
    if len(listn) == 1:
        return listn[0]
    
    else:
        return max (listn[0],RecurMax(listn[1:]))        
    
print(RecurMax([2,3,4,7,6]))