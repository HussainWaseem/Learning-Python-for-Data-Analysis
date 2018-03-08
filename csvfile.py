# Reading csv files



import csv

with open('Employees1.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)

# csv_file is our file object.
        
# csv.reader(fobj) returns an iterable.
        
        
print('\n')        
print(csv_reader)
# since the returned value is an iterable, it just prints the memory location of it.


#csv_reader is an iterable which actually puts every line into a separate list and returns it iteratively.
# split happens at delimiter which by default is a comma.



# Now if we wanted a certian column of the csv to be printed out we can do it by indexing.


with open('Employees1.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line[0])   # since column 0 is just Name. It'll print all the names
            
# Here we are not prinitng the entire list. But we actually are printing certain elements from the list.
            
            
            


# Writing a csv file.
            
            

with open('Employees1.csv','r') as csv_file:       #opening the existing csv file
    csv_reader = csv.reader(csv_file)
    
    with open('New_csvfile.csv','w') as new_file:        # creating a new csv file to write into it.
        csv_writer = csv.writer(new_file, delimiter = '-')
        
        for line in csv_reader:
            csv_writer.writerow(line)
            

# csv_writer is an iterable which has a method called writerow which takes lists. Here line is actually a list which
# csv_reader returns.
        
        
# Now a New_csv file is created whose delimiter is a dash '-'
            
# csv.writer puts a quote around the elements who don't have delimiters but values.
# Kind of escape sequence.
            
            
            
# Now to read the csv file we just created.
            

with open('New_csvfile.csv','r') as readingcsv:
    csv_reader = csv.reader(readingcsv, delimiter = '-')  # We have to explicitely mention the delimiter since
                                                           # the default to be read is comma
    for line in csv_reader:
        print(line)
        
        

# DictReader method of csv module
        
with open('Employees1.csv','r') as readobj:
    csv_reader = csv.DictReader(readobj)
    
# csv reader is now an iterable. But different from what csv.reader() used to return.
    
    print(csv_reader)
    
    for line in csv_reader:
        print(line)                # YEs! It is an iterable which is not a list by line, but an Oredred dict by line.
                                   # OrderedDict([(Column heading1, value),(Column heading2, value)...)])
                                   # list of tuples.
        
    print('\n')
    print('\n')
    print('\n')
    print('\n')                              # Ordered here means, it will preserve its order.
    for line in csv_reader:
        print(line['JOB TITLE'])          # We can index it and can take out desired elements from each row.
        
        

# DictWriter method of csv module.
        

with open ('Employees1.csv','r') as readobj:
    csv_reader = csv.DictReader(readobj)
        
    field_names = ['NAME','JOB TITLE','DEPARTMENT','EMPLOYEE ANNUAL SALARY','ESTIMATED ANNUAL SALARY MINUS FURLOUGHS']
    with open('Newone.csv','w') as newone:
        csv_writer = csv.DictWriter(newone, fieldnames = field_names, delimiter = '\t')
        
# We need to write the fieldnames so that while reading Python knows the fields that need to be accessed and written
# and in which order.
        
        csv_writer.writeheader()  #writeheader() method of the iterable writer object will include the top row of 
                                 # csv file as fieldnames.
        
        for line in csv_reader:
            csv_writer.writerow(line)








#########################################################################
            
            
# fieldnames parameter used is actually a sequence which uses the order in which the file needs to be written.
            
# Lets change the order of the fieldnames to be written in our new csv file.
            


with open ('Employees1.csv','r') as readobj:
    csv_reader = csv.DictReader(readobj)
        
    field_names = ['DEPARTMENT','JOB TITLE', 'NAME','EMPLOYEE ANNUAL SALARY','ESTIMATED ANNUAL SALARY MINUS FURLOUGHS']
    with open('New_field_changed.csv','w') as newone:
        csv_writer = csv.DictWriter(newone, fieldnames = field_names, delimiter = '\t')
        

        csv_writer.writeheader()  # Just to mention the column heading at the top.
        
        for line in csv_reader:
            csv_writer.writerow(line)
            
# I have changed the sequence of the elements within the fieldnames, so the order in now which the file will be
# written would be different.


# Note - DictWriter can only be used if DictReader is also used.
            
            

###########################################################################
            
# If we want only selected fieldnames to be written in our new csv file.
            

with open ('Employees1.csv','r') as readobj:
    csv_reader = csv.DictReader(readobj)
        
    field_names = ['NAME','JOB TITLE','DEPARTMENT']
    with open('deletedfields.csv','w') as newone:
        csv_writer = csv.DictWriter(newone, fieldnames = field_names, delimiter = '\t')
        

        
        csv_writer.writeheader()  
        for line in csv_reader:
            del line['EMPLOYEE ANNUAL SALARY']
            del line['ESTIMATED ANNUAL SALARY MINUS FURLOUGHS']
            csv_writer.writerow(line)
 
# Now the resulted Ordered Dictionary line by line won't show last 2 columns and their values.           