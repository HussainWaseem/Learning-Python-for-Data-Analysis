

# We are getting dates for keys
L = [line.split(',')[0] for line in open('date.txt') ]

print(L)


# We are getting nest lists, each lists containing all temps for a date.
temp_list = [line.strip().split(',')[1:]for line in open('date.txt')]
print(temp_list)

print()



#calculating avg
avg = []

for i in range(len(temp_list)):
    total = 0
    for each in temp_list[i]:
        total+= float(each) # total = total + f(e)
    avg.append((total)/len(temp_list[i])) 

print(avg)
    

d = {L[i]:(temp_list[i],avg[i]) for i in range(len(L))}

print(d)


