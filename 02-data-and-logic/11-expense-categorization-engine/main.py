print("=== Expense Categorization Engine ===")


# ============================================================
# Expense Data
# ============================================================

expenses = [
    {
        "id": 1,
        "description": "Grocery Shopping",
        "amount": 2400.00,
        "category": "food",
        "month": "January"
    },
    {
        "id": 2,
        "description": "Uber Ride",
        "amount": 450.00,
        "category": "transport",
        "month": "January"
    },
    {
        "id": 3,
        "description": "Netflix Subscription",
        "amount": 649.00,
        "category": "entertainment",
        "month": "January"
    },
    {
        "id": 4,
        "description": "Electricity Bill",
        "amount": 1800.00,
        "category": "utilities",
        "month": "January"
    },
    {
        "id": 5,
        "description": "Restaurant Dinner",
        "amount": 1200.00,
        "category": "food",
        "month": "February"
    },
    {
        "id": 6,
        "description": "Train Ticket",
        "amount": 850.00,
        "category": "transport",
        "month": "February"
    },
    {
        "id": 7,
        "description": "New Headphones",
        "amount": 3200.00,
        "category": "shopping",
        "month": "February"
    },
    {
        "id": 8,
        "description": "Mobile Recharge",
        "amount": 599.00,
        "category": "utilities",
        "month": "February"
    },
    {
        "id": 9,
        "description": "Movie Tickets",
        "amount": 900.00,
        "category": "entertainment",
        "month": "March"
    },
    {
        "id": 10,
        "description": "Monthly Groceries",
        "amount": 3100.00,
        "category": "food",
        "month": "March"
    }
]


next_expense_id = 11

valid_categories = [
    "food",
    "transport",
    "entertainment",
    "shopping",
    "utilities",
    "health",
    "education",
    "other"
]

valid_months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]


# ============================================================
# Main Menu
# ============================================================

