import random

class BankAccount:
    def __init__(self, owner, balance=0, has_overdraft=False):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111111, 999999999)
        self._overdraft = has_overdraft

    # deposit method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to {self.owner}'s account. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")


    # withdraw method
    def withdraw(self, amount):
        if self._overdraft:
            if amount < 0:
                print("Cannot withdraw a negative amount or nothing at all.")
                return
            else:
                self.balance -= amount
                print(f"Withdrew {amount} from {self.owner}'s account. New balance: {self.balance}")
        else:
            if amount > self.balance:
                print("Insufficient funds.")
            elif amount < 0:
                print("Cannot withdraw a negative amount or nothing at all.")
            else:
                self.balance -= amount
                print(f"Withdrew {amount} from {self.owner}'s account. New balance: {self.balance}") 

    
class SavingsAccount(BankAccount):
    def withdraw(self):
        print("Withdrawals aren't allowed from a savings account.")
        return



