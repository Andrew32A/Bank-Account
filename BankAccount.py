import random

class BankAccount:
    def __init__(self, full_name):
        # define attributes
        self.name = full_name
        self.account_number = random.randint(80000000,99999999)
        self.balance = 0
    
    # defined methods below

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount} | New balance: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        if amount > self.balance:
            print("Insufficient funds. You have been charged an overdraft fee of $10")
            self.balance -= 10
        else:
            print(f"Amount withdrawn: ${amount} | New balance: ${self.balance}")

    def get_balance(self):
        print(f"Your current balance is: ${self.balance}")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
        self.balance = round(self.balance, 2)
        print(f"You have gained ${interest} in interest, your current balance is ${self.balance}")

    def print_statement(self):
        print (f"{self.name}\nAccount number: {self.account_number}\nBalance: ${self.balance}")


user_mitchel = BankAccount("Mitchel Hudson")
BankAccount.print_statement(user_mitchel)
BankAccount.deposit(user_mitchel, 10000)
BankAccount.withdraw(user_mitchel, 5000)
BankAccount.get_balance(user_mitchel)
BankAccount.add_interest(user_mitchel)
BankAccount.print_statement(user_mitchel)