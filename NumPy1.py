# NumPy ->> Scientific Library (module) of Python. Doesn't comes in Standard Library. So need to be imported separately.

# NumPy has functions and tools for Linear  Algebra, Arrays and Matrices, etc.

#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays & matrices,
# along with a large collection of high-level mathematical functions to operate on these arrays.



# Vector = 1 D Array

# Adding two vectors or two 1-D arrays.

a = [0,1,4]
b = [0,1,8]

# add these two vectors and return the resultant using simple Python.

def sumNumb(x,y):
    return x+y

def addVectors(a : list, b : list) -> list :
    return [x for x in map(sumNumb,a,b)]

print(addVectors(a,b))




##################################################################


# Arrays in NumPy ->> More efficient that lists in Python. High Performance for Large data. More cleaner code.
# NumPy has a Multi dimensional array object called ndarray. NumPy’s array class is called ndarray. 
# It has 2 parts - 
                 # Actual data
                 # Meta data, explaining the actual data


# In NumPy, the dimension of an arrays is called its Rank. Dimension = axis = rank
# Rank of Array of 1-D is called rank 1, rank of 2-D array is called Rank 2 and so on.
# The length of the array will define the length of the axis.
                 
# For 1-D array there is only 1 axis. For 2-D there are two and so on.
                 
print()                
import numpy as np

# NOTE - In NumPy arrays, it is actual array and no comma between different numbers.

# 1. creating an array from 'arange' function.

array1 = np.arange(5)    #arange (read as array-range) is a function of numpy module which takes in one parameter
                         # similar to range() and creates a 1-D array of 0 to that range. Range end excluded.

print(array1)                 
                 
                 

array2 = np.arange(5,10)
print(array2)


array2 = np.arange(0,10)
print(array2)

array3 = np.arange(0,10,2)  # Using step of 2
print(array3)


array3 = np.arange(0,10,0.5)  # Using decimal step
print(array3)

array4 = np.arange(10,0,-2) #Using negative step
print(array4)

array5 = np.arange(0,10, dtype = float)  #dtype is a keyword argument used by arange() and using it we can
                                         # specify that which data-type should our data be in array.
print(array5)

print()



##################################################################




# Creating an array explicitely using 'array' function

array1 = np.array([1,2,3], dtype = float) # works on lists, dtype keyword argument works both in arange() and array()
print(array1)

array1 = np.array((1,2,3)) # works on tuples
print(array1)

array1 = np.array('123')  # Doesn't works on strings
print(array1)

array1 = np.array({1:'a',2:'b'})  # Doesn't works on dictionaries
print(array1)


print()


##################################################################


print()
print()
print()
# Creating multi-dimensional arrays explicitely

array1 = np.array([(1,2,3),
                   (4,5,6)])  # By giving list of tuples. 

print(array1)
print(array1.ndim)

# Since NumPy is a numerical module, it only works with numbers.
print()


array2 = np.array(((1,2,3),
                   (4,5,6), 
                   (7,8,9))) # Nested tuples, 2D array
print(array2)
print(array2.ndim)




##################################################################



# To check number of dimensions (or rank) of an array using arrayObj.ndim field. It is used with array object.

print()

array1 = np.arange(10)
print(array1.ndim)


array1 = np.array(((1,2,3),
                   (4,5,6)))
print(array1.ndim)

print()



##################################################################


# To know the items in an array using arrayObj.size. Just returns the total elements in the entire array irrespective 
# of its dimension.

array1 = np.arange(10)

print(array1.size)

array1 = np.array(((1,2,3),
                   (4,5,6)))

print(array1.size)



##################################################################

# To know the datatype of elements.

array1 = np.arange(10)

print(array1.dtype)


# itemsize tells you size of each elements in bytes

array1 = np.arange(10)
print(array1.itemsize)  # So its 4 byte here



##################################################################

# Memory usage by array = itemsize (in bytes of each element) * total size (total elements) of array

# Total memory usage = Memory used by 1 elements * total elements

array1 = np.arange(10)

a = array1.itemsize
b = array1.size

print(a*b)  #40 bytes. (as 1 element is of 4 bytes and we have 10 elements)



##################################################################

# Shape (rows,columns) of the array

