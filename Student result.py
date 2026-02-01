# Program to calculate Total, Percentage, Result and Grade
# Enrollment number : 92400527061
# Name : Nipunsinh Jadeja

mark1 = int(input("Enter marks of subject 1: "))
mark2 = int(input("Enter marks of subject 2: "))
mark3 = int(input("Enter marks of subject 3: "))
mark4 = int(input("Enter marks of subject 4: "))

total = mark1 + mark2 + mark3 + mark4
per = total / 4

print("total :  ",total)
print("percentage :  ",per)

if mark1 < 40 or mark2 < 40 or mark3 < 40 or mark4 < 40:
    print("result = FAIL")
    print("grade = With Held")
else:
    print("result = PASS")
    
    if per >= 75:
        print("grade = A+")
    elif per >= 60:
        print("grade = A")
    elif per >= 50:
        print("grade = B")
    elif per >= 40:
        print("grade = C")

        

        
