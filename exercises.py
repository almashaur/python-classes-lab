import random

class BankAccount:
    def __init__(self, owner, balance, has_overdraft=False):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111111, 999999999)
        self.has_overdraft = has_overdraft

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if not  self.has_overdraft and amount > self.balance:
            return "Withdrawal denied: Insufficient funds and no overdraft allowed."
        self.balance -= amount
        return self.balance
    
    def __str__(self):
        return f"Account {self.account_no} - Balance: {self.balance:.2f}"


class SavingsAccount(BankAccount):
    def withdraw(self):
        return "No withdrawals permitted"




# Create BankAccount instances
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500, has_overdraft=True)

# Make deposits
print(f"Alice deposits $500: New balance = {account1.deposit(500)}")
print(f"Bob deposits $200: New balance = {account2.deposit(200)}")

# Make withdrawals
print(f"Alice withdraws $2000: {account1.withdraw(2000)}")  # Should deny
print(f"Bob withdraws $1000: New balance = {account2.withdraw(1000)}")  # Should allow (has overdraft)

# Print account summaries
print(account1)
print(account2)

# SavingsAccount
savings = SavingsAccount("Charlie", 3000)
print(savings.deposit(500))
print(savings.withdraw())  # Should return "No withdrawals permitted"
print(savings)
