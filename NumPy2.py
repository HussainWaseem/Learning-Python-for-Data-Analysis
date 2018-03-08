# Deep Copying of NumPy arrays -> copy() method of arrayObj

import numpy as np

a = np.arange(10).reshape(2,5)
print(a)

b = a[:, :]
print(np.may_share_memory(a,b))  # This type of copying is not copying as they still share same memory.

print()


# Using copy method of arrayObj

a = np.arange(10).reshape(2,5)
b = a.copy()

print(np.may_share_memory(a,b))   #Now they don't share memory.
# copy() method explicitely creates a copy of an array at different memory location.


# Now if we modify either of them, they don't change each other.

a[0,0] = 100
print(a)
print(b) #b remains unchanged.
                                
# There is an optional parameter called order
# It signifies the order in which the array is stored in the memory.
# if order = 'C' -> it means row wise operations will be faster.
# if order = 'F' -> it means column wise op will be faster.
# Both are contiguous.

##################################################################################                               



# More on identity matrix

# 2 ways of creating an identity matrix -> np.identity() and np.eye()
# np.identity() is simple.
# np.eye() has more paramters which give more functionalities to it.


a = np.identity(4)  # by default the dtype is float
print(a)


a = np.identity(4, dtype = int)  # can be changed to int
print(a)


# This is all about np.identity(n, dtype) -> very simple, dtype is optional



a = np.eye(4)   # main diagonal identity matrix
print(a)


a = np.eye(4, dtype = int)
print(a)


# More feautres of np.eye() -> creating a upper diagonal, lower diagonal, main diagonal identity matrix.

# optional paramter -> k (decide the diagonal) -> 0 = main D,      +1 = Upper D,      -1 = Lower D
# k = 0 by default

a = np.eye(4,k=0, dtype = int)
print(a)

a = np.eye(4,k=1, dtype = int)
print(a)


a = np.eye(4,k=-1, dtype = int)
print(a)

# any other value of k, and the matrix will become 0 matrix.




# To create a Non Square identity matrix

a = np.eye(4,10, dtype = int)  
print(a)

# np.eye() syntax ->  np.eye(numb_of_rows,   numb_of_columns = None,  k = 0,  dtype = float64 )


# by default, np.eye() creates a square identity matrix with main diagonal and float.

 
####################################################################################################

# NumPy exercises

# =============================================================================
# 1) Create an arbitrary one dimensional array called "v".
# 
# 2) Create a new array which consists of the odd indices of previously created array "v".
# 
# 3) Create a new array in backwards ordering from v.
# 
# 4) What will be the output of the following code:
# 
#    a = np.array([1, 2, 3, 4, 5])
#    b = a[1:4]
#    b[0] = 200
#    print(a[1])   #  answer is 200
#    
# 5) Create a two dimensional array called "m".
# 
# 6) Create a new array from m, in which the elements of each row are in reverse order.
# 
# 7) Another one, where the rows are in reverse order.
# 
# 8) Create an array from m, where columns and rows are in reverse order.
# 
# 9) Cut of the first and last row and the first and last column.
# 
# =============================================================================
print()  

# Q 1 to Q 3
v = np.arange(10)

print(v)
new = v[1::2]  # new has all the odd indices of v

print(new)

new_2 = v[::-1]
print(new_2)



# Q 5 to Q 9
m = np.arange(10).reshape(2,5)
print(m)

row0 = m[0]
rev_row0 = row0[::-1]

row1 = m[1]
rev_row1 = row1[::-1]

reverse_row = np.array([rev_row0,
                        rev_row1])
print(reverse_row)


# Shortcut to perform reversing of an entire array by row.
print(m[::, ::-1 ]) # All columns reversed. But the elements of each row are reversed.

# Reversing all rows
print(m[::-1, :: ]) # But elements of each column are reversed.

#Reversing columns and rows
print(m[::-1, ::-1 ])


new_ar = np.arange(20).reshape(5,4)
print(new_ar)

# Removing 1st and last row and 1st and last column, slicing the rest.

print(new_ar[ 1:4, 1:3])

#or
print(new_ar[ 1:-1, 1:-1])


########################################################################################

print()

# Changing all the elements of an array to same

a = np.arange(10)

print(a)

a[:] = 20
print(a)

# Since we know that this is not a copy in the lang of NumPy the original array is changed.

########################################################################################


# Like arrayObj of numpy class. We have dtypeObj of numpyclass.


