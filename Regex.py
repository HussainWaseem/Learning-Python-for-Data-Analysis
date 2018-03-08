# Regular Expressions

#within compile we put regular expression.

import re

string = 'abcdefghijkl1234582'
string2 = 'abcd1234efgh2058tyui9632'

reg_ex = '[a-z]+[0-9]+'

#pattern is an object which can be used to do a single foremost match, search, findall matches,etc.

# Compilation is done so that the reg_ex can be converted to byte code. Since it is a prog lang of its own.

# match object created at the end has some useful methods.
# start which tells where the match started.
# end which tells where the match ended

# span tells the start and end span

# group gives the matched pattern.

pattern = re.compile(reg_ex)  # This generates the object which has the pattern we are searching.

matchobj = pattern.match(string)  # We pass in our own string in which the pattern is to be searched.
                                   # match() will only search if the string starts with the pattern. 
                                   # else matchobj will be Nonetype.

print(matchobj.start())


print(matchobj.end())


print(matchobj.span())


print(matchobj.group())



searchobj = pattern.search(string2)   # search is another method of pattern obj. And it searches not from the start
                                       # but the entire string from the start and gives out the 1st pattern matched.

print(searchobj.start())


print(searchobj.end())



print(searchobj.group())




findList = []

findList = pattern.findall(string2)  #findall() method of pattern obj finds all the matches and return a list of matches.

print(findList)



findIterobj = pattern.finditer(string2)

for i in findIterobj:
    print(i)
    


#############################################################################
    
# Escape Sequencing and Raw Strings.
    
numb = '325.111.021'
anyn = '123a456b789'

pattern = re.compile('\d\d\d.\d\d\d.\d\d\d')

matchObj = pattern.match(numb)
matchObj2 = pattern.match(anyn)

print(matchObj.group())
print(matchObj2.group())
# Here the same regexpression matched both the strings. Why? Because dot (.) means any character in regex terms.


# So we need to use backslash with every dot or some other special char such as + and * to escape them.
# These - + and other special char likes ( ) } { ] [ etc are called meta characters in reg ex. 
# They carry a meaning of their own.

# If you want to rake them literally. Put a backslash with them at the beginning.

# If you want to escape any python escape seq like \n, \t, \r, \b then use a raw string.




pattern = re.compile('\d\d\d\.\d\d\d\.\d\d\d') 

matchObj = pattern.match(numb)
matchObj2 = pattern.match(anyn)

print(matchObj.group())

print(matchObj2) #Returns None because pattern has not matched for 123a456b789.



############################################################################################



numb1 = '325-123-856'
numb2 = '123.234.569'
numb3 = '123*235*965'

# I want to write a regex that matches numb1 and numb2 but not numb3.

# Using sets! [] It matches for that character anything which is inside that set. 

pattern = re.compile('\d\d\d[.-]\d\d\d[.-]\d\d\d')

# Remember inside a set , things are read literally so don't need any escaping sequences.



matchObj1 = pattern.match(numb1)

matchObj2 = pattern.match(numb2)

matchObj3 = pattern.match(numb3)

print(matchObj1.group())  #Matches
print(matchObj2.group())  #Matches
print(matchObj3)          # Doesn't match. None returned.


# NOTE - Set always matches ONLY one character.

# [a-b] specifies a range. Will match a character for that range.


example = '5acbf'

example2 = '7acbf'

pattern= re.compile('[0-9].*')  

print(pattern.match(example).group())


print(pattern.match(example2).group())

# Done!


# [^xyz] = It negates whatever is inside the set.


#############################

# Groups in Regex.

#They are different from sets as in we can check for multiple characters at once.


s = 'Mr Tim'
y = 'Mr. Cook'
z = 'Ms. Jane'
q = 'Mrs. Haley'


pattern = re.compile('M(r|s|rs).?\s\w*')

matchObj = pattern.match(s)
matchObj1 = pattern.match(y)
matchObj2 = pattern.match(z)
matchObj3 = pattern.match(q)


print(matchObj.group())
print(matchObj1.group())
print(matchObj2.group())
print(matchObj3.group())


# We see here that inside a group we matched for rs too. Which is actually 2 chars, but matching at once possible
# only with groups and not sets.


# Anchors in reg ex  = ^ , $, \b and \B

#####################################
# These are called Quantifiers or Meta characters.  These and * + ?. They can't be used individually . They are used with some regex.

# {x} = x number of times 
#              {x,y} = Min x and Max y numbe of times
#                     {x,}  = Min x and Max any number of times.
#  {,y} = Min any and Max y number of times



###########################################


# Write a regex that matches all these 3 URls.

