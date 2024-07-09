# Create a Simple Bank Account Class

class BankAccount:
  def __init__(self, account_balance = 0):
    self.account_balance = account_balance
  
  def deposit(self, amount):
    self.account_balance += amount
  
  def withdraw(self, amount):
    if self.account_balance > amount:
      self.account_balance -= amount
      return True
    else:
      return False
    
  def display_balance(self):
    current_balance = f"Current Balance: ${self.account_balance}"
    return print(current_balance)