array1 = np.array([(1,2,3),
                   (4,5,6)])
print(array1)
print(array1.shape) 
# 2 rows and 3 columns

# But this shape will work as a size when only 1-D array is given

array1 = np.arange(10)
print(array1)
print(array1.size)



##################################################################


# Total elements in an array (matrix) = m*n = no of rows and no of columns
# arrayObj.reshape(m,n)

array1 = np.arange(15)

print(array1.reshape(3,5))  # It doesn't modifies it. Like list functions use to modify it. It returns. 
                            # We need to explicitely store the returned value again.
print(array1)

array1 = array1.reshape(3,5)
print(array1)


array1 = array1.reshape(5,3)
print(array1)

print(array1.shape)   # What is the shape of the array?
print(array1.dtype)   # What is the datatype of array?
print(array1.size)    # What is the Total size of array?
print(array1.itemsize)  # What is the item size of each element?


# array1 = array1.reshape(1,5) Gives an error as I have changed the Total size of array/matrix.

######################################################################


# Creating a Multi-data-type array -> Is it possible? No. Auto Type conversion happens.

array1 = np.array([1, 2.0, 3, 4.0])

print(array1)                            # We here see that all elements are converted to floats (Higher data type)

print(array1.itemsize)  # 8, since float.

print(array1.dtype)   # float64  (64 = 8 bytes  = 8*8 bits)

######################################################################


# Type of arrays we are creating

a = np.arange(0,10,2,dtype = int)

print(a)

print(type(a))   # <class 'numpy.ndarray'>

# 1D array = Vector
# n dimensional array = Matrix

######################################################################


# Common Errors made while creating an array.


# While array creation, necessary parameters needed is just 1. optional is dtype.
# That has to be either list, tuple, multiple lists inside a tuple, multiple tuples inside a tuple.


# You can't enter just numerals independently.
# a = np.array(1,2,3)
# a = np.array(1.0,2.0,3.0)

# These will show the error, as we have not entered lists, tuples, tuples of lists, tuples of tuples.
# List of tuples and list of lists is also allowed


######################################################################


# Creating Arrays with intial Place Holders. ->> zeros and ones matrices

# Often, the elements of an array are originally unknown, but its size is known.
# Hence, NumPy offers several functions to create arrays with initial placeholder content.


# Default dtype in these operations is float64

a = np.zeros((3,5))    # zeros() will also take 1 necessary parameter and that is size. It is creating a zero matrix.
print(a)

print()

b = np.ones((3,5))
print(b)

print()

c = np.ones((3,5),dtype = int)  # Explicitely mentioning int
print(c)


print()

d = np.ones((3,3,5),dtype = int)   # A 3D array (See the dimensions, 3,3,5)
                                   
print(d)



######################################################################


# linspace function of arrayObj -> dtype of resultant array is always float64.


# It is similar to arange() but one difference is , instead of taking step it takes valid size of matrix/array.

a = np.linspace(0,10,5)  # from 0 to 10 , number of elements I want in my 1D array is 5

print(a)

# It automatically creates most suitable elements.

a = np.linspace(0,10,20)
print(a)

# It can create any number of elements between a range.

print()
######################################################################


# Applying any function on arrayObj

# Now one intersting point of arrayObj is ->> applying any function to the array will apply that to its entire elements.

# And a new array is returned.


a = np.linspace(0,10,20)

print(a)

print()
a = np.sin(a)   #NOTE - this sin is different from sin of maths module.
                 # All functions of numpy module are array specific.
                 # All functions of math module are Python core specific.
                 # math module functions will not work on arrays.
                 # math.sin(a) will give an error.

print(a)
print()
######################################################################


# Converting available array/Matrix in zero array/Matrix and ones array/Matrix.

a = np.arange(10).reshape(2,5)

print(a)
print()


a = np.zeros_like(a,dtype = float)#zeros_like function of np module takes in an array and convert it into a zero Array.
                                  # dtype is optional to give

print(a)
print()

b = np.arange(12).reshape(4,3)
print(b)

print()

b = np.ones_like(b)
print(b)
print()

######################################################################

# arrayObj.reshape()



a = np.arange(24).reshape(2,3,4) # A 3D array # 2 rows, 3 larger_view_columns, 4 meta columns or axis 2.

