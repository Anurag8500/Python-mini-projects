print("=== Modular Expense Tracker ===")


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
# Helper Functions
# ============================================================

def find_expense(expense_id):
    """Find and return an expense by ID."""

    for expense in expenses:

        if expense["id"] == expense_id:
            return expense

    return None


def get_expense_amount(expense):
    """Return the amount of an expense."""

    return expense["amount"]


def calculate_average(amounts):
    """Calculate an average from a list of numbers."""

    if not amounts:
        return 0

    return sum(amounts) / len(amounts)


def calculate_grade_from_spending(amount):
    """
    Categorize spending level for demonstration.

    This helper keeps the example focused on
    function design and return values.
    """

    if amount >= 10000:
        return "High"

    elif amount >= 5000:
        return "Medium"

    else:
        return "Low"


# ============================================================
# Expense Functions
# ============================================================

def view_expenses():
    """Display all expenses."""

    print("\n=== All Expenses ===")

    if not expenses:
        print("No expenses available.")
        return

    for expense in expenses:

        print(
            f"[{expense['id']}] "
            f"{expense['description']} | "
            f"₹{expense['amount']:,.2f} | "
            f"{expense['category'].title()} | "
            f"{expense['month']}"
        )


def add_expense():
    """Add a new expense."""

    global next_expense_id

    print("\n=== Add Expense ===")

    description = input(
        "Description: "
    ).strip()

    if not description:
        print("Description cannot be empty.")
        return

    while True:

        try:

            amount = float(
                input("Amount: ₹").strip()
            )

            if amount <= 0:

                print(
                    "Amount must be greater than 0."
                )

                continue

            break

        except ValueError:

            print(
                "Please enter a valid amount."
            )


    print("\nAvailable categories:")

    for category in valid_categories:
        print(f"- {category.title()}")


    while True:

        category = input(
            "Category: "
        ).strip().lower()

        if category in valid_categories:
            break

        print("Invalid category.")


    print("\nAvailable months:")

    for month in valid_months:
        print(f"- {month.title()}")


    while True:

        month = input(
            "Month: "
        ).strip().lower()

        if month in valid_months:

            month = month.title()
            break

        print("Invalid month.")


    expense = {
        "id": next_expense_id,
        "description": description.title(),
        "amount": amount,
        "category": category,
        "month": month
    }


    expenses.append(expense)


    print(
        f"Expense added successfully "
        f"with ID {next_expense_id}."
    )


    next_expense_id += 1


def update_expense():
    """Update an existing expense."""

    print("\n=== Update Expense ===")

    try:

        expense_id = int(
            input("Enter expense ID: ").strip()
        )

    except ValueError:

        print("Please enter a valid ID.")
        return


    expense = find_expense(expense_id)


    if expense is None:

        print("Expense not found.")
        return


    print(
        f"\nUpdating: "
        f"{expense['description']}"
    )


    new_description = input(
        f"New description "
        f"(press Enter to keep "
        f"'{expense['description']}'): "
    ).strip()


    if new_description:

        expense["description"] = (
            new_description.title()
        )


    while True:

        new_amount = input(
            f"New amount "
            f"(press Enter to keep "
            f"₹{expense['amount']:,.2f}): "
        ).strip()


        if new_amount == "":
            break


        try:

            new_amount = float(new_amount)

            if new_amount <= 0:

                print(
                    "Amount must be greater than 0."
                )

                continue


            expense["amount"] = new_amount
            break


        except ValueError:

            print(
                "Please enter a valid amount."
            )


    print("\nAvailable categories:")

    for category in valid_categories:
        print(f"- {category.title()}")


    while True:

        new_category = input(
            f"New category "
            f"(press Enter to keep "
            f"{expense['category'].title()}): "
        ).strip().lower()


        if new_category == "":
            break


        if new_category in valid_categories:

            expense["category"] = new_category
            break


        print("Invalid category.")


    print("\nAvailable months:")

    for month in valid_months:
        print(f"- {month.title()}")


    while True:

        new_month = input(
            f"New month "
            f"(press Enter to keep "
            f"{expense['month']}): "
        ).strip().lower()


        if new_month == "":
            break


        if new_month in valid_months:

            expense["month"] = new_month.title()
            break


        print("Invalid month.")


    print("Expense updated successfully.")


