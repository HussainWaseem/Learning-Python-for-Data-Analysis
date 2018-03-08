''' Sq using iteration'''

# squaring = n^2 = Adding n, n times. (times = iteration, How many iterations = n times)
#                                       ( what is n? n is the number itself)

number = int(input("Give number to be squared : "))
iterator = abs(number) # we have to iterate n times.
answer = 0
                          # iterator is a kind of decrementing function. 
                          # we initialized it outside loop ->> We set a terminating condition ->> We change it 
                          #within the loop.
while(iterator != 0):
    answer += abs(number)
    iterator -=1

print(" The square of the number is",answer) # This will work for 0
                                            # Even though the while doesnot.

 
# We are taking absolute(x) because if not taken
# Loop will never stop. 
# Iterator will go farther away from 0.
# Since iterator is set to number.
# if number is negative and iterator is -- .
