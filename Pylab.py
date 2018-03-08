# roll number list
L = [x.split(',')[0] for x in open('rollnumb.csv')]
del L[0] # deleting the header
print(L)
L2 = []



# entire row list by stripping
for i in open('rollnumb.csv'):
    a = i.strip()
    y =a.split(',')
    L2.append(y)
del L2[0] # deleting the first header row
print(L2) #nested list, where each inner list is a repr of a row.
    

# creating a marks list (conv into int)
L3 = []
for e in range(len(L2)):
    L3.append(int(L2[e][2]))
    L3.append(int(L2[e][3]))
    L3.append(int(L2[e][4]))
print(L3)


# Creating an avg list
avg = [(sum(L3[i:i+3]))/3 for i in range(0,len(L3),3)]
print(avg)

# dict created
d = {L[i]:avg[i] for i in range(6)}
print(d)


