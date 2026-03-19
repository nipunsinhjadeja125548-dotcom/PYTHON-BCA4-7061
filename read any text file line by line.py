#read any text file line by line 

filename = input("enter file name: ")

with open(filename,"r") as file:
    for line in file:
        print(line,end="")
