#BankAccount
class BankAccount:
    def __init__(self, account_holder):   
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds for this withdrawal.")

    def account_info(self):
        return f"Account holder: {self.account_holder}, Balance: ${self.balance:.2f}"


#SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, interest_rate=0.02):
        super().__init__(account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied. New balance: ${self.balance:.2f}")


#CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, transaction_fee=1):
        super().__init__(account_holder)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        total_withdrawal = amount + self.transaction_fee
        if total_withdrawal <= self.balance:
            self.balance -= total_withdrawal
            print(f"Withdrew ${amount:.2f} (including fee: ${self.transaction_fee:.2f}). New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds for this withdrawal and transaction fee.")


 # Test Cases
if __name__ == "__main__":
    print("\n Test Case 1: Basic Functionality of BankAccount ")
    basic_account = BankAccount("User01")
    basic_account.deposit(5000)
    assert basic_account.balance == 5000, "Error: Deposit failed, balance should be $5000"
    basic_account.withdraw(2000)
    assert basic_account.balance == 3000, "Error: Withdrawal failed, balance should be $3000"
    basic_account.withdraw(4000)  
    assert basic_account.balance == 3000, "Error: Withdrawal failed, balance should remain $3000"
