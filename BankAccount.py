import random

class BankAccount:
    def __init__(self, full_name):
        # define attributes
        self.name = full_name
        self.account_number = random.randint(80000000,99999999)
        self.balance = 0
    
    # define methods
    def deposit(self):
        pass

    def withdraw(self):
        pass

    def get_balance(self):
        pass

    def add_interest(self):
        pass

    def print_statement(self):
        print (self.account_number)
        pass

test = BankAccount("test")

BankAccount.print_statement(test)