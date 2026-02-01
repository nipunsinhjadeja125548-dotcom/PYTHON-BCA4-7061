# Compound Interest
# Enrollment number : 92400527061
# Name : Nipunsinh Jadeja

p = float(input("Enter Amount: "))
r = float(input("Enter Rate : "))
t = float(input("Enter Time : "))


ci = p * (1 + r / 100) ** t - p


print("Compound Interest is:", ci)
