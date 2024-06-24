'''
Full Name: Bernard Lunny
Team Members: Surya Maddali, Derek Zhou
ID: 962834855
Date: 12/9/2022
Filename: P.2_Lunny_Bernard_bjl5770
Purpose: this program first writes data to a text file then reads it. Next, it writes to 
a csv file using the contents from the text file and putting them into a word information
table with headers. Then it creates a copy of the table and stores it in a 2D list.
Then it takes the copy and is able to iterate through the list and find a key and value
When the key and values are found, the program is able to run multiple operations on
the row asscoaited with the key, but without changing the table. 
'''

#Takes in 3 parameters and writes data to text file
def write_file(text_file, data, data2):
    outfile = open(text_file, "w")
    outfile.write(data)
    outfile.write(data2)
    outfile.close
   
def read_then_write_csv(text_file, csv_file,data,data2):
    new_lst = []
    frequency = []
    dup_lst = []
    frequency_2 = []
    infile = open(text_file, "r")
    text_file_contents = infile.read()
    infile.close()
    lst = text_file_contents.split()
    split_data_1 = data.split(" ")
    split_data_2 = data2.split(" ")
    
#Iterates through original list and removes and repeating elements, this is used to 
#write the new_lst into the csv file so there are no repeated elements like 'course or 'Cmpsc131'   
    for i in lst: 
        found = False
        if len(new_lst) == 0:
            new_lst += [i]
        else:
            for j in new_lst: 
                if i == j:
                    found = True
#this line adds the two repeated strings to the empty list dup_lst                    
                    dup_lst += [i]
            if found == False:    
                new_lst += [i]
                
#Iterates through original and new lst and compares them.
    for i in range(len(new_lst)):
        count = 0
        for j in range(len(lst)):
            if new_lst[i] == lst[j]:
                count = count + 1
        frequency += [str(count)]
#Iterates through new_lst and compares it to the list of the duplicates which is 
#['course', 'CMPSC131'] this is used for the second line row in the csv    
    for i in range(len(new_lst)):
        count = 0
        for j in range(len(dup_lst)):
            if new_lst[i] == dup_lst[j]:
                count = count + 2
        frequency_2 += [str(count)]

    outfile = open(csv_file, "w")

    outfile.write('Words ,')
    outfile.write('Occurences,')
    outfile.write('Line,')
    outfile.write('Word #,')
    outfile.write('Line,')
    outfile.write('Word #')
    
#Arranges data into rows or inserts data into csv vertically.
#Since the length of the new_lst is 9, each row is only 9 cells long. 
    for x in range(len(new_lst)):
        outfile.write(" ")
        outfile.write('\n')
        for y in range(len(new_lst[x])):
            outfile.write(new_lst[x][y])
        outfile.write(',')
        for z in range(len(frequency[x])):
            outfile.write(frequency[x][z])
        outfile.write(',')
        
#Compares list length between new_lst and original two lines of data from 
#text file to determine which line # it was originally. 
        if x < len(split_data_1):
            line_num_1 = "1"
            outfile.write(line_num_1)
        else:
            line_num_2 = "2"
            outfile.write(line_num_2)
        outfile.write(',')
        
#Compares the len between the new_lst and the original two lines of data
#from reading our text file. 
        if x < len(split_data_1):
            word_num_1 = x + 1
            outfile.write(str(word_num_1))
        elif x > len(split_data_2):
            word_num_2 = ((x + 1) - len(split_data_2))
            outfile.write(str(word_num_2))
        outfile.write(',')
#Iterates through the frequency_2 which is the difference between new_lst
# and dup_lst. The frequency list is [0,0,0,0,2,2,0,0,0].
#it writes none to file if the string in the list is equal to zero
        for i in range(len(frequency_2[x])):
            if frequency_2[x][i] == '0':
                outfile.write("")
            elif frequency_2[x][i] == '2':
                outfile.write("2")  
        outfile.write(',')
        for i in range(len(frequency_2[x])):
            if frequency_2[x][i] == '0':
                outfile.write("") 
            elif frequency_2[x][i] == '2':
                outfile.write(str((len(split_data_1)-len(split_data_2))))
    outfile.close()
    
'''
Start of P2 - P3 code:
'''
#Iterates through the csv table and organzies values, comma separated by row, and eventually
#stores each row in a list within a 2D List  

