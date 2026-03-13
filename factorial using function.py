# factorial using function
# Enrollment Number : 92400527061
# Name : Nipunsinh Jadeja


def factorial (num) :
    
    fac = 1
    

    for i in range(1,num+1):
        fac = fac *  i
    print("Fact is : ",fac)
       

num = int(input("Enter number: "))
factorial(num)


