''' Write a program that examines three variables x, y, and z
and prints the largest odd number among them. If none of them are odd, it
should print a message to that effect.''' 


x = int(input("First Integer : "))
y = int(input("Second Integer : "))
z = int(input("Third Integer : "))

if x%2 == 0 and y%2 == 0 and z%2 ==0:
    print("None of them are odd!")

elif  x%2 != 0 and y%2 != 0 and z%2 != 0:
    if x>y and y>z:
        print(x,"is largest odd")
    elif y>z:
        print(y,"is largest odd")
    else:
        print(z,"is largest odd")

elif x%2 != 0 and y%2 != 0:
    if x>y:
        print(x,"is largest odd")
    else:
        print(y,"is largest odd")

elif x%2 != 0 and z%2 != 0:
    if x>z:
        print(x,"is largest odd")
    else:
        print(z,"is largest odd")

else:
    if y>z:
        print(y,"is largest odd")
    else:
        print(z,"is largest odd")




''' Write a program that asks the user to input 10 integers, and
then prints the largest odd number that was entered. If no odd number was
entered, it should print a message to that effect.'''


# Lets do this using list and for loop.

my_list = []

for i in range(10):
    a = int(input("Give me number"))
    
    if a % 2 != 0:
        my_list.append(a)
        
if len(my_list) != 0:
    print("The largest odd is",max(my_list))
else:
    print("No odds")
            
    
    
        
    