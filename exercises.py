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



# test values:
nightfall = BankAccount("Nightfall", 950, True)
dawnbringer = BankAccount("Dawnbringer", 666) #overdraft auto set to False

# test cases:
# nightfall (account with overdraft)
nightfall.deposit(76)
nightfall.withdraw(100) 
nightfall.withdraw(-100) # should not allow negative withdraw
nightfall.withdraw(10000) # should allow overdraft

#dawnbringer (account without overdraft)
dawnbringer.deposit(29)
dawnbringer.withdraw(100) 
dawnbringer.withdraw(-100) # should not allow negative withdraw
dawnbringer.withdraw(10000) # should not allow overdraft


# test savings account
HouseSavings = SavingsAccount("HouseSavings", 5000, True) # overdraft allowed, even tho it doesnt matter since withdrawal isnt allowed
CarSavings = SavingsAccount("CarSavings", 1000) # no overdraft allowed, even tho it doesnt matter since withdrawal isnt allowed

# test cases:
# HouseSavings (account with overdraft)
HouseSavings.deposit(1000)
HouseSavings.withdraw() # should not allow withdrawal

# CarSavings (account without overdraft)
CarSavings.deposit(1000)
CarSavings.withdraw() # should not allow withdrawal