# With the aid of dtype we are capable to create "Structured Arrays", - also known as "Record Arrays".
# The structured arrays provide us with the ability to have different data types per column.


# It has similarity to the structure of excel or csv documents.


i16 = np.dtype(np.int16)  # We created a data-type object of int16.

print(i16)
a = np.array([ [1.6, 2.2, 3.4],
              [4.54, 5.9, 6.2],
              [7.1, 8.25, 9.12] ], dtype = i16)

print(a)


# ndarrays are homogeneous data objects, i.e. all elements of an array have to be of the same data type.


# Creating a record-data-type object for this data -:
# =============================================================================
# 
# Country	       Population Density	     Area	     Population
# Netherlands	    393	                  41526	     16,928,800
# Belgium	       337	                     30510	     11,007,020
# United Kingdom	256	                     243610	     62,262,000
# Germany	       233	                     357021	     81,799,600
# Liechtenstein	205	                     160	     32,842
# Italy	       192	                     301230	     59,715,625
# Switzerland	   177	                     41290	     7,301,994
# Luxembourg	   173	                     2586	     512,000
# France	      111	                     547030	     63,601,002
# Austria	      97	                     83858	     8,169,929
# Greece	      81	                     131940	     11,606,813
# Ireland	      65	                     70280	     4,581,269
# Sweden	      20	                     449964	     9,515,744
# Finland	      16	                     338424	     5,410,233
# Norway	      13	                     385252	     5,033,675
# =============================================================================



dt = np.dtype([('density', np.int32)])  #density is the column name

c1 = np.array([(393,),(337,),(256,)], dtype = dt)  # Note here we made entires as singleton tuples.
# Any other type of entries will show an error.

print(c1)
print(type(c1))
print(c1['density'])  # Will return the column array


print(type(c1['density']))

# Both are ndarrayObj but their representation is different.

# Now creating another record obj

dt2 = np.dtype([('country', 'S20'), ('density', np.int32), ('area', np.int32), ('population', np.int32)])
population_table = np.array([
    ('Netherlands', 393, 41526, 16928800),
    ('Belgium', 337, 30510, 11007020),
    ('United Kingdom', 256, 243610, 62262000),
    ('Germany', 233, 357021, 81799600),
    ('Liechtenstein', 205, 160, 32842),
    ('Italy', 192, 301230, 59715625),
    ('Switzerland', 177, 41290, 7301994),
    ('Luxembourg', 173, 2586, 512000),
    ('France', 111, 547030, 63601002),
    ('Austria', 97, 83858, 8169929),
    ('Greece', 81, 131940, 11606813),
    ('Ireland', 65, 70280, 4581269),
    ('Sweden', 20, 449964, 9515744),
    ('Finland', 16, 338424, 5410233),
    ('Norway', 13, 385252, 5033675)],
    dtype=dt2)


print(population_table[:4])

print(population_table.ndim)

#np.int32 == 'i4'

# 'S20' == binary code strings.
# np.unicode,20 will make the strings unicode and an extra b in output will be removed.

# Here 20 is the str size. 


dt2 = np.dtype([('country', np.unicode,20), ('density', 'i4'), ('area', 'i4'), ('population', 'i4')])
population_table = np.array([
    ('Netherlands', 393, 41526, 16928800),
    ('Belgium', 337, 30510, 11007020),
    ('United Kingdom', 256, 243610, 62262000),
    ('Germany', 233, 357021, 81799600),
    ('Liechtenstein', 205, 160, 32842),
    ('Italy', 192, 301230, 59715625),
    ('Switzerland', 177, 41290, 7301994),
    ('Luxembourg', 173, 2586, 512000),
    ('France', 111, 547030, 63601002),
    ('Austria', 97, 83858, 8169929),
    ('Greece', 81, 131940, 11606813),
    ('Ireland', 65, 70280, 4581269),
    ('Sweden', 20, 449964, 9515744),
    ('Finland', 16, 338424, 5410233),
    ('Norway', 13, 385252, 5033675)],
    dtype=dt2)


print(population_table[:4])


# Accessing individual columns

print(population_table['area'])  # Access is by tag. 


# All slicing and indexing operations are as usual. Remember in all of these problems array is 1-D.

####################################################################################



# Operator overloading in NumPy arrays ->>Depending upon the operands, the operator behaves differently.


# Addition of a scalar to entire array

a = 5

b = np.arange(10).reshape(2,5)
print(b)
b += a

