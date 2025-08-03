import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 4:
        print("Usage: python main-0.py <account_holder> <initial_balance> <operation> <amount>")
        return

    account_holder = sys.argv[1]
    try:
        initial_balance = float(sys.argv[2])
    except ValueError:
        print("Initial balance must be a number.")
        return

    operation = sys.argv[3].lower()
    try:
        amount = float(sys.argv[4])
    except (IndexError, ValueError):
        print("Please provide a valid amount.")
        return

    account = BankAccount(account_holder, initial_balance)

    if operation == "deposit":
        account.deposit(amount)
    elif operation == "withdraw":
        account.withdraw(amount)
    else:
        print("Invalid operation. Use 'deposit' or 'withdraw'.")
        return

    print(f"Current Balance: ${account.balance:.2f}")

if __name__ == "__main__":
    main()
