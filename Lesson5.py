#If statements
#Conditional statements
#Check if number is positive
num=2
if num>0:
    print(num, "Is a positive number")

#This statement is printed only when the test expression is true
#If it is false the statement is ignored

num=-2
if num>0:
    print(num, "Is a positive number")

#using else
number=-4
if number >0:
    print(number, "Is a positive number or zero")
else:
    print(number, "Is a negative number")

#Using elif when conditions are more than 1
if number >0:
    print(number, "Is a positive number")
elif number ==0:
    print(number, "Is equal to zero")
else:
    print(number, "Is a negative number")

#Nested if-if inside another if
name="Maxwell"
age=18
weight=100
#Check if someone qualifies for blood donation
if age >=18:
    if weight >=50 and weight <100:
        print(name, "You qualify for blood donation")
    elif weight >=100:
        print(name, "You are obese; you do not qualify")
    else:
        print(name, "above 18 but below the required weight")
else:
    print(name, "Underage so you do not qualify")