def delete_expense():
    """Delete an expense."""

    print("\n=== Delete Expense ===")

    try:

        expense_id = int(
            input("Enter expense ID: ").strip()
        )

    except ValueError:

        print("Please enter a valid ID.")
        return


    expense = find_expense(expense_id)


    if expense is None:

        print("Expense not found.")
        return


    expenses.remove(expense)


    print(
        f"Expense "
        f"'{expense['description']}' "
        f"deleted successfully."
    )


def search_expenses():
    """Search expenses by description or category."""

    print("\n=== Search Expenses ===")

    search_term = input(
        "Search by description or category: "
    ).strip().lower()


    if not search_term:

        print("Search term cannot be empty.")
        return


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
        return


    print("\n=== Search Results ===")


    for expense in matching_expenses:

        print(
            f"[{expense['id']}] "
            f"{expense['description']} | "
            f"₹{expense['amount']:,.2f} | "
            f"{expense['category'].title()} | "
            f"{expense['month']}"
        )


def filter_expenses_by_category():
    """Display expenses belonging to a selected category."""

    print("\n=== Filter by Category ===")

    print("\nAvailable categories:")

    for category in valid_categories:
        print(f"- {category.title()}")


    category = input(
        "Enter category: "
    ).strip().lower()


    if category not in valid_categories:

        print("Invalid category.")
        return


    matching_expenses = [

        expense

        for expense in expenses

        if expense["category"] == category
    ]


    if not matching_expenses:

        print(
            "No expenses found in this category."
        )

        return


    total = sum(
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
        f"₹{total:,.2f}"
    )


def calculate_expense_summary():
    """Calculate and return overall expense statistics."""

    if not expenses:

        return {
            "count": 0,
            "total": 0,
            "average": 0,
            "highest": None,
            "lowest": None
        }


    amounts = [
        expense["amount"]
        for expense in expenses
    ]


    total = sum(amounts)


    average = calculate_average(
        amounts
    )


    highest = max(
        expenses,
        key=get_expense_amount
    )


    lowest = min(
        expenses,
        key=get_expense_amount
    )


    return {
        "count": len(expenses),
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest
    }


def show_expense_summary():
    """Display the overall expense summary."""

    print("\n=== Expense Summary ===")


    summary = calculate_expense_summary()


    if summary["count"] == 0:

        print("No expenses available.")
        return


    print(
        f"Number of expenses: "
        f"{summary['count']}"
    )


    print(
        f"Total spending: "
        f"₹{summary['total']:,.2f}"
    )


    print(
        f"Average expense: "
        f"₹{summary['average']:,.2f}"
    )


    print(
        f"Highest expense: "
        f"{summary['highest']['description']} "
        f"(₹{summary['highest']['amount']:,.2f})"
    )


    print(
        f"Lowest expense: "
        f"{summary['lowest']['description']} "
        f"(₹{summary['lowest']['amount']:,.2f})"
    )


def calculate_monthly_summary():
    """Group expenses by month and calculate totals."""

    monthly_data = {}


    for expense in expenses:

        month = expense["month"]


        if month not in monthly_data:

            monthly_data[month] = {
                "count": 0,
                "total": 0
            }


        monthly_data[month]["count"] += 1

        monthly_data[month]["total"] += (
            expense["amount"]
        )


    return monthly_data


def show_monthly_summary():
    """Display monthly expense statistics."""

    print("\n=== Monthly Summary ===")


    monthly_data = calculate_monthly_summary()


    if not monthly_data:

        print("No expenses available.")
        return


    ranked_months = sorted(
        monthly_data.items(),
        key=lambda item: item[1]["total"],
        reverse=True
    )


    for month, data in ranked_months:

        average = (
            data["total"]
            / data["count"]
        )


        print(
            f"\n{month}"
        )

        print(
            f"  Expenses: "
            f"{data['count']}"
        )

        print(
            f"  Total: "
            f"₹{data['total']:,.2f}"
        )

        print(
            f"  Average: "
            f"₹{average:,.2f}"
        )


def calculate_category_summary():
    """Group expenses by category."""

    category_data = {}


    for expense in expenses:

        category = expense["category"]


        if category not in category_data:

            category_data[category] = {
                "count": 0,
                "total": 0
            }


        category_data[category]["count"] += 1

        category_data[category]["total"] += (
            expense["amount"]
        )


    return category_data