print(b)


# Similarly Scalar sub, scalar multiplication and exponentiation can be done.

# Similarly Addition, sub and multiplication (component wise) can be done
# a+b, a-b, a*b.
# These operators will behave differently in both the cases.


# dot products of 1-D array
a = np.arange(10)
print(a)
print(a.ndim)

b = np.arange(10)
b[:]  = 2
print(b)
print(b.ndim)

print()

c = np.dot(a,b)  # or a.dot(b)
print(c)
print(type(c)) # returns a scalar

 # If 'a' and 'b' are both scalars or both 1-D arrays then a scalar is returned
 
print(np.dot(3,4)) #dotproduct of scalars.



a = np.array([3])
print(a.ndim)    # Its a 1-D array

a = np.array(3)
print(a.ndim)    # Its a 0-D array or a scalar.


a = np.array([3, -2])
b = np.array([-3, 2])

print(a.dot(b))  # another dot product of 1-D arrays


#################################################################################

# Condition check for dot product of 2-D Arrays

a = np.arange(10).reshape(2,5)
print(a.shape) # returns a tuple determining shape

print(a.shape[-1]) # Last element of tuple (m,n) == n == number of columns

b = np.arange(10).reshape(5,2)
print(b.shape)
print(b.shape[0])
print(b.shape[-2])

# So if a.shape[-1] == b.shape[-2] or b.shape[0] 
# which is actually, m*n == n*m
# Then only dot product is possible.


# So if somewhere we don't dont the shapes of array in the dynamic program.
# We can use these conditions for dot product.


######################################################################

 
# To check for equal arrays ->> np.array_equal(a,b)

a = np.arange(10)
b = np.arange(10)
c = np.arange(10)

print(a == b)  # doesn't works as we wanted. (a == b == c) will not work.
               # This checks the equality of each element and returns the array with bool values.
               
print(np.array_equal(a,b)) # This also takes 2 arguments.
# array_equal returns True if two arrays have the same shape and elements


print(a is b)  # remember is operator checks whether both are same Obj -> have same mem location!
               

######################################################################


# NumPy 2D arrays vs NumPy Matrices -> Are they same? -> Principally yes, but operationally no.

# =============================================================================
# Some may have taken two-dimensional arrays of Numpy as matrices.
# This is principially all right, because they behave in most aspects like our mathematical idea of a matrix. 
# We even saw that we can perform matrix multiplication on them. 
# Yet, there is a subtle difference. There are "real" matrices in Numpy. 
# They are a subset of the two-dimensional arrays. 
# We can turn a two-dimensional array into a matrix by applying the "mat" function. 
# The main difference shows, if you multiply two two-dimensional arrays or two matrices. 
# We get real matrix multiplication by multiplying two matrices, 
# but the two-dimensional arrays will be only multiplied component-wise: 
# 
# =============================================================================
print()
# Array creation -> np.array()
# Matrix creation -> np.mat(array)

# So to create a matrix, We first need to create an array.

a = np.arange(10).reshape(2,5)
print(a)
print(type(a))

a = np.mat(a)
print(a)
print(type(a))

# Representation is same, but class are different.


a = np.arange(10).reshape(2,5)
b = np.arange(10).reshape(5,2)
b[:] = 20

a,b = np.mat(a),np.mat(b)
print(a)
print(b)

print(a*b)  # Here since we are directly using the matrices, Matrix dot product will happen.

print(a.dot(b)) # This also works.

############################################################################


# Logical Operation on arrays -> np.logical_or   np.logical_and

a = np.array([ [True, True], 
               [False, False] ])

b = np.array([ [True, False],
               [True, False] ])


print(np.logical_or(a,b))
print(np.logical_and(a,b))


############################################################################


# Till now whatever operations we applied on 2 different arrays such as a+b, a-b, a**b,a*b etc
# (except Matrix multiplication), we realized that these op are valid only when we apply them
# on arrays of same shape (same m*n).



#BROADCASTING ->> Numpy provides a powerful mechanism, called Broadcasting, which allows to perform
# arithmetic operations on arrays of different shapes. 


# How does it happens? ->> Under certain conditions, the smaller array is "broadcasted"
# in a way that it has the same shape as the larger array.


# It occurs implicitely inside NumPy and we don't need to mention it.


a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

b = np.array([10,20,30])

print(a*b)
print(a+b)
print(b-a)

# The smaller array inside numpy is made like this -> [10,20,30]
                                                    # [10,20,30]
                                                    # [10,20,30]
