''' Towers of Hanoi Problem using Recusion '''
# This problem can be elegantly solved using Recursion but is very tough to solve using iteration.


# Simple you can take n slices. 
# Base case is = If there is one slice, you can move it freely from source to end.
# Recursive cases = Case 1 = Put the n-1 slices from Source to middle peg.
#                   Case 2 = Put the left slice from source to end peg. (This slice is the largest slice).
#                   Case 3 = Put the n-1 slices from middle to end peg. You're done.


def Move(source,end):
    print('Move from ' + str(source) + ' to ' + str(end)) # This is a func() to move a single slice form s -> end.
    
def Towers(N,first,last,middle):
    if N == 1:
        Move(first,last)               
    else:
        Towers(N-1,first,middle,last)  # Moving n-1 chunks from first to middle peg.
        Towers(1,first,last,middle)    # Moving the largest left slice to the last peg.
        Towers(N-1,middle,last,first)  # Moving the n-1 chunks from middle to the last peg.

Towers(4,'P1','P3','P2')