#While loop
#the loop inside while loop is executed as long as the condition is satisfied
#while the condiotion is true the loop continues
#we exit the loop when the condition is not true
#make sure you increase the value you are testing
count=1
while count <6:
    print(count,"printing the value of count")
    #increase the variable of the value youre testing
    count=count +1
    patients=1
while patients<10:
    #recap on if statements
    #BMI program
    name = str(input("enter your name:"))
    weight = int(input("enter your weight :"))
    height = float(input("Enter your height :"))
    BMI = weight / height ** 2  # eponentiation
    print("The Body Mass Index of peerson x is", BMI)

    if BMI < 18.5:
        print(patients,BMI,name,"Underweight")
    elif BMI >= 18.5 and BMI <= 22.9:
        print(patients,BMI,name,"normal")
    elif BMI >= 23 and BMI <= 24.9:
        print(patients,BMI,name,"Overweight")
    elif BMI >= 25 and BMI <= 29.9:
        print(patients,BMI,name,"pre-obese")
    elif BMI >= 30 and BMI <= 34.9:
        print(patients,BMI,name,"obese class 1")
    elif BMI >= 35 and BMI <= 39.9:
        print(patients,BMI,name,"obese class 2")
    elif BMI >= 40:
        print(patients,BMI,name,"obese class 3")
    patients=patients+1
    if patients==2:
        print("take a break")
        break