url1 = 'CoreyMSchafer@gmail.com'
url2 = 'corey.schafer@university.edu'
url3 = 'corey-321-schafer@my-work.net'


pattern = re.compile('[a-zA-Z0-9.-]+@(gmail|university|my-work)\.(com|edu|net)')

matchObj = pattern.match(url1)

matchObj2 = pattern.match(url2)

matchObj3 = pattern.match(url3)


print(matchObj.group())

print(matchObj2.group())
print(matchObj3.group())

###############################################


# Write a regex to match these urls.

url4 = 'https://www.google.com'

url5 = 'http://coreyms.com'

url6 = 'https://youtube.com'

url7 = 'https://www.nasa.gov'



pattern = re.compile('https?://(.+)')

matchObj = pattern.match(url4)

matchObj2 = pattern.match(url5)

matchObj3 = pattern.match(url6)

matchObj4 = pattern.match(url7)


print(matchObj.group(1))

print(matchObj2.group(1))
print(matchObj3.group(1))
print(matchObj4.group(1))


####################################


# pattern object also has another method called sub which stands for substitution

# It can use backreferencing to substitute text.


# Referencing to above example.


pattern = re.compile('https?://(www\.)?(\w+)(\.\w+)')

# Here we have formed groups. To which we can have an access.

matchObj = pattern.match(url4)

matchObj2 = pattern.match(url5)

matchObj3 = pattern.match(url6)

matchObj4 = pattern.match(url7)


print(matchObj.group(1),matchObj.group(2),matchObj.group(3))

print(matchObj2.group(1),matchObj2.group(2),matchObj2.group(3))

print(matchObj3.group(1),matchObj3.group(2),matchObj3.group(3))

print(matchObj4.group(1),matchObj4.group(2),matchObj4.group(3))

# group() also takes in multiple parameters and returns a tuple in that case.

print(matchObj.group(1,2,3))  # returns a tuple of all groups mentioned. 
 

print()

substitute = pattern.sub(r'\\2\\3', url5)   # Note during backreferencing always use r to make it a raw string.
# double backslashes are necessary because these \2 and \3 mean some octal special char in Python.

#So we need to escape them and tell them its not of Python built in but of regex.

# Here when Python searches for Pattern in url5, it replaces the entire url5 with group2 group3 of matched pattern 
# in url5.

print(substitute)

###############################################


# Note findall () method of pattern, it prepares of list of all matches! But if we are using a group in our regex,
# then it just uses that group as the elements of the list and not the entire matched pattern.


# So Beware of using findall and groups in regex together until needed.

####################################################
print()



# Using flags in regex.

# re.IGNORECASE or re.I

stringEx = 'sTaRt'   # When the data is mixed with with cases.

pattern = re.compile('start', re.IGNORECASE)

print(pattern.match(stringEx).group())


pattern = re.compile('start', re.I)

print(pattern.match(stringEx).group())


########################################


# pattern.split() method = Splits the string at the matched pattern. Returns the list of elements. Pattern is lost.

newex = 'abc123bcd123efg'


pattern = re.compile('\d{3}')

splitObj = pattern.split(newex)

print(splitObj)


######################################



# Why to use raw strings while defining a regular expression? (To escape Python built in escape seq.)

# -- To make python understand that we are not using Python' special escape sequences, rather it is a literal that 
#  we pass into reg ex.

# So use r everywhere. It will save you from common pitfalls.

# There are no disadvantages of using r.
# Eg \1 and \2 ... are octal escape sequences in Python built in.

# But they are also used as groups referencing while using pattern.sub().

# In that case you can do 2 things.

# escaping them purposefully. \\1, \\2, ...

# or just using r outside the string.

# That will tell Python to not take these as built ins. (or to escape them)

# NOTE - r escapes only the escape sequences. And not . + etc.

# To escaping . or + use \. and \+

#############################################


# Special use of caret inside the set.

# USed for negation.


# The only other special character inside square brackets (character class choice) is the caret "^".
# If it is used directly after an opening sqare bracket, it negates the choice. 

#[^0-9] denotes the choice "any character but a digit". 

#The position of the caret within the square brackets is crucial. 

#If it is not positioned as the first character following the opening square bracket, it has no special meaning. 

# [^abc] means anything but an "a", "b" or "c" 
# [a^bc] means an "a", "b", "c" or "a^".


#################################################

print()

# Another Method of not using compiling and compiling on the fly. This is common with all re methods.

another = '9865-1206'

matchObj = re.match('\d{4}-\d{4}', another)  # Here we have not used re.compile. And have passed the reg ex directly.

print(matchObj.group())