while True:

    print("\n=== Menu ===")
    print("1. View all expenses")
    print("2. Add expense")
    print("3. Update expense category")
    print("4. Category summary")
    print("5. Highest expenses")
    print("6. Monthly analysis")
    print("7. Search expenses")
    print("8. Filter by category")
    print("9. Expense statistics")
    print("10. Detailed expense report")
    print("11. Exit")

    choice = input("Choose an option: ").strip()


    # ========================================================
    # VIEW ALL EXPENSES
    # ========================================================

    if choice == "1":

        print("\n=== All Expenses ===")

        for expense in expenses:
            print(
                f"[{expense['id']}] "
                f"{expense['description']} | "
                f"₹{expense['amount']:,.2f} | "
                f"{expense['category'].title()} | "
                f"{expense['month']}"
            )


    # ========================================================
    # ADD EXPENSE
    # ========================================================

    elif choice == "2":

        print("\n=== Add Expense ===")

        description = input("Description: ").strip()

        if not description:
            print("Description cannot be empty.")
            continue


        while True:

            try:
                amount = float(
                    input("Amount: ₹").strip()
                )

                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Please enter a valid amount.")


        print("\nAvailable categories:")

        for category in valid_categories:
            print(f"- {category.title()}")


        while True:

            category = input("Category: ").strip().lower()

            if category in valid_categories:
                break

            print(
                "Invalid category. "
                "Please choose from the available categories."
            )


        print("\nAvailable months:")

        for month in valid_months:
            print(f"- {month.title()}")


        while True:

            month = input("Month: ").strip().lower()

            if month in valid_months:
                month = month.title()
                break

            print("Invalid month.")


        expenses.append(
            {
                "id": next_expense_id,
                "description": description.title(),
                "amount": amount,
                "category": category,
                "month": month
            }
        )

        print(
            f"Expense added successfully "
            f"with ID {next_expense_id}."
        )

        next_expense_id += 1


    # ========================================================
    # UPDATE EXPENSE CATEGORY
    # ========================================================

    elif choice == "3":

        print("\n=== Update Expense Category ===")

        try:
            expense_id = int(
                input("Enter expense ID: ").strip()
            )
        except ValueError:
            print("Please enter a valid ID.")
            continue


        selected_expense = None

        for expense in expenses:

            if expense["id"] == expense_id:
                selected_expense = expense
                break


        if selected_expense is None:
            print("Expense not found.")
            continue


        print(
            f"\nExpense: "
            f"{selected_expense['description']}"
        )

        print(
            f"Current category: "
            f"{selected_expense['category'].title()}"
        )

        print("\nAvailable categories:")

        for category in valid_categories:
            print(f"- {category.title()}")


        while True:

            new_category = input(
                "New category: "
            ).strip().lower()

            if new_category in valid_categories:
                break

            print("Invalid category.")


        selected_expense["category"] = new_category

        print("Category updated successfully.")


    # ========================================================
    # CATEGORY SUMMARY
    # ========================================================

    elif choice == "4":

        category_data = {}


        for expense in expenses:

            category = expense["category"]

            if category not in category_data:

                category_data[category] = {
                    "expense_count": 0,
                    "total_amount": 0
                }


            category_data[category]["expense_count"] += 1

            category_data[category]["total_amount"] += (
                expense["amount"]
            )


        ranked_categories = sorted(
            category_data.items(),
            key=lambda item: item[1]["total_amount"],
            reverse=True
        )


        print("\n=== Category Summary ===")


        for category, data in ranked_categories:

            average_amount = (
                data["total_amount"]
                / data["expense_count"]
            )

            print(f"\n{category.title()}")

            print(
                f"  Expenses: "
                f"{data['expense_count']}"
            )

            print(
                f"  Total: "
                f"₹{data['total_amount']:,.2f}"
            )

            print(
                f"  Average: "
                f"₹{average_amount:,.2f}"
            )


    # ========================================================
    # HIGHEST EXPENSES
    # ========================================================

    elif choice == "5":

        ranked_expenses = sorted(
            expenses,
            key=lambda expense: expense["amount"],
            reverse=True
        )


        print("\n=== Highest Expenses ===")


        for rank, expense in enumerate(
            ranked_expenses[:5],
            start=1
        ):

            print(
                f"{rank}. "
                f"{expense['description']} | "
                f"₹{expense['amount']:,.2f} | "
                f"{expense['category'].title()} | "
                f"{expense['month']}"
            )


    # ========================================================
    # MONTHLY ANALYSIS
    # ========================================================

    elif choice == "6":

        monthly_data = {}


        for expense in expenses:

            month = expense["month"]

            if month not in monthly_data:

                monthly_data[month] = {
                    "expense_count": 0,
                    "total_amount": 0
                }


            monthly_data[month]["expense_count"] += 1

            monthly_data[month]["total_amount"] += (
                expense["amount"]
            )


        ranked_months = sorted(
            monthly_data.items(),
            key=lambda item: item[1]["total_amount"],
            reverse=True
        )


        print("\n=== Monthly Analysis ===")


        for month, data in ranked_months:

            average_amount = (
                data["total_amount"]
                / data["expense_count"]
            )

            print(f"\n{month}")

            print(
                f"  Expenses: "
                f"{data['expense_count']}"
            )

            print(
                f"  Total: "
                f"₹{data['total_amount']:,.2f}"
            )

            print(
                f"  Average: "
                f"₹{average_amount:,.2f}"
            )


    # ========================================================
    # SEARCH EXPENSES
    # ========================================================

    elif choice == "7":

        search_term = input(
            "Search by description or category: "
        ).strip().lower()


        if not search_term:
            print("Search term cannot be empty.")
            continue


        matching_expenses = [
            expense
            for expense in expenses
            if (
                search_term in expense["description"].lower()
                or search_term in expense["category"].lower()
            )
        ]


        if not matching_expenses:
            print("No matching expenses found.")
            continue


        print("\n=== Search Results ===")


        for expense in matching_expenses:

            print(
                f"[{expense['id']}] "
                f"{expense['description']} | "
                f"₹{expense['amount']:,.2f} | "
                f"{expense['category'].title()} | "
                f"{expense['month']}"
            )


    # ========================================================
    # FILTER BY CATEGORY
    # ========================================================

    elif choice == "8":

        print("\nAvailable categories:")

        for category in valid_categories:
            print(f"- {category.title()}")


        category = input(
            "Enter category: "
        ).strip().lower()


        if category not in valid_categories:
            print("Invalid category.")
            continue


        matching_expenses = [
            expense
            for expense in expenses
            if expense["category"] == category
        ]


        if not matching_expenses:
            print("No expenses found in this category.")
            continue


        total_category_amount = sum(
            expense["amount"]
            for expense in matching_expenses
        )


        print(
            f"\n=== {category.title()} Expenses ==="
        )


        for expense in matching_expenses:

            print(
                f"[{expense['id']}] "
                f"{expense['description']} | "
                f"₹{expense['amount']:,.2f} | "
                f"{expense['month']}"
            )


        print(
            f"\nCategory total: "
            f"₹{total_category_amount:,.2f}"
        )


    # ========================================================
    # EXPENSE STATISTICS
    # ========================================================

    elif choice == "9":

        if not expenses:
            print("No expenses available.")
            continue


        total_expenses = len(expenses)

        total_spending = sum(
            expense["amount"]
            for expense in expenses
        )

        average_expense = (
            total_spending
            / total_expenses
        )


        highest_expense = max(
            expenses,
            key=lambda expense: expense["amount"]
        )

        lowest_expense = min(
            expenses,
            key=lambda expense: expense["amount"]
        )


        print("\n=== Expense Statistics ===")

        print(
            f"Number of expenses: "
            f"{total_expenses}"
        )

        print(
            f"Total spending: "
            f"₹{total_spending:,.2f}"
        )

        print(
            f"Average expense: "
            f"₹{average_expense:,.2f}"
        )

        print(
            f"Highest expense: "
            f"{highest_expense['description']} "
            f"(₹{highest_expense['amount']:,.2f})"
        )

        print(
            f"Lowest expense: "
            f"{lowest_expense['description']} "
            f"(₹{lowest_expense['amount']:,.2f})"
        )


    # ========================================================
    # DETAILED EXPENSE REPORT
    # ========================================================

    elif choice == "10":

        if not expenses:
            print("No expenses available.")
            continue


        total_spending = sum(
            expense["amount"]
            for expense in expenses
        )


        category_counts = {}

        for expense in expenses:

            category = expense["category"]

            category_counts[category] = (
                category_counts.get(category, 0) + 1
            )


        highest_expense = max(
            expenses,
            key=lambda expense: expense["amount"]
        )


        average_expense = (
            total_spending
            / len(expenses)
        )


        print("\n========================================")
        print("         DETAILED EXPENSE REPORT")
        print("========================================")


        print(
            f"\nTotal expenses      : "
            f"{len(expenses)}"
        )

        print(
            f"Total spending     : "
            f"₹{total_spending:,.2f}"
        )

        print(
            f"Average expense    : "
            f"₹{average_expense:,.2f}"
        )

        print(
            f"Highest expense    : "
            f"{highest_expense['description']} "
            f"(₹{highest_expense['amount']:,.2f})"
        )


        print("\nExpenses by category:")


        for category, count in category_counts.items():

            print(
                f"- {category.title()}: "
                f"{count}"
            )


        print("\nTop 3 expenses:")


        top_expenses = sorted(
            expenses,
            key=lambda expense: expense["amount"],
            reverse=True
        )[:3]


        for rank, expense in enumerate(
            top_expenses,
            start=1
        ):

            print(
                f"{rank}. "
                f"{expense['description']} — "
                f"₹{expense['amount']:,.2f}"
            )


    # ========================================================
    # EXIT
    # ========================================================

    elif choice == "11":

        print("\nGoodbye!")
        break


    # ========================================================
    # INVALID OPTION
    # ========================================================

    else:

        print(
            "Invalid option. "
            "Please choose between 1 and 11."
        )