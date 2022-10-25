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
        pass

    def add_interest(self):
        pass

    def print_statement(self):
        print (self.account_number)
        pass

test = BankAccount("test")

BankAccount.print_statement(test)
BankAccount.deposit(test, 10000)
BankAccount.withdraw(test, 5000)