print()

# Using flag too.

new_an = 'sTaRt'

matchObj = re.match('start',new_an, re.I)

print(matchObj.group())


#####################################################################


# To capture the entire string. Using ^ and $. It means if it starts with something and ends with something. Get that.

searchObj = re.search(r'a.+d','and he is the end')

print(searchObj.group())


# or 

searchObj = re.search(r'^a.+?d','and he is the end')  # Using ? turned it into Non Greedy

print(searchObj.group())



# Greedy Concept - * and + are greedy operators. They always match the largest string.

# Also re.search and re.match are greedy methods. They match the largest string.

# But using ? infront of greedy operators makes it non Greedy. 




########################################


searchObj = re.search(r'^a$', 'a')

print(searchObj.group())  #Match done


print()

searchObj = re.search(r'^a$', 'anna')

print(searchObj)  #No match. Why??  Because we are only checking for a single character a.


print()

searchObj = re.search(r'^a.*a$', 'anna')  #Now it matched. because we are taking any number of char in string
                                          # starting with a and ending with a.

print(searchObj.group())




#############################################

print()

# Some exceptions with the sets - Taking sets as literal.


searchObj = re.search(r'\[hello\]', 'hello')  # If we put backslashes like these, regex will take the set as Literal.
                                                #It matches if the string has [hello] 

print(searchObj)




searchObj = re.search(r'\[hello\]', '[hello]')

print(searchObj.group())


###############################################

print()

# Quantifiers dealing with 0 or more will always return something. Either an empty string if 0 is matched.
# else the matched pattern.


searchObj = re.search(r'\d*', 'abcd')

print(searchObj)
print('The group is',searchObj.group())


#######################################


# Matching boundary lines strings.


# \b denotes word boundary. This means it will select the pattern if it is NOT surrounded by word character.
# Word characters = \w = [a-zA-Z0-9_]

searchObj = re.search(r'\bhello\b', 'hello') 

print(searchObj)  # Matched. Since hello is not surrounded by any Word character on either of its side.




searchObj = re.search(r'\bhello\b', 'hello there')  # Matched, since space is not a Word Char.

print(searchObj)





searchObj = re.search(r'\bhello\b', 'hello_there') 

print(searchObj)  # Not matched. Since _ is a Word char.




searchObj = re.search(r'\bhello\b', 'hello-there') 

print(searchObj) # Matched, - is not a Word char.


###############################################################
print()

# \B does its opposite. It matches if the string is surrounded by Word Char.


searchObj = re.search(r'\Bhello\B', 'hello') 

print(searchObj)  # Not Matched. Since hello is not surrounded by any Word char.


searchObj = re.search(r'\Bhello\B', '_hello_there') 

print(searchObj)  # Matched.



# Anchors (means attachment) belong to the family of regex tokens that don't match any characters,
# but that assert something about the string or the matching process.

# These \b, \B, ^, $ are called called Anchors.



# These *, + , ?, {} etc are called Quantifiers, They are used for repetitions.

# * and + are greedy Quantifiers. They always match the largest string possible.

# Applying ? ahead of them makes them Non Greedy/Lazy quantifiers.

# Then they match for the shortest string possible.
###########################################################

print()
# Flags also work with sets or we call them classes.


searchObj = re.search(r'hello', 'Hello There', re.I)

print(searchObj)

print(searchObj.group())
print()




searchObj = re.search(r'[a-z]', 'Hello There', re.I)

print(searchObj)

print(searchObj.group()) # returns H. since we are checking just for one char.
print()




searchObj = re.search(r'[a-z]+', 'Hello There', re.I)

print(searchObj)

print(searchObj.group())  # Now the entire Hello, since we searched for repetitions.



################################################################

print()


# Making regular expressions more readable.
# re.VERBOSE mode.


uuid = 'c2d1039e-0d9e-4e45-a253-151be5e433c3'
searchObj = re.search(r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}', uuid, re.I)

print(searchObj)

print(searchObj.group()) # It matched since the reg ex is true for the uuid.

print()


uuid = 'c2d1039e-0d9e-4e45-a253-151be5e433c3'
searchObj = re.search(r'''[a-fA-F0-9]{8}
                          -[a-fA-F0-9]{4}
                          -[a-fA-F0-9]{4}
                          -[a-fA-F0-9]{4}
                          -[a-fA-F0-9]{12}''', uuid, re.I)  # Using a Multi lined reg ex to make it more readable.
                                                              # Will it work? No!! Why??
                                                              # Because reg ex also take these spaces and new lines
                                                              # as their part.
                                                              # So they search for spaces and \n too in the uuids.

