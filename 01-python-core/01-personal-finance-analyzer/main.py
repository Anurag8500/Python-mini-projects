expenses = []

print("=== Personal Finance Analyzer ===")

number_of_expenses = int(input("How many expenses do you want to enter? "))

if number_of_expenses <= 0:
    print("No expenses to analyze.")
else:
    for i in range(number_of_expenses):
        print(f"\nExpense {i + 1}")

        category = input("Category: ").strip().lower()
        amount = float(input("Amount: ₹"))

        expenses.append({
            "category": category,
            "amount": amount
        })

    # Basic calculations
    total = sum(expense["amount"] for expense in expenses)
    average = total / len(expenses)

    highest = max(expenses, key=lambda expense: expense["amount"])
    lowest = min(expenses, key=lambda expense: expense["amount"])

    # Category analysis
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    # Results
    print("\n=== Financial Summary ===")

    print(f"Total spending: ₹{total:.2f}")
    print(f"Average expense: ₹{average:.2f}")

    print(
        f"Highest expense: "
        f"{highest['category'].title()} - ₹{highest['amount']:.2f}"
    )

    print(
        f"Lowest expense: "
        f"{lowest['category'].title()} - ₹{lowest['amount']:.2f}"
    )

    print("\nSpending by category:")

    for category, amount in category_totals.items():
        print(f"- {category.title()}: ₹{amount:.2f}")