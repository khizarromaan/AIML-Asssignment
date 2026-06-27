class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount, "New balance:", self.balance)
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrew:", amount, "New balance:", self.balance)
        else:
            print("Insufficient balance!")
            
    def show_balance(self):
        print("Account Holder:", self.account_holder, "Current Balance:", self.balance)

account = BankAccount("Khizar", 5000)

account.show_balance()
account.deposit(1500)
account.withdraw(2000)
account.withdraw(9000)