print(searchObj) # Doesn't match


# So here comes the role of re.VERBOSE which tells reg ex parser to ignore spaces and new lines in regex.



print()


uuid = 'c2d1039e-0d9e-4e45-a253-151be5e433c3'
searchObj = re.search(r'''[a-fA-F0-9]{8}
                          -[a-fA-F0-9]{4}
                          -[a-fA-F0-9]{4}
                          -[a-fA-F0-9]{4}
                          -[a-fA-F0-9]{12}''', uuid, re.I | re.VERBOSE)



print(searchObj)

print(searchObj.group())  # Matches ! And makes the reg ex looks easy to read.






# re.VERBOSE also allows you to put comments inside your reg ex.
# Also re.VERBOSE is same as re.X


print()


uuid = 'c2d1039e-0d9e-4e45-a253-151be5e433c3'
searchObj = re.search(r'''[a-fA-F0-9]{8}    # 8 digit hexa decimals
                          -[a-fA-F0-9]{4}   # 4 digit hexa decimals
                          -[a-fA-F0-9]{4}   # 4 digit hexa decimals
                          -[a-fA-F0-9]{4}   # 4 digit hexa decimals
                          -[a-fA-F0-9]{12}  # 12 digit hexa decimals''', uuid, re.I | re.X)  # | is called piping.



print(searchObj)

print(searchObj.group()) # MAtched.


####################################################################################

print()

# Just match the Airport codes Which is of the form [A-Z] 3 times in a row. No more No less.



air1 = 'SAN' 

air2 = 'SANO'

air3 = 'SANO123'

pattern = re.compile('[A-Z]{3}')

matchObj = pattern.match(air1)

matchObj2 = pattern.match(air2)

matchObj3 = pattern.match(air3)

print(matchObj)

print(matchObj2)

print(matchObj3)


# Actually it finds a match for all. But we wanted just to match that airport Id which has only [A-Z] 3 times. 
# No more no less.


air1 = 'SAN' 

air2 = 'SANO'

air3 = 'SANO123'

pattern = re.compile('^[A-Z]{3}$')  # We used here start and end anchors. To match only as much as we want.

matchObj = pattern.match(air1)

matchObj2 = pattern.match(air2)

matchObj3 = pattern.match(air3)

print(matchObj)  # Matched

print(matchObj2)  # None

print(matchObj3)  # None



###############################################################################

print()
# group is used for 

# 1. Bulk modifying '(\d{4})?' it means modifying from greedy to non greedy. or this pattern should come 0 or 1 time.

# 2. Capturing   re.search/match.group(x)

# Selecting anyone out of multiple options. (x|y|z|xy|yz|xz)

# group() returns an Error! if wrong groups are asked.


searchObj = re.search(r'(\d{4})-\d{2}', '9999-99')

print(searchObj)
print(searchObj.group())  # is same as group(0)
print(searchObj.group(1))
#print(searchObj.group(2)) ERROR! Wrong group asked.


###################################################
print()


# groups()  ->> a new method of search/match object which returns a tuple of all groups.


searchObj = re.search(r'(\d{4})-(\d{2})', '9999-99')

print(searchObj)
print(searchObj.groups()) # returns a tuple of all groups.

#########################################################
print()

# Making a group uncapturing.


# syntax ->> (?: regex part)


searchObj = re.search(r'(\d{4})-(?:\d{5})', '9999-12345')

print(searchObj)

print(searchObj.groups())  # Here the 2nd group is ignored.

# It is useful in cases where you need to modify a bulk part of regex but you want want it to be captured 
# while using functions like findall and groups


###########################################################
print()

# Matching time. Using Or option within a group. The valid time is 00:00 to 23:59
# In the first part of the time, first digit can be 0 ,1 and 2.
# If 0 or 1, The2nd digit of the first part can be 0-9.

# If 2 then 2nd gigit of the first part  can exceed 3.

# After the colon, the first digit can't exceed 5
# After the colon, the second digit can go from 0-9


t1 = '11:20'
t2 = '22:80' # Invalid time
t3 = '24:00' # Invalid time
t4 = '23:59'

searchObj = re.search(r'([01]\d|[2][0-3]):[0-5]\d', t1)

searchObj2 = re.search(r'([01]\d|[2][0-3]):[0-5]\d', t2)

searchObj3 = re.search(r'([01]\d|[2][0-3]):[0-5]\d', t3)


print(searchObj) # found a match

print(searchObj2) # None

print(searchObj3) # None


########################################################

# Greedy to Non Greedy reg ex - *, +, ? , {} are all on default greedy.
# When accompanied by ? become Non greedy.