def show_category_summary():
    """Display spending by category."""

    print("\n=== Category Summary ===")


    category_data = calculate_category_summary()


    if not category_data:

        print("No expenses available.")
        return


    ranked_categories = sorted(
        category_data.items(),
        key=lambda item: item[1]["total"],
        reverse=True
    )


    for category, data in ranked_categories:

        average = (
            data["total"]
            / data["count"]
        )


        print(
            f"\n{category.title()}"
        )

        print(
            f"  Expenses: "
            f"{data['count']}"
        )

        print(
            f"  Total: "
            f"₹{data['total']:,.2f}"
        )

        print(
            f"  Average: "
            f"₹{average:,.2f}"
        )


def show_budget_analysis():
    """Analyze total spending against a user-defined budget."""

    print("\n=== Budget Analysis ===")


    while True:

        try:

            budget = float(
                input("Enter your budget: ₹").strip()
            )


            if budget <= 0:

                print(
                    "Budget must be greater than 0."
                )

                continue


            break


        except ValueError:

            print(
                "Please enter a valid amount."
            )


    summary = calculate_expense_summary()


    total_spending = summary["total"]


    remaining = budget - total_spending


    spending_percentage = (
        total_spending
        / budget
        * 100
    )


    print(
        f"\nBudget: "
        f"₹{budget:,.2f}"
    )


    print(
        f"Total spending: "
        f"₹{total_spending:,.2f}"
    )


    print(
        f"Spending percentage: "
        f"{spending_percentage:.2f}%"
    )


    if remaining > 0:

        print(
            f"Remaining budget: "
            f"₹{remaining:,.2f}"
        )


    elif remaining == 0:

        print("Budget fully used.")


    else:

        print(
            f"Budget exceeded by: "
            f"₹{abs(remaining):,.2f}"
        )


    spending_level = (
        calculate_grade_from_spending(
            total_spending
        )
    )


    print(
        f"Spending level: "
        f"{spending_level}"
    )


def show_detailed_report():
    """Display a complete expense report."""

    print("\n========================================")
    print("       DETAILED EXPENSE REPORT")
    print("========================================")


    summary = calculate_expense_summary()


    if summary["count"] == 0:

        print("\nNo expenses available.")
        return


    print(
        f"\nTotal expenses   : "
        f"{summary['count']}"
    )


    print(
        f"Total spending   : "
        f"₹{summary['total']:,.2f}"
    )


    print(
        f"Average expense  : "
        f"₹{summary['average']:,.2f}"
    )


    print(
        f"Highest expense  : "
        f"{summary['highest']['description']} "
        f"(₹{summary['highest']['amount']:,.2f})"
    )


    print(
        f"Lowest expense   : "
        f"{summary['lowest']['description']} "
        f"(₹{summary['lowest']['amount']:,.2f})"
    )


    print("\nCategory breakdown:")

    category_data = calculate_category_summary()


    for category, data in sorted(
        category_data.items(),
        key=lambda item: item[1]["total"],
        reverse=True
    ):

        print(
            f"- {category.title()}: "
            f"₹{data['total']:,.2f}"
        )


    print("\nMonthly breakdown:")

    monthly_data = calculate_monthly_summary()


    for month, data in sorted(
        monthly_data.items(),
        key=lambda item: item[1]["total"],
        reverse=True
    ):

        print(
            f"- {month}: "
            f"₹{data['total']:,.2f}"
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


# ============================================================
# Main Program
# ============================================================

while True:

    print("\n=== Menu ===")
    print("1. View expenses")
    print("2. Add expense")
    print("3. Update expense")
    print("4. Delete expense")
    print("5. Search expenses")
    print("6. Filter by category")
    print("7. Expense summary")
    print("8. Monthly summary")
    print("9. Category summary")
    print("10. Budget analysis")
    print("11. Detailed report")
    print("12. Exit")


    choice = input(
        "Choose an option: "
    ).strip()


    if choice == "1":

        view_expenses()


    elif choice == "2":

        add_expense()


    elif choice == "3":

        update_expense()


    elif choice == "4":

        delete_expense()


    elif choice == "5":

        search_expenses()


    elif choice == "6":

        filter_expenses_by_category()


    elif choice == "7":

        show_expense_summary()


    elif choice == "8":

        show_monthly_summary()


    elif choice == "9":

        show_category_summary()


    elif choice == "10":

        show_budget_analysis()


    elif choice == "11":

        show_detailed_report()


    elif choice == "12":

        print("\nGoodbye!")
        break


    else:

        print(
            "Invalid option. "
            "Please choose between 1 and 12."
        )