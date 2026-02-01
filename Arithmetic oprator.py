# Program to perform arithmetic operation
# Enrollment number : 92400527061
# Name : Nipunsinh Jadeja

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator : ")

if op == '+':
    print("addition =", a + b)
    
elif op == '-':
    print("subtration =", a - b)
    
elif op == '*':
    print("multipltion =", a * b)
    
elif op == '/':
    print("division =", a / b)
    
else:
    print("Invalid Operator")
