#recap on if statements
#Assignment BMI program
weight=int(input("enter your weight :"))
height=float(input("Enter your height :"))
BMI=weight / height**2#eponentiation
print("The Body Mass Index of peerson x is",BMI)

if BMI <18.5 :
    print(BMI,"Underweight")
elif BMI >=18.5 and BMI <=22.9:
    print(BMI,"normal")
elif BMI >=23 and BMI<=24.9:
    print(BMI,"Overweight")
elif BMI >=25 and BMI <=29.9:
    print(BMI,"pre-obese")
elif BMI >=30 and BMI <=34.9:
    print(BMI,"obese class 1")
elif BMI >=35 and BMI <=39.9:
    print(BMI,"obese class 2")
elif BMI >=40:
    print(BMI,"obese class 3")