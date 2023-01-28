# for loop
fruits=["Passion","Mango","Banana","Orange","Apple","Avocado"]
print(fruits)
#Looping/iterating means repeating the same process
#for loop iterates through a asequence e.g list, string, dictionary, tuple
for fruit in fruits:
    #variable fruit refers to the individual items in the fruits list
    #in means members of the fruits variable(our list)
    print(fruit)
    fruit="banana"
    for x in fruit:
        if x=="n":
            break
        print(x)
#loop through a range of numbers
for number in range(0,10):
    print(number)

    for number in range(10,20,2):
        print(number)
tuple1=("shan","Dan","Farah","Jose")
for name in tuple1:
    print(name)
dict1={
        "Brand":"Nike",
        "Model":"AirForce1",
        "YOM":2000
    }
for item in dict1.keys():
    print(item)
for item in dict1.values():
    print(item)
for item in dict1.values():
    if item == "Airforce1":
        print("The amount is 20,000")
        break #If the condition is true, exit the loop
        print(item)
for item in dict1.keys():
    if item=="Model":
        continue #If the condition is true, ignore the current item and continue
        print(item)