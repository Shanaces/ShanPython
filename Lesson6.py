#If statements
#awading students gradesbased on their performance
#inputing something in the terminal user inputs their own values
marks=int(input("Enter marks "))#declaration of the data type
if marks >=0 and marks <50:
    print(marks, "your grade is E")
elif marks >=50 and marks <60:
    print(marks,"Your grade is D")
elif marks >=60 and marks <70:
    print(marks,"Your grade is C")
elif marks >=70 and marks <80:
    print(marks, "Your Grade is B")
elif marks >=80 and marks <=100:
    print(marks, "Congratulations, your grade is A ")
else:
    print(marks,"Invalid marks")
    #you input the value in the terminal, press enter and after the program has run you run it again
    #It will give you the chance to display another value and you run it again

    #nested if
#check whether student qualifies to move to next class
#someone canmove to the next class only when they have the above,18+
age = int(input("Enter age of student:"))
name = str(input("Enter name of student:"))
if marks >=80 and marks <=100:
        if age >=18:
            print(name,age,"years qualify for university")
        else:
            print("you passed but you're underage")
elif marks ==-2:
    print(name,age,"Invalid marks")

else:
    print("You do not qualify")