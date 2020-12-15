#banking application

class Customer:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def create_account(self):
        account = 2335873457937503
        self.account = account
        print("Account {} is created for {}". format(self.account, self.name))    


    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

c = Customer("John")
c.create_account()
