#application fumnctions
#USSD Mpesa
#Withdraw money
#Check Balance
#buy airtime
#create a dictionary to hold the details of the user
user={
    "name":"Maxwell",
    "pin":1234,
    "balance":3000,
}

#crate a function from menu
#Parameters and arguments
#parameters allow the user to input values when calling the function
#The parameter is defined inside the parenthesis when creating the function
#arguments are values given when calling the functiom
#arguments are the values of parameters
#all the parameters defined must be given the values when calling the function
def withdraw(amount,agent,pin): #parameter
    #check if pin is correct
    if pin == user["pin"]:
       print(f"hello {user['name']} WELCOME TO YOUR ACCOUNT ")
       if amount<= user["balance"]:
           print("====APPROVED====")
           account_balance=user["balance"]- amount
           print(f"..CONFIRMED..KES{amount}withdrawn from agent no. {agent}"
                 f"New Mpesa balance is Kes {account_balance}")

       else:
           print("Insufficient funds. you do not have enough money to do this transaction. \n"
                 "Try again with different amount")

    else:
        print("Incorrect pin.Try again")

def menu():
    print("====WELCOME==== \n please select an option to proceed")
    print("1. Withdraw money")
    print("2. Check balance")
    print("3. Buy airtime")
    print("4. Mpesa statement")
    print("5. Send money")
    answer=int(input("Select a menu:"))
    if answer == 1:
        withdraw(int(input("enter the amount to withdraw:")),
                 int(input("Enter the agent number:")),
                 int(input("Enter your pin:"))) #arguments
    else:
        print("Select another option")
menu()
#assignment do check balance buy airtime and send money