# And then all the operations are performed.






# Creating arrays -> Via replication -> Stacking arrays.                                                    
B = np.array([[1, 2, 3]]*3) #3 stacks created. # See here the 2-D array is being stacked up
print(B)

B = np.array([[1, 2, 3],
               [4,5,6 ]] * 3)
print(B) 
print(B.ndim) # dimension is not changed, just replication occurs.                                                     
                                                    


############################################################################

# Turning a 1-D vector to a 2-D column vector -> a[:, np.newaxis]


# There is nothing like rows and columns in a 1-D vector. Its just a line.
# In a 2-D vector, the concept of rows and columns come.

a = np.array([1,2,3])
print(a)

b = a[: , np.newaxis]
print(b) # Column vector formed

print(np.may_share_memory(a,b))  # But they share same mem location (NOTE - is opr shows they dont because is opr
                                                                    #  works a bit differently)   

a[1] = 100
print(a)
print(b)
# Changes is seen in both arrays.



# arrayObj.copy() and np.newaxis when used one after the other will create different arrays in diff mem location.
a = np.array([1,2,3])

b = a.copy()

b = b[: , np.newaxis]

print(a)
print(b)

print(np.may_share_memory(a,b))

a[1] = 100
print(a)
print(b) # Changes are independent of each other now.

############################################################################


# Broadcasting in the case of column vector ->>

a = np.array([11,22,33])
print(a)
print(a.ndim)  # Its a 1-D vector

b = a[:, np.newaxis]

c = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])

print(b) #column vector 
print(b.ndim)
print(c) # 2-D array



# Operations between a 2-D array and a 2-D column vector. (b and c here).

print(b*c)
print(b+c)

# Actually behind the scenes b is turning into this ->> [11,11,11]
                                                      # [22,22,22]
                                                      # [33,33,33] and then all the opr are performed.


############################################################################

# Tranpose of an array ->> rows <-> columns

a = np.array([[11,22,33]]*3)
print(a)

b = a.copy().transpose()
print(b)                                                      

############################################################################                                                      
                                                     

# Earlier broadcasting is done between 2 different sized 2-D vectors.
# Also between a 2-D vector and a 2-D column vector.

# But now we will see broadcasting happening between 1-D array and a 2-D array & Column vector.

a = np.array([10,20,30]) #1-D array

b = np.array([[11,22,33],
              [44,55,66],
              [77,88,99]]) #2-D array

print(a+b)

# Behind the scenes, the 1-D array is converted into a 2-D array and looks like - [10,20,30]
                                                                                 #[10,20,30]
                                                                                 #[10,20,30]
                                                                                 
a = np.array([11,22,33]) #1-D array
b = a[:, np.newaxis]

print(b) # 2-D column vector

print(a+b)  

# Here both side broadcasting happens , 1-D array becomes 2-D array -> [11,22,33]
                                                                      #[11,22,33]
                                                                      #[11,22,33]           
# And 2-D column vector became ->  [11,11,11]
                                 # [22,22,22]
                                 # [33,33,33]                                                                     

############################################################################ 

# Right way to create a column vector. 
                                 
a = np.array([1,2,3])             
A = np.array([1,2,3])
print(A.ndim)

b = a[:, np.newaxis]  # This works, first copying and then changing axis.
print(b)

c = A[np.newaxis, :]  # This works too but it converts 1-D array into a row vector. 

print(c.ndim)  # Its now a 2-D array.                              


############################################################################ 


# Concatenating arrays -> np.concatenate((a,b,...), axis = 0)

# By default, it is set to concatenate by columns, we can change it explicitely.



# In 1-D array concatenation, since there is no axis, it works like lists. [1,2,3]*3 = [1,2,3,1,2,3,1,2,3]
a = np.array([1,2,3])

b = np.concatenate((a,a,a))

print(a)
print()
print(b)




# In 2-D arrays

a = np.array([[1,2,3]])

b = np.concatenate((a,a,a)) #concatenation, and 3 rows are stacked up.

print(a)
print()
print(b)


a = np.array([[1,2,3]])

b = np.concatenate((a,a,a), axis = 1) # concatenation by axis = 1. Since there is only 1 row, repetitions happens.

print(a)
print()
print(b)



a = np.array([[1,2,3],
              [4,5,6]])

b = np.concatenate((a,a,a), axis = 1)


print(a)
print()
print(b)


