''' Tuples '''
# Immutables.
# defining tuples = With braces or without braces 

t = (1,2,'l',True)
print(t)

g = 1,2,'l',False
print(g)

# Tuples are Squences (just like Strings and lists) = So they have 6 properties = len(),indexing,slicing, concatenation,
# iterable and membership test (in and not in)

# Range object is also sequence but it doesnot follow concatenation.

print(t[3])

print(t[1:2]) # prints (2,) This comma denotes that it is a tuple and not just an int object.

print(t[:])

# Assignment doesnot works for tuples. You can't change tuples

t = (1,)
h = 1,
print(t,h)


''' Iteration over Tuples and Nested Tuples '''

''' Write a Program that gets data in the form of nested tuples. Each nested tuple has an integer at index 0 and string
 at index 1.
Gather all the numbers in one new tuple and strings in another new tuple. 
Return maxnumber, minnumber and number of unique words. '''

def getData(t):
    num = ()
    words = ()
    for i in t:
        num = num + (i[0],)  # num is a tuple. (i[0],) is a singleton tuple. We concatenate.
        if i[1] not in words:  # taking only unique words
            words = words + (i[1],)
            
    min_number = min(num)
    max_number = max(num)
    unique_words = len(words)
    
    return (min_number,max_number,unique_words)


data = ((1,"Hello"),(2,"World"),(15,"Hello"))
print(getData(data))

#----------------------------------------------------------------------------------------

x = (1, 2, (3, 'John', 4),'hi')

# Whenever you slice something out of a tuple, the resultant is always tuple.
# Unlike indexing, where the resultant may be any other type.'

y = x[0:-1]

z = x[0:1]

print(y)
print(z)

print(type(y),type(z))

# Also you can multi index a string inside a tuple/list and can access its individual Character.

print(x[-1][-1])
print(type(x[-1][-1]))

#-----------------------------------------------------------------------------------


''' Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, 
where every other element of the input tuple is copied, starting with the first one. 
So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), 
then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple'). '''


def oddTuples(t):
    t_new = ()
    count = 0
    for i in t:
        if count % 2 == 0:  # Here I do for even because indexing starts from 0. Odd elements are indexed even.
            t_new = t_new + (t[count],)  # concatenation of strings.
        else:
            pass
        count +=1
    return t_new

test = ('I', 'am', 'a', 'test', 'tuple')

print(oddTuples(test))
            








