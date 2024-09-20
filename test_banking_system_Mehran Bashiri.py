# test_banking_system.py
from banking_system import BankAccount, SavingsAccount, CheckingAccount

# Test Cases
def run_tests():
    # Test Case 1: Basic Functionality of BankAccount
    basic_account = BankAccount("user01")
    basic_account.deposit(1000)  
    assert basic_account.balance == 1000, (
        f"Error: {basic_account.account_holder}'s balance should be $1000, "
        f"but got ${basic_account.balance:.2f}"
    )
    basic_account.withdraw(300)  
    assert basic_account.balance == 700, (
        f"Error: {basic_account.account_holder}'s balance should be $700, "
        f"but got ${basic_account.balance:.2f}"
    )
    basic_account.withdraw(800)  
    assert basic_account.balance == 700, (
        f"Error: {basic_account.account_holder}'s balance should remain $700 "
        f"(Insufficient funds)."
    )
    print(f"Test Case 1: {basic_account.account_holder}'s balance correctly handled with "
          "deposits and withdrawals.")

    # Test Case 2: SavingsAccount with Interest Application
    savings_account = SavingsAccount("user02", interest_rate=0.03)
    savings_account.deposit(2000) 
    assert savings_account.balance == 2000, (
        f"Error: {savings_account.account_holder}'s balance should be $2000, "
        f"but got ${savings_account.balance:.2f}"
    )
    savings_account.apply_interest()  
    assert savings_account.balance == 2060, (
        f"Error: {savings_account.account_holder}'s balance should be $2060 after "
        f"applying 3% interest, but got ${savings_account.balance:.2f}"
    )
    print(f"Test Case 2: {savings_account.account_holder}'s balance correctly handled with "
          "interest application.")

    # Test Case 3: CheckingAccount with Transaction Fee
    checking_account = CheckingAccount("user03", transaction_fee=2)
    checking_account.deposit(1000)  
    assert checking_account.balance == 1000, (
        f"Error: {checking_account.account_holder}'s balance should be $1000, "
        f"but got ${checking_account.balance:.2f}"
    )
    checking_account.withdraw(200)  
    assert checking_account.balance == 798, (
        f"Error: {checking_account.account_holder}'s balance should be $798 after "
        f"withdrawing $200 plus $2 fee, but got ${checking_account.balance:.2f}"
    )
    checking_account.withdraw(900)  
    assert checking_account.balance == 798, (
        f"Error: {checking_account.account_holder}'s balance should remain $798 "
        f"(Insufficient funds for withdrawal with fee)."
    )
    print(f"Test Case 3: {checking_account.account_holder}'s balance correctly handled with "
          "withdrawals and fees.")

    # Test Case 4: Handling Edge Cases
    edge_account = BankAccount("user04")
    edge_account.deposit(0)  
    assert edge_account.balance == 0, (
        f"Error: {edge_account.account_holder}'s balance should remain $0 after "
        f"depositing $0, but got ${edge_account.balance:.2f}"
    )
    edge_account.deposit(-500)  
    assert edge_account.balance == 0, (
        f"Error: {edge_account.account_holder}'s balance should remain $0 "
        f"(negative deposit should be rejected), but got ${edge_account.balance:.2f}"
    )
    print(f"Test Case 4: {edge_account.account_holder}'s edge cases handled correctly.")
    print("All test cases passed successfully.")

if __name__ == "__main__":
    run_tests()
