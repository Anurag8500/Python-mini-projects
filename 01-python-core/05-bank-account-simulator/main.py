print("=== Bank Account Simulator ===")

account = {
    "holder": "",
    "account_number": "",
    "balance": 0.0
}

transactions = []


# Account setup
account["holder"] = input("Account holder name: ").strip().title()
account["account_number"] = input("Account number: ").strip().upper()

while True:
    try:
        opening_balance = float(input("Opening balance: ₹"))

        if opening_balance < 0:
            print("Opening balance cannot be negative.")
            continue

        account["balance"] = opening_balance
        break

    except ValueError:
        print("Please enter a valid amount.")


# Main application loop
while True:
    print("\n=== Menu ===")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. View transaction history")
    print("5. Account summary")
    print("6. Exit")

    choice = input("Choose an option: ").strip()

    # Check balance
    if choice == "1":
        print(f"\nCurrent balance: ₹{account['balance']:.2f}")

    # Deposit money
    elif choice == "2":
        try:
            amount = float(input("Amount to deposit: ₹"))

            if amount <= 0:
                print("Deposit amount must be greater than 0.")
                continue

            account["balance"] += amount

            transactions.append({
                "type": "Deposit",
                "amount": amount,
                "balance_after": account["balance"]
            })

            print("Deposit successful.")
            print(f"New balance: ₹{account['balance']:.2f}")

        except ValueError:
            print("Please enter a valid amount.")

    # Withdraw money
    elif choice == "3":
        try:
            amount = float(input("Amount to withdraw: ₹"))

            if amount <= 0:
                print("Withdrawal amount must be greater than 0.")
                continue

            if amount > account["balance"]:
                print("Insufficient balance.")
                continue

            account["balance"] -= amount

            transactions.append({
                "type": "Withdrawal",
                "amount": amount,
                "balance_after": account["balance"]
            })

            print("Withdrawal successful.")
            print(f"New balance: ₹{account['balance']:.2f}")

        except ValueError:
            print("Please enter a valid amount.")

    # Transaction history
    elif choice == "4":
        if not transactions:
            print("\nNo transactions yet.")
            continue

        print("\n=== Transaction History ===")

        for number, transaction in enumerate(transactions, start=1):
            print(
                f"{number}. "
                f"{transaction['type']} - "
                f"₹{transaction['amount']:.2f} | "
                f"Balance: ₹{transaction['balance_after']:.2f}"
            )

    # Account summary
    elif choice == "5":
        print("\n=== Account Summary ===")
        print(f"Account holder: {account['holder']}")
        print(f"Account number: {account['account_number']}")
        print(f"Current balance: ₹{account['balance']:.2f}")
        print(f"Total transactions: {len(transactions)}")

    # Exit
    elif choice == "6":
        print("\nThank you for using the Bank Account Simulator.")
        break

    else:
        print("Invalid option. Please choose between 1 and 6.")