def store_lst_2d(csv_file):
    empty = []
    infile = open(csv_file, "r")
    empty = infile.read().split('\n')
    infile.close
    table_to_2d = []
    for x in range(len(empty)):
        empty[x] = empty[x].split(',')
    for y in range(1,len(empty)):
        new_empty = []
        for z in range(len(empty[y])):
            new_empty += [empty[y][z]]
        table_to_2d += [new_empty]
    return table_to_2d

#Takes in the word info table as a parameter, organizes it by putting each row on a new line,
#then prints it

def entire_map(lst_2d):
    for lst in lst_2d:
        print(lst)
        
#Takes in key as a parameter and uses it to find that key in the word info table
# It will iterate through the table and once the key is found,
#it will return the numbers associated with that key or its row
#If the key is not found, it will return -1
      
def get_value(key, lst_2d):
    for x in range(len(lst_2d)):
        if(lst_2d[x][0]==key):
            empty_lst = []
            for y in range(1,len(lst_2d[x])):
                empty_lst += [lst_2d[x][y]]
            return empty_lst
    if(lst_2d[x][0]!=key):
        return -1
    else:
        pass                    
#Iterates through the table and finds the occurence and word# associated with the key
#If the occurence or key are not found, it will return [-1,-1] 
                    
def get_location(key, occurence, lst_2d):
    for x in range(len(lst_2d)):
        if(lst_2d[x][0]==key) and (lst_2d[x][1]==occurence):
            empty_lst=[]
            for y in range(0,len(lst_2d[x])):
                empty_lst += [lst_2d[x][y]]
            return ([empty_lst[2],empty_lst[3]])       
    if(lst_2d[x][0]!=key) and (lst_2d[x][1]!=occurence):
        return [-1,-1]

#Takes word info table as a parameter and creates an empty 2d list, and returns
#the empty list

def delete_table(lst_2d):
    new_empty_lst = [[]]
    return new_empty_lst

#Iterates through the table to find the row associated with the key.
#Once the row is found it appends the row to a list and compares the list with the entire
#table itself. Another list is created that is onyl the numbers associated with the 
#selected key. This is then compared with the original table (lst_2d) to remove the 
#values assocatiated with the key itself from the table, but leaving the key alone.

def delete_entry(key, lst_2d):
    for x in range(len(lst_2d)):
        if(lst_2d[x][0]==key):
            empty = []
            empty_2=[]
            for j in range(0,len(lst_2d[x])):
                empty += [lst_2d[x][j]]
            for k in range(0,len(lst_2d[x]),6):
                empty_2 += [lst_2d[x][k]] 
    for x in range(len(lst_2d)):
        a = lst_2d
        if lst_2d[x] == empty:
            lst_2d[x] = empty_2
    print(lst_2d)
    if(lst_2d[1]!=[key]):
        return -1
    
#Iterates through the table and finds the corresponding key and values
#that match the variable in the main function. Once found, it will check 
#the occurence, word, and lines. If the occurence is 1 it will delete it,
#if the occurence is 2, it deletes a single entry, and also deletes the second
#word and line entry associated with the key.

def delete_location(key, lst_2d, occurence):
    for q in range(len(lst_2d)):
        if(lst_2d[q][0]==key):
            empty_lst=[]
            empty_lst_2=[]
            for y in range(0,len(lst_2d[q])):
                empty_lst += [lst_2d[q][y]]
            for z in range(0,len(lst_2d[q])):
                empty_lst_2 += [lst_2d[q][z]] 
    if empty_lst_2[1] == '1':
        empty_lst_2[1] = ' '
    elif empty_lst_2[1] == '2':
        empty_lst_2[1] = '1'
    elif empty_lst_2[4] == '2':
        empty_lst_2[4] = ' '  
    elif empty_lst_2[5] == '1 ':
        empty_lst_2[5] = ' '     
    for i in range(len(lst_2d)):
        if lst_2d[i] == empty_lst:
            lst_2d[i] = empty_lst_2
    return lst_2d
    if(lst_2d[1]!=[key]):
        return -1

def main():
    key = 'Kahn'
    occurence = '1'
    data = 'Dan Kahn teaches the course CMPSC131\n'
    data2 = 'CMPSC131 is an important course'
    text_file = "P2cmpsc131.txt"
    csv_file = "P2cmpsc131.csv"
    write_file(text_file, data, data2)
    read_then_write_csv(text_file, csv_file, data, data2)
    store_lst_2d(csv_file)
    lst_2d = store_lst_2d(csv_file)
    entire_map(lst_2d)
    get_value(key, lst_2d)
    get_location(key, occurence, lst_2d)
    delete_table(lst_2d)
    delete_location(key, lst_2d, occurence)
    delete_entry(key,lst_2d)
main()