# axis = 0 -> stacking vertically , new rows.

# axis = 1 -> horizontal stacking / repeating.


################################################################################


# Converting 1-D array into row Vector (2-D Array)

a = np.array([1,2,3])
print(a.ndim)
b = a[np.newaxis, :]  # Now it is a 2-D array but a row vector.
print(b.ndim)

# See -> a[(adding a row vector)np.newaxis : (keeping columns same)]

#  a[(keeping rows same) : (adding a column vector)np.newaxis]

################################################################################


# 1-D array -> to 2-D row vector array -> concatenation

a = np.array([1,2,3]) # 1-D array
print(a)

b = a[np.newaxis, :] # 2-D row vector array
print(b)

b = np.concatenate((b,b,b)) # concatenation (stacking new rows)
print(b)


################################################################################

# Concatenating 2 different arrays (All variants -> Num_of_row same for row wise (axis = 1) concat)
                                    # (Num_of_column same for column wise (axis = 0) concat)

a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

c = np.concatenate((a,b))
print(c)

c = np.concatenate((a,b,a)) #concatenation by columns / stacking is done in order.
print(c)


 # c = np.concatenate((a,b),axis = 1) will show an error.Concatenation requires right match of rows when done rowwise.
 
print(c)

c = np.concatenate((b,b), axis = 1) # Repetition
print(c)


a = np.array([1,2,3])
a = a[:,np.newaxis]

b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

# c = np.concatenate((a,b)) -> Will give an error, You can't stack a matrix and a column vector. Column should match
                                # when concatenating column wise.



################################################################################
                                

# NOTE - Broadcasting happens in +, -, *, ** or other similar arithmetic op.
# But it doesn't happens in concatenation.


print()

################################################################################

# Tiling arrays -> np.tile(Array, representation)

# 1. Repeating within itself.

# (When only one element is given for representation, one repetition happens and no stacking)

a = np.array([1,2,3]) #1-D array

b = np.tile(a,2) # repeating a 2 times within itself
print(b)                               
print()
a = np.array([[1,2,3]]) # 2-D array

b = np.tile(a,2) # repeating a 2 times within itself
print(b)                               
print()


# 2. More types of representations (all 2-D) -> stacking and repetitions.


a = np.array([[1,2,3]]) # 2-D array
                              
b = np.tile(a,(2,3))  # Within representation, 1st element is for stacking, 2nd is for repeating.
print(b)  # 2 stacks and 3 repetitions.                             
print()

c = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

d = np.tile(c,(3,2))  #3 stacks and 2 repetitions.
print(d)

print()
################################################################################

# We have created arrays using -> np.array(), np.arange(), np.linspace(), np.zeros(), np.ones(),np.identity(),np.eye()

# 2 Ways to flatten any array -> a.flatten(), a.ravel() -> Converting any n-dim array to 1-D array.

a = np.arange(30).reshape(5,6)

print(a) 

a = a.flatten()
print(a)
print()
################################################################################
# np.tile(a,repr) vs np.concatenate((a,b,cd,...), axis = 0)

# In tile we have only one array and we manipulate that. There is no strict condition.
# In concatenation we have multiple arrays and we glue them along any axis. Row and column matching condition.
# In concatenation, stacking only happens in columns, In rows its repetitions.

# Vector stacking.

# In NumPy column and row stacking in their real sense means something else. 

# In 1-D arrays

a = np.arange(5)

print(a)
print(a)
 
b = np.column_stack((a,a))
print(b)

# What it does it, it returns the column vector (2-D) by making the rows as columns.

print()


# What is actually happening behind the scenes in 1-D array column_stacking.
a = np.arange(5)
a = a[np.newaxis, :]

print(a)
print(a)
 
b = np.concatenate((a,a))
print(b.transpose())






# In 2-D arrays

a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])

print(a)
print(a)

b = np.column_stack((a,a))

print(b)

# In case of 2-D its repetitions, the times a is used.

# Very strange. Yes it is!

# In concatenation -> repetition used to happen in the case of 1-D array, in column_stack, it happens with 2-D arrays.


# Trying column_stack with column vectors.

a = np.arange(5)
b = a[:, np.newaxis]

print(b)
print(b)
c = np.column_stack((b,b))
print(c)

# Just stacked side by side like columns. (column_stack is more realistic for column vectors)
#######################################################################################



# Row_stacking ->


