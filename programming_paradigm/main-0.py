import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 3:
        print("Usage: python main-0.py <name> <initial_balance>")
        return

    name = sys.argv[1]
    try:
        initial_balance = float(sys.argv[2])
    except ValueError:
        print("Initial balance must be a number.")
        return

    account = BankAccount(name, initial_balance)

    # Simulate operations
    print(account.deposit(67))
    print(account.withdraw(670))
    print(account.display_balance())

if __name__ == "__main__":
    main()
