# create dictionary in such a way that it should add number as a key and square root of number as a value
# Enrollment Number : 92400527061
# Name : Nipunsinh Jadeja


n = int(input("Enter number: "))

dictionary = {}

for i in range(1,n+1):
    dictionary[i] = i ** 2

    print(dictionary)