# In 1-D array
a = np.arange(5)
b = np.row_stack((a,a)) # 2 rows are stacked of a in the resultant array which is 2-D.
print(a)
print(a)
print(b)



# In 2-D array


a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])

b = np.row_stack((a,a)) #  2 rows are stacked of a in the resultant array which is 2-D.
print(a)
print(a)
print(b)


# Row stacking works same both both 1-D and 2-D arrays


# Lets try row_stack with row vectors.
a = np.arange(5)
b = a[ np.newaxis,:]

print(b)
print(b)
c = np.row_stack((b,b))
print(c)

# Row stacking works same both both 1-D and 2-D arrays and row vectors (since it is also a 2-D array).


######################################################################################



# Some special column_stacking

# What does a[x] for a 2-D array returns? -> Its row x.

a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])

print(a[0])
print(a[0].ndim)  # It returns a 1-D array

# Remember in column_stack of 1-D arrays, vertical stacking (axis 0 concatenation) and transpose happens.
print(a[0])
print(a[0])
print(a[0])
b = np.column_stack((a[0],a[0],a[0]))

print(b)

######################################################################################


# When to use what?

# 1. When you just want to stack up rows (no matter its a 1D or 2D array) -> use np.row_stack((tuple))

#2. When you want to repeat or stack up rows depending upon your choice (either at a time) using multiple
# arrays -> go for concatenation
# np.concatenate((tuple), axis = 0|1) , axis = 0 will stack up vertically. axis = 1 will repeat.
# Note -> but in 1-D array only repetition occurs.


#3. When you want to broadcast an array explicitely so that it becomes like what you want -> use np.tile(a, repr)

# repr is a tuple, Whose first element determines how many vertical stacks you want, and 2nd element goes for rep.
# This is also helpful if you want to do both at a time (stacking and repetition) which is not possible in concatenate.




######################################################################################

# Floor value of elements of an array

# The floor of the scalar x is the largest integer i, such that i <= x. (such that i is just smaller or eq to x)
# floor values are always integers.

a = np.array([-2.5,-1.5,-3,0.5,1.25,1.45,1.78,2.3,2.1])
print(a)
print(np.floor(a))


######################################################################################


# To get a transpose matrix -> 2 ways (rowx becomes columnx) and vice versa
# 1st way -> b = a.tranpose()
# 2nd way -> b = a.T

a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])

print(a)
print(a.transpose())

print(a.T)


######################################################################################

# More on reshape()


a = np.array([[10,20,30,11],
              [40,50,60,22],
              [70,80,90,33]])

b = a.reshape(4,3)
print(b)

# a.reshape() vs a.resize() -> reshape makes it clear that total size(numb of elements) is not changed.
#                               resize can do any size and will change the total size also.


# reshape from its name stands just for reshaping without changing the size.
# resize from its name stands from changing the size. (and when you change the size, the shape automatically changes)



# np.resize(array,(size))


a = np.array([[10,20,30,11],
              [40,50,60,22],
              [70,80,90,33]])

print(a)
b = np.resize(a,(4,3))
print(b)                  # here we have kept the size intact.


a = np.arange(10)

print(a)
print(np.resize(a,(2,6)))  # We have changed the size and shape both.


# np.resize(array,(size)) and a.resize((size))
#np.resize(array,(size)) returns the new array

# a.resize() doesn't returns anything. it returns None. It modifies the array. The older array no more remains.

a = np.arange(10)
print(a)
a.resize((2,8))
print(a)



a = np.array([[10,20,30,11],
              [40,50,60,22],
              [70,80,90,33]])

print(a)
b = np.resize(a,(8,2))
print(b)                  


# We see that in most of the cases (except 1-D) the repetition starts building up for the new elements due to increased size.


#########################################################################################


# np.resize(array,(size))  vs a.resize((size))


# np.resize(array,(size)) fills with repetition and returns a new array. Old array remains unchanged.

# a.resize((size)) modifies the array itself, returns None and fills the new elements with 0



print()
a = np.array([[10,20,30,11],
              [40,50,60,22],
              [70,80,90,33]])

print(a)
b = np.resize(a,(8,2))  # new elements filled with repetitions.
print(b)                



a = np.array([[10,20,30,11],
              [40,50,60,22],
              [70,80,90,33]])

print(a)
a.resize((8,2))  #new elements filled with 0
print(a)                 


#########################################################################################


# HOW TO CREATE A COLUMN VECTOR DIRECTLY -??

a = np.array([[1],  #column vector (has only 1 column)
              [2],
              [3]])