#Greedy - As longest match/search as possible
print(re.search(r'hi*', 'hiii')) # max anything, go to max
print(re.search(r'hi+', 'hiii')) # max anything, go to max
print(re.search(r'hi?', 'hiii')) # max 1, go to max

print(re.search(r'hi{1,}', 'hiii'))  # min 1, max anything
print(re.search(r'hi{,2}', 'hiii')) # min 0 , max 2
print(re.search(r'hi{1,2}', 'hiii')) # min 1 and max 2.



print()

# Non Greedy - As smallest match/search as possible
print(re.search(r'hi*?', 'hiii'))  # min 0, stop at 0
print(re.search(r'hi+?', 'hiii')) # min 1 stop at 1
print(re.search(r'hi??', 'hiii')) # min 0, stop at 0

print(re.search(r'hi{1,}?', 'hiii')) # min 1. Stop at min.
print(re.search(r'hi{,2}?', 'hiii')) # min 0, stop at 0
print(re.search(r'hi{1,2}?', 'hiii')) # min 1, stop at 1

################################################################


# re.sub revisited ->> re.sub(regex, newstring, oldstring)
# Wherever regex comes in oldstring, replace regex with newstring in the oldstring.

row = 'column1, column2,column3'

# If we were to deal with a csv file and we want to first normalize the data in pure csv format,
# then we need to remove all spaces.

# re.sub will help us in that.
# In each row what we can do is, to replace (every comma and any number of spaces) all of this happening 
# consecutively with just a comma.

# Then we get a pure csv format.


string = re.sub(r',\s*', ',', row)  # RETURNS A STRING
# Its just a string modification

# Wherever this regex appears, replace it with a comma (,) in the string row.

print(string)





# Lets see if a regex is not found , what string is returned.

a = re.sub(r'\d\d', 'abc', 'Hello World')

print(a) # So it prints Hello World back. 

# So if a regex is not found, it doesn't throws any error, but returns the same string back.

#####################################################



# Changing the format of the date using re.sub


a = '11/22/1999' # its in mm/dd/yyyy

# Convert this to dd/mm/yyyy


# re.sub in combination with capturing data by groups can help us do this.

new = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\2/\1/\3', a )

print(new)

####################################################

# re.findall() will give you matched paterns.
# Also if you have captured groups in your regex, it will return groups.


# If only one group is captured, it is returned as an element of the list.

# If multiple groups are captured, they are returned as a tuple in the list.


a = re.findall(r'\d\d-\d\d-\d\d\d\d', '12-34-5678-91-11-9999') # When not capturing

print(a)


a = re.findall(r'(\d\d)-\d\d-\d\d\d\d', '12-34-5678-91-11-9999') # When capturing just one group

print(a)


a = re.findall(r'(\d\d)-(\d\d)-(\d\d\d\d)', '12-34-5678-91-11-9999') # When capturing multiple groups

print(a)


######################################################

# Palindromes of 5 characters  (Using backreferences in the regex) This could be generalized to any numb of char

ex = 'level'
ex2 = 'stats'
ex3 = 'notpa'


a = re.match(r'(\w)(\w)\w\2\1', ex)

print(a)


a = re.match(r'(\w)(\w)\w\2\1', ex2)

print(a)


a = re.match(r'(\w)(\w)\w\2\1', ex3)

print(a)


# Remember if there was a file and you have to find all palindromes there and print it, you can do it with search,
# since it searches just the first palindrome and ends.


# Also you can't do it with findall, you can find palindromes but will not be able to print it 
# as you have groups in regex and only that portion will be printed.

# Also if you tried to group the entire regex in one (), backreferncing needs to be changed , 
# as extra groups are added. 

# findall in that case will return a tuple of all groups, palindrome will be one of the elements of the tuple,
# you need to pick it out by indexing.


# Better option is finditer and list comprehension together.

# finiter returns the entire pattern like search and match.

# You can purposefully do m = re.finditer(regex, string),   m.group(x) to get your groups.

#####################################################



# Name capturing groups ->> (?P <tag>)


# Used when there are so many groups and they need to be backreferenced either in the regex or in substitution


a = re.sub(r'(?P<month>\d\d)-(?P<day>\d\d)-(?P<year>\d\d\d\d)', '\g<day>-\g<month>-\g<year>', '12-22-1999')

print(a)



# use re.VERBOSE with it to make it more readable.


a = re.sub(r'''(?P<month>\d\d)
               -(?P<day>\d\d)
               -(?P<year>\d\d\d\d)''',    '\g<day>-\g<month>-\g<year>',   '12-22-1999', re.X)

print(a)


#####################################################