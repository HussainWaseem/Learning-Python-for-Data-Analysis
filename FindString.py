''' In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.

Sample Input:
ABCDCDC
CDC

Sample Output:
2 '''

my_str, sub = input(), input()
count = 0

while sub in my_str:
    i = my_str.find(sub)  # find() returns the index where the substring is found.
    my_str = my_str[:i] + my_str[i+1:] # I'll rupture the counted substring and
                                      # check again if I have more copies.
    count += 1

print(count)

# str.find(str, [start_index=0], [end_index=len(string)])
# returns index if found.
# returns -1 if not found.

#--------------------------------------------------------------------------

string = input("Give me a string : ")
substr = input("Give me the key : ")
cnt = 0
for i in range(len(string)):
    if string[i:].startswith(substr):  # Sequential seraching one letter after another.
        cnt += 1
print(cnt)