print(a)



######################################################################

# If an array is too large to be printed, NumPy automatically skips the central
# part of the array and only prints the corners

print(np.arange(10000))


######################################################################

print()
# Simple Array operations. (Need to be Mathematically valid, For eg - Array of diff size can't be added/sub)

a = np.arange(10)
b = np.arange(10)

print(a)
print()
print(b)
print()


c = a+b  #Array addition
print(c)
print()

d = a-b  #Array subtraction
print(d)
print()


# Scalar Multiplication

a = np.arange(10)

a*=2

print(a)

# Checking for each element whethe it is larger /smaller than some value

a = np.arange(10)

a = a > 5

print(a)  # Only those elements which are greater than 5 we filtered as true.

####################################################################


# Array element Multiplication vs Matrix Multiplication


# Array element Multiplication

a = np.array(([1,2,3],
              [4,5,6]))

b = np.array(([1,2,3],
              [4,5,6]))
c = a*b
print(c)

print()


# Matrix Multiplication, dot product. (Should be Mathematically valid)

a = np.array(([1,2,3],
              [4,5,6]))

b =b.reshape(3,2)                # Making it valid = a = (2*3) , b = (3*2), Final Matrix of 2*2 

f = a.dot(b)
print(f)

####################################################################


# 2 variants of dot product.

# arrayObj function. a.dot(b)

# numpy module function np.dot(a,b)

####################################################################

# Common Errors that happen 

a = np.arange(10)
b = np.arange(10,dtype = float)

c = a+b
print(c)


b+=a
print(b)

# In both the cases, we tried adding two arrays of diffrent types.
# Resultant array is of higher precision.


# But if we tried this ->> This will show an error only when we use augmented addition or any other mathematical op. 
                          # Never do augmented mathematical op by keeping lower precision array on the left.
a = np.arange(10)
b = np.arange(10,dtype =float)

# a+=b Gives type error

a = a+b  #works fine
print(a)

####################################################################


# Sum, min and max from an array

a = np.array([1,2,3])

print(a.sum())   # Returns the sum of all the elements of the array

print(a.max())  # returns the max magnitude of the array

print(a.min())   # returns the min magnitude of the array


#############################################################


# Creating an array filled with random elements but of known size.

a = np.random.random((3,5))    #dtype is not allowed here. By default it is float

print(a)


# NOTE - Whenever you are creating an array from scratch and you have to directly give the size as a paramter.
# Then input the size in a tuple. (x,y)

# Giving the size just as numerals x,y will cause an error.


# These cases are common error points when using zeros(), ones(), np.random.random()

#############################################################



# To make any array 1-D (or to say to flatten any array) -> arrayObj.ravel()

a = np.arange(18).reshape(3,3,2)

print(a.ndim)
print(a)

a = a.ravel()

print(a.ndim)
print(a)

############################################################

# In NumPy axis = 0 is the column  and axis 1 = row

# What does it means??
# axis are genrally rows.
# axis = 0 means no rows, that is only columns

# axis = 1 , means, there are rows.  Kind of O|1, true false .

###############################################################



# Sum of rows and column separately

a = np.arange(10).reshape(2,5)

print(a)

print(a.sum(axis = 0))  # no rows. Therefore sum of columns. Returns a 1-D array of sum
print(a.sum(axis = 1))  # rows.  Therefore sum of rows in the form of 1-D array.


####################################################

# max and min from each axis.
print()

a = np.arange(10).reshape(2,5)
print(a)

print()
print(a.max(axis = 0))  # 1-D array of max from each column
print(a.max(axis = 1))  # # 1-D array of max from each row


print(a.min(axis = 0))
print(a.min(axis = 1))

##########################################################

# Creating an identity matrix -> using a function called np.eye()
# In an identity matrix all the left to right diagonal elements are 1 and rest are 0.
# It is always a square matrix (a matrix in which rows = columns)

a = np.eye((3))   # it takes number of rows = number of columns as its parameter.
print(a)

print(a.ndim)


##########################################################

# Creating an array filled with random integers.

a = np.random.randint(1,50,10)   # Syntax different that np.random.random((n,m)) -> it generated float elements.
                                 # Its syntax is that of linspace but no endpoint and retstep parameters.
print(a)
# Always creates a 1D array as linspace.
# But here all 3 parameters are necessary unlike linspace where 3rs parameter is optional with a default value of 50.

# You can reshape it, just like linspace array.
a = a.reshape(2,5)
print(a)

##########################################################

# Whatever Mathematical operation you apply on Numpy ndarray object,
# the operation doesn't changes the array but the elements of the array.

# Changing an array of celsius temp into farh temp.

C = np.array([20.4, 15.32, 12.89, 30.45, 21.78])

C = (C*9/5) + 32

print(C)


# But in case of list, we had to for loop in, go to every element and then apply this math opr
# creating a new list then.

# It complex, low performance and less readable.
# But in NumPy, its high performance, less complex and more readable.



##########################################################

# Plotting our temperature values we calculated above

import matplotlib.pyplot as plt  # matplotlib is a Plotting/Graphical package of Python.
                                 # pyplot is a special plotting module from matplotlib package.
                                  # matplotlib is built upon Python, NumPy and SciPy.

plt.plot(C) 
plt.show()

# Indices of elements of the array become as x axis. (Here 5 elements -> 0 to 4)
# Values of these elements become y axis.


##########################################################

# Weird things with arange.()

a = np.arange(0.5,10.4,0.8,dtype = int)
print(a)

# This returns 0 to 13. But How? My array should stop at 10

# Because -> NumPy first sees the start, stop and step and calculates the number of elements that need to be there
# in the array. In this case 13.

# After that the dtype is seen by the NumPy, that is int.
# So the array is forcefully filled with 13 elements by a step of 1 since 0.8 is rounded to 1 as int.

##########################################################

# Default of linspace, if number of elements are not given -> is 50 elements

# Inclusion and exclusion of end element -> endpoint = True (included), endpoint = False (excluded)

a = np.linspace(1,20)  # Includes last element unless it is explicitely excluded
print(a)
# That is by default, ednpoint = True

a = np.linspace(1,10,10)  # can include the last element too, depending upon the step
print(a)


a = np.linspace(1,10,10, endpoint = False)  # explicitely excluding the end element.
print(a)


a = np.arange(1,10) #last element is not included in range ever.
print(a)

##########################################################

# RETURNING step from the linspace().
# We can ask the function to also return the equal spacing it has done to produce the req number of elements.

a = np.linspace(1,10,30,endpoint = True, retstep = True)
print(a)

# A tuple is returned -> array,step

print(a[0])
print(a[1])

##########################################################

# Creating a Scalar array.

a = np.array(42)
print(a)
print(a.ndim)  #Scalars are zero dimensional. 

###############################################

# Creating a 3D array explicitely

a = np.array([ [[1,2,3], [4,5,6]],
               [[7,8,9], [10,11,12]] ])
print(a)
print(a.ndim)

###############################################


# Another way of reshaping of array using shape 'field'
# shape originally returns the shape of the array

a = np.arange(10).reshape(2,5)

print(a.shape)

# Reshaping using shape 'field'
a.shape = (5,2)
print(a.shape)

###############################################


# Some more detailing into 3 D Arrays

B = np.array([ [[111, 112, 113], [121, 122, 123]],
               [[211, 212, 213], [221, 222, 223]],
               [[311, 312, 313], [321, 322, 323]],
               [[411, 412, 413], [421, 422, 423]] ])
print(B.shape) # (4,2,3)

a = B.size

# (rows = 4, Larger_view_columns = 2, Columns_within_columns (Just 1) = 3 (axis2) )
print(a == B.shape[0]*B.shape[1]*B.shape[2])
print()


##################################################################

# Indexing operation on NumPy arrays


# On 1D array
a = np.arange(10)

print(a)

print(a[0],a[1],a[-1],a[-2],a[9])  # Just like other data str in Python( lists and tuples)
print()



# On 2D arrays  (rows and colums start from 0 index)

a = np.arange(4).reshape(2,2)

print(a)

print(a[0][0], a[0][1],
      a[1][0], a[1][1])

print()



# Indexing out the entire row

a = np.arange(4).reshape(2,2)
print(a)

print('Row 0 is :', a[0])

