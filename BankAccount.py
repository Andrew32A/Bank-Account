import random

class BankAccount:
    def __init__(self, full_name):
        # define attributes
        self.name = full_name
        self.account_number = random.randint(80000000,99999999)
        self.balance = 0
    
    # defined methods below

    def deposit(self, amount):
        # takes self balance and adds amount in arg
        self.balance += amount
        print(f"Amount deposited: ${amount} | New balance: ${self.balance}")

    def withdraw(self, amount):
        # takes self balance and subracts amount in arg
        self.balance -= amount
        if amount > self.balance:
            print("Insufficient funds. You have been charged an overdraft fee of $10")
            self.balance -= 10
        else:
            print(f"Amount withdrawn: ${amount} | New balance: ${self.balance}")

    def get_balance(self):
        # prints and returns self balance
        print(f"Your current balance is: ${self.balance}")
        return self.balance

    def add_interest(self):
        # adds an interest of 0.0083% of self balance to self balance
        if self.balance < 0:
            print(f"Your account is not elegible for interest due to having a balance of ${self.balance}")
        else:
            interest = self.balance * 0.00083
            self.balance += interest
            self.balance = round(self.balance, 2)
            print(f"You have gained ${interest} in interest, your current balance is ${self.balance}")

    def print_statement(self):
        # hides first 4 numbers of account number with * and displays users full name and balance
        hidden_acc_num = (str(self.account_number)[4:8])
        hidden_acc_num = "****" + hidden_acc_num
        print (f"{self.name}\nAccount number: {hidden_acc_num}\nBalance: ${self.balance}")

# Mitchel Hudson
user_mitchel = BankAccount("Mitchel Hudson")
user_mitchel.deposit(400000)
user_mitchel.withdraw(150)
user_mitchel.get_balance()
user_mitchel.add_interest()
user_mitchel.print_statement()
print("\n\n")

# Adam Braus
user_dani = BankAccount("Adam Braus")
user_dani.deposit(20000)
user_dani.withdraw(20001)
user_dani.get_balance()
user_dani.add_interest()
user_dani.print_statement()
print("\n\n")


# Andrew Alsing
user_andrew = BankAccount("Andrew Alsing")
user_andrew.deposit(10000000000)
user_andrew.withdraw(2)
user_andrew.get_balance()
user_andrew.add_interest()
user_andrew.print_statement()
print("\n\n")