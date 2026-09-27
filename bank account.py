"""
Week 3 - Assignment 1: Bank Account Class
Create a class with methods: deposit, withdraw, display balance.
"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew: {amount}. New balance: {self.balance}")

    def display_balance(self):
        print(f"Account owner: {self.owner} | Balance: {self.balance}")


if __name__ == "__main__":
    account = BankAccount("Alex", 1000)
    account.display_balance()
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(5000)   # should show insufficient funds
    account.display_balance()
