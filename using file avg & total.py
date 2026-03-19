""" Write a program to read text file having number and display all 
numbers with total and average at the last """
# Enrollment number : 92400527061
# Name : Nipunsinh Jadeja

with open("number.txt","r") as file:
    total = 0
    count = 0

    print("Number in file !")

    for line in file:
        num = int(line.strip())

        print(num)
        total += num
        count += 1

avg = total / count

print("Total =", total)
print("Average =", avg)