print(a)

b = np.array([[1,2,3]]) #row vector (has only 1 row)

print(b)



#########################################################################################


# Some equivalent functions -> (in operation)

# a.flatten() == a.ravel()

# np.concatenate((a,b,c,..), axis = 0) = np.vstack((a,b,c..)) , instead of writing axis = 0, you can use just vstack.

# np.concatenate((a,b,c,..), axis = 1) = np.hstack((a,b,c..))   #instead of writing axis = 1, you can use just hstack.


#########################################################################################


#########################################################################################




# Splitting the array into multiple different arrays


# np.split(array,indice or 1-D array, axis = 0)  



# indice(x) = breaking the array into x equal parts, if not possible an error is raised.

# 1-D array instead of an indice = [x,y,z..] = break as [:x],[x:y],[y:z],[z:..],..



a = np.arange(10)  #10 elements
print(a)

print(np.split(a,5))  #breaking a in 5 equal parts.

print(np.split(a,[2,5,7]))  #breaking a using slices as explained above.


# 1-D array can be splitted along axis = 0 only. (Though they don't have any axis)

# 2-D arrays can be splitted around any axis.




a = np.array([[10,20,30,11],
              [40,50,60,22],
              [70,80,90,33],
              [100,110,120,44]])

print(a)
print(np.split(a,2))  # The columns are splitted   
#[[10,20,30,11]
#[40,50,60,22],
#-----------------
#[70,80,90,33],
#[100,110,120,4]] 

print(a)
print(np.split(a,2,axis = 1))  # The rows are splitted   
#[[10,20, | 30,11]
#[40,50,  | 60,22],
#[70,80,  | 90,33],
#[100,110,| 120,4]]


a = np.array([[10,20,30,11],
              [40,50,60,22],
              [70,80,90,33],
              [100,110,120,44]])

print(a)
print(np.vsplit(a,2))  # The columns are splitted   
#[[10,20,30,11]
#[40,50,60,22],
#-----------------
#[70,80,90,33],
#[100,110,120,4]] 

print(a)
print(np.hsplit(a,2))  # The rows are splitted   
#[[10,20, | 30,11]
#[40,50,  | 60,22],
#[70,80,  | 90,33],
#[100,110,| 120,4]]


# Equivalent -> np.split(array,indice|1-D array, axis = 0)  # split by column = np.vsplit()
# np.split(array,indice|1-D array, axis = 1)  # split by row = np.hsplit()
  
#####################################################################################


# Always -> vstack or vsplit is by axis = 0 , by column.

# Always -> hstack or hsplit is by axis = 1 , by row.



 
#####################################################################################

# COMPARING row_stack() and column_stack with vstack() and hstack()



# np.row_stack -> Which does vertical stacking, stacking rows is equivalent to == np.vstack()


a = np.array([[1],
             [2],
             [3]])

print(a)
print(np.row_stack((a,a)))
print(np.vstack((a,a)))
# Exactly the same.




# Now we compare np.column_stack and np.hstack() for 2-D arrays (here is a column vector)
a = np.array([[1],
             [2],
             [3]])

print(np.column_stack((a,a)))
print(np.hstack((a,a)))
# They are same when dealing with column vectors.



# They are same when dealing with 2-D arrays (as both of them signify repeating for 2-D arrays)
a = np.arange(10).reshape(2,5)
print(a)

print(np.column_stack((a,a)))
print(np.hstack((a,a)))


# But when working with 1-D array, both are different.
a = np.arange(10)
print(a)

print(np.column_stack((a,a))) # Does vertical stacking (concatenation by axis = 0) then transpose.
print(np.hstack((a,a))) # Does repeate.


# hstack () is repeating always (no matter what is the dimension of array)
# column_stack does repeating only for 2-D arrays.

#################################################################################
#################################################################################

#################################################################################

#################################################################################

#################################################################################

#################################################################################

#################################################################################







# FANCY INDEXING IN NUMPY -  arrays can be indexed by arrays


# Indexing a 1-D array using a 1-D array
a = np.arange(10)**2

b = np.array([0,1,3,4,8,2])

print(a)

print(a[b])

# What happened? -> b when enclosed in [] represents the indices. And a[b] will return the elements of a 
# placed at the indices of b.
# The array returned will of the size and shape of b always.



# Indexing a 1-D array using a 2-D array
a = np.arange(10)**2

