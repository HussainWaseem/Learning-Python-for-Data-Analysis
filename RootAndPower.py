''' Write a program that asks the user to enter an integer and
prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
to the integer entered by the user. If no such pair of integers exists, it should
print a message to that effect.'''

x = int(input("Enter an Integer : "))
root = 0
pwr = 1
count = 0


while (root**pwr < abs(x) and 0 < pwr < 6):
    while (0 < pwr < 6):
        if root**pwr == abs(x):
            print("root is",root,"power is",pwr)
            count += 1
            
        pwr += 1
    root += 1
    pwr = 1

if count == 0 and abs(x) != 0:
    print("No root-power pair exists!")
    
# Keeping root each each level until condition is exhausted.
# For each root level, checking for power 1 to 5 both inclusive.
# printing all possible root , power pairs.

# We are also checking wether for any number if under while is executed or not.
# if not then we are counting.

# After exiting while we are checking if we have not counted.
# That means the if was not executed.
# no root-power pair found.

        
if x == 0 or x == -0:
    print("root is 0 , power is 1,2,3,4,5")




    