print('Row 1 is :', a[1])



# Another way of indexing

a = np.arange(4).reshape(2,2)

print(a)
print(a[0,0], a[0,1],        # a[0][0] == a[0,0]
      a[1,0], a[1,1])


##################################################################


# Slicing operation on Arrays


#On 1-D array
a = np.arange(10)

print(a)

print(a[0:3])  # same as list and tuples in the case of 1-D array

print(a[0::2]) # step part is also valid.

print('copy :',a[:])
print('Beginning to a stop :',a[:6])
print('Start to end :',a[6:])
print('Reverse :',a[::-1])



# On 2-D array

# The syntax goes like this -> a[beginning_row : end_row,  beginning_column : end_column]

a = np.array([ [1,2,3],
               [4,5,6] ])

print(a)
print(a.ndim)

print(a[0: , 1:])       # All rows are selected, and Column 1 and 2 are selected. The overlap part is sliced always.

print()
print(a[1:, 0:])
print()
# If we keep the overlap part in mind, this slicing will appear very easy.

a = np.array([ [1,2,3],
               [4,5,6],
               [7,8,9],
               [10,11,12]])
 
print(a)    

print('Get me the 1st column only : a[:, 0:1] \n',a[:, 0:1])


print('Get me the 2nd column only : a[:, 1:2] \n',a[:, 1:2])


print('Get me the 1st row only : a[0:1, :] \n',a[0:1, :])

print('Get me the 2nd row only : a[1:2, :] \n',a[1:2, :])


# NOTE - Whenever you need only a particular row -> the row is set, and all columns are needed
# Same case when a particular column is needed, you need all rows and column is set.

# NOTE - When slicing, column and row tabulation is maintained while printing.
# That is row looks like row and column vector looks like column vector.


# More slicing
a = np.array([ [1,2,3],
               [4,5,6],
               [7,8,9],
               [10,11,12]])
 
print(a)   

print('Overlap of 2nd row to end and 2nd column to end : \n',a[1:, 1:])

# Here when I am saying 2nd row and 2nd column it is starting from 1
# But during slicing, we take it from 0. (Row index and column index)



# More complex slicing -> When step is included

a = np.array([ [1,2,3],
               [4,5,6],
               [7,8,9],
               [10,11,12]])
 
print(a)   

print(a[::2, ::2])  # All rows and all column taken but at a step of 2. So row 0 and 2. Column 0 and 2. Then overlap.


# Slicing and indexing of 3D arrays is too complex, so we are not going into it.


############################################################################################

# Modifying an Array

# 1-D array
a = np.arange(10)
print(a)

a[2] = 45

a[-1] = 100

print(a)


# 2-D array
a = np.arange(10).reshape(2,5)
print(a)

a[0][4] = 45  # or a[0,4] = 45

a[1][2] = 100 # or a[1,2] = 100

print(a)

print()
##################################################################

# NOTE - If we just change a slice of Python list, the original list remains unmodified.

a = [1,2,3,4,5,6,7,8,9]

sliced = a[2:6]

print(sliced)

sliced[0] = 45
sliced[3] = 100

print(sliced)
print(a)


print()

# But in NumPy arrays, if we change the slice, the original array changed too, 
# this is becasue the NumPy array is stored contiguously (one continuous mem block).

a = np.arange(10).reshape(2,5)

sliced = a[:, 1:]

print(a)
print(sliced)

sliced[0,2] = 45    # Modifying the sliced array
sliced[1,3] = 100

print(sliced)

print(a) # original array also got modified -> the elements which were changed in sliced, got changed in original too.


#######################################################################################

# Memory Address checker ->np.may_share_memory(ar1,ar2)

# If 2 arrays share same memory block, it will return True, else False.

# In the upper example we have a and sliced who share same memory block.

print(np.may_share_memory(a,sliced)) # True


# Lets see if we take a copy of an array and work upon it, do we see any modification on the original one.

a = np.arange(10).reshape(2,5)

b= a[:, :]
print()
print(np.may_share_memory(a,b))
b[0,0] = 45
b[1,1] = 100

print(b)
print(a)

# NOTE - Even after taking a copy, the original array is changed.
# So beware of this.


#######################################################################################