b = np.array([[1 , 2 , 3],
              [4 , 5 , 6],
              [7 , 8 , 9]])

print(a)

print(a[b])


# Here also the same thing happened, elements of a are placed inside b at its indices.
# The array returned will of the size and shape of b always.




# 2-D array1 [2-D array2] -> Instead of each index representing an element, here it represnts rows.

a = np.arange(50).reshape(10,5)

b = np.array([[1 , 2 , 3],
              [4 , 5 , 6],
              [7 , 8 , 9]])

print(a)
print(b)

print(a[b])  # Here the array returned is 3-D since by replacing an element with a row, an extra dimension is added.



# 2-Darray[1-D array] -> Rows are called in place of 1-D array elements(indices).

a = np.array([2,0,1])

b = np.array([[1 , 2 , 3],
              [4 , 5 , 6],
              [7 , 8 , 9]])

print(a)
print(b)
print(b[a])




# What we have seen in fancy indexing till now?
# 1-D array1 [1-D array2] -> elements of array1 went to replace the indices of array2. The final shape and size is
# of array2.

# 1-D array1 [2-D array2] -> elements of array1 went to replace the indices of array2. The final shape and size is
# of array2.





# 2-D array1 [2-D array2] -> rows of array1 went to replace the indices of array2. Extra dimension added due to rows.

# 2-D array1 [1-D array2] -> rows of 2-Darray1 went to replace the indices of array2. No new dimension added. Just
# shifting of order of rows happen.



###################################################################################################

a = np.arange(12).reshape(3,4)
i = np.array( [ [0,1],         # == [[i1,i2],[i3,i4]]
                [1,2] ] )

j = np.array( [ [2,1],        # == [[j1,j2],[j3,j4]]
                [3,3] ] )
print(i)
print(j)
print(a)
print(a[i,j])

#(0,2)  (1,1)   # grouping as (i1,j1), (i2,j2)
                             #(i3,j3), (i4,j4)
#(1,3)  (2,3)

###################################################################################################

# Changing elements of an array in 1 go.

a = np.array([0,10,20,30,40,50,60,70,80,90])
b = [1,3,5,8,9]

print(a[b])  # Normal 1-D to 1-D indexing.

a[b] = 0 # Changing selected elements to 0
print(a)





a = np.array([0,10,20,30,40,50,60,70,80,90])
b = [1,3,5,8,9]

print(a[b])  # Normal 1-D to 1-D indexing.

a[b] = [100,300,500,800,900] # Changing selected elements to new values
print(a)







a = np.array([0,10,20,30,40,50,60,70,80,90])
b = [1,3,5,8,9]

print(a[b])  # Normal 1-D to 1-D indexing.

a[b] += 1 # Changing selected elements to new values using augmented operation (here the array b is augmntd with +1)
print(a)


###################################################################################################
 


# INDEXING WITH BOOLEAN ARRAYS  -> returns elements/rows with True correspondance.


# 1-D with 1-D.

a = np.arange(10)*10
print(a)

b = a > 40  # generating a boolean array of same size of a
print(b)

print(a[b]) #Indexing using boolean array

# [ 0 10 20 30 40 50 60 70 80 90][False False False False False  True  True  True  True  True]
# Retuns those elements which correspond to True indices.



# 2-D with 1D


a = np.arange(10)*10
print(a)

b = a > 40  # generating a boolean array of same size of a (1-D array)
print(b)


c = np.arange(50).reshape(10,5)*2 # generating a 2-D array

print(c)

print(c[b]) ##Indexing using boolean array

## Retuns those rows which correspond to True indices.

# NOTE - The number of rows should match the number of elements in boolean array. (otherwise error).

# Just like in 1-D array, each elements corresponds to each bool value from beginning to end.
# Similarly in 2-D array, each row corresponds to each bool value from beginning to end.


print()
print()
print()
# Changing values who are true can be done here too.


# In 1-D arrays


a = np.arange(10)*10
print(a)

b = a > 40  # generating a boolean array of same size of a (1-D array)
print(b)


a[b] = 0  # Subtituting values (elements which correspond to true are now substituted to 0)

print(a) 

print()

print()





a = np.arange(10)*10
print(a)

b = a > 40  # generating a boolean array of same size of a (1-D array)
print(b)


c = np.arange(50).reshape(10,5)*2 # generating a 2-D array

print(c)

c[b] = 0  # Subtituting values (Rows which were true are now substituted to 0)

print(c) 


######################################################################################




