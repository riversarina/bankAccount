# Begin by creating a BankAccount class. This class will handle the account holder's name, balance, deposits, and withdrawls.se
class  BankAccount:
# set up the constructor:
# inside the BankAcoount class. define an __init__ method. This constructor should accept two parameters:
# Account_houlder: The name of the perons who holds the account.
# Balance: The starting balance (default should be set to zero)
# Use self to assign these paramenters to instance variables self.account_holder and self.balance
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self.balance = balance
# Add a Deposit Method:
# Inside the class, define a deposit mehtod that accepts an amount parameter.
# Check if the deposit amount is at least $10. If it is, add it to the balance and print a confirmation message. If it isn't, print a message that the minimum deposit amount is $10.
    def deposit(self, amount):
        if amount>=10:
            self.balance +=amount
            print(f"${amount} has been deposited!{self.account_holder}'s new balance is ${self.balance}")
        else:
            print("The minimum transaction is $10. Try again!")

    def withdrawl(self,amount):
        if amount>=10 and amount<=self.balance:
            self.balance -=amount
            print(f"${amount} has been withdrawn!{self.account_holder}'s new balance is ${self.balance}")
        else:
            print("Sorry, you cannot perform this action. The minimum balance is $10.")


person1 = BankAccount("John")
person1.deposit(500)
person1.withdrawl(200)

# Add a Withdrawl Method:
# Define a withdrawl method that accepts an amount parameter
# Check if the amount is greater than zero and within the avaliable balance. If both conditions are met, subtract it from the balance and print the updated balance. Otherwise, print a message indicating that the withdrawl is not possible.



