print("=== Terminal Productivity Suite ===")


# ============================================================
# Application Data
# ============================================================

tasks = []
notes = []
expenses = []

next_task_id = 1
next_note_id = 1
next_expense_id = 1

valid_priorities = ["low", "medium", "high"]
valid_expense_categories = [
    "food",
    "transport",
    "shopping",
    "bills",
    "entertainment",
    "other"
]


# ============================================================
# Main Application
# ============================================================

while True:
    print("\n=== Main Menu ===")
    print("1. Task Manager")
    print("2. Notes Manager")
    print("3. Expense Tracker")
    print("4. Dashboard")
    print("5. Search Everything")
    print("6. Exit")

    choice = input("Choose an option: ").strip()

    # ========================================================
    # TASK MANAGER
    # ========================================================

    if choice == "1":

        while True:
            print("\n=== Task Manager ===")
            print("1. View tasks")
            print("2. Add task")
            print("3. Mark task as completed")
            print("4. Delete task")
            print("5. Back")

            task_choice = input("Choose an option: ").strip()

            # View tasks
            if task_choice == "1":
                if not tasks:
                    print("\nNo tasks available.")
                    continue

                print("\n=== Tasks ===")

                for task in tasks:
                    print(
                        f"[{task['id']}] "
                        f"{task['title']} | "
                        f"Priority: {task['priority'].title()} | "
                        f"Status: {task['status'].title()}"
                    )

            # Add task
            elif task_choice == "2":
                title = input("Task title: ").strip()

                if not title:
                    print("Task title cannot be empty.")
                    continue

                while True:
                    priority = input(
                        "Priority (low / medium / high): "
                    ).strip().lower()

                    if priority in valid_priorities:
                        break

                    print(
                        "Invalid priority. "
                        "Choose low, medium, or high."
                    )

                task = {
                    "id": next_task_id,
                    "title": title,
                    "priority": priority,
                    "status": "pending"
                }

                tasks.append(task)
                next_task_id += 1

                print(
                    f"Task #{task['id']} "
                    "added successfully."
                )

            # Complete task
            elif task_choice == "3":
                if not tasks:
                    print("\nNo tasks available.")
                    continue

                try:
                    task_id = int(
                        input("Enter task ID: ")
                    )

                    task_found = False

                    for task in tasks:
                        if task["id"] == task_id:

                            if task["status"] == "completed":
                                print(
                                    "Task is already completed."
                                )
                            else:
                                task["status"] = "completed"
                                print(
                                    "Task marked as completed."
                                )

                            task_found = True
                            break

                    if not task_found:
                        print("Task ID not found.")

                except ValueError:
                    print("Please enter a valid task ID.")

            # Delete task
            elif task_choice == "4":
                if not tasks:
                    print("\nNo tasks available.")
                    continue

                try:
                    task_id = int(
                        input("Enter task ID to delete: ")
                    )

                    task_found = False

                    for task in tasks:
                        if task["id"] == task_id:
                            tasks.remove(task)
                            print(
                                "Task deleted successfully."
                            )
                            task_found = True
                            break

                    if not task_found:
                        print("Task ID not found.")

                except ValueError:
                    print("Please enter a valid task ID.")

            # Back
            elif task_choice == "5":
                break

            else:
                print(
                    "Invalid option. "
                    "Please choose between 1 and 5."
                )

    # ========================================================
    # NOTES MANAGER
    # ========================================================

    elif choice == "2":

        while True:
            print("\n=== Notes Manager ===")
            print("1. View notes")
            print("2. Add note")
            print("3. Delete note")
            print("4. Back")

            note_choice = input("Choose an option: ").strip()

            # View notes
            if note_choice == "1":
                if not notes:
                    print("\nNo notes available.")
                    continue

                print("\n=== Notes ===")

                for note in notes:
                    print(f"\n[{note['id']}] {note['title']}")
                    print(f"    {note['content']}")

            # Add note
            elif note_choice == "2":
                title = input("Note title: ").strip()

                if not title:
                    print("Note title cannot be empty.")
                    continue

                content = input("Note content: ").strip()

                if not content:
                    print("Note content cannot be empty.")
                    continue

                note = {
                    "id": next_note_id,
                    "title": title,
                    "content": content
                }

                notes.append(note)
                next_note_id += 1

                print(
                    f"Note #{note['id']} "
                    "added successfully."
                )

            # Delete note
            elif note_choice == "3":
                if not notes:
                    print("\nNo notes available.")
                    continue

                try:
                    note_id = int(
                        input("Enter note ID to delete: ")
                    )

                    note_found = False

                    for note in notes:
                        if note["id"] == note_id:
                            notes.remove(note)
                            print(
                                "Note deleted successfully."
                            )
                            note_found = True
                            break

                    if not note_found:
                        print("Note ID not found.")

                except ValueError:
                    print("Please enter a valid note ID.")

            # Back
            elif note_choice == "4":
                break

            else:
                print(
                    "Invalid option. "
                    "Please choose between 1 and 4."
                )

    # ========================================================
    # EXPENSE TRACKER
    # ========================================================

    elif choice == "3":

        while True:
            print("\n=== Expense Tracker ===")
            print("1. View expenses")
            print("2. Add expense")
            print("3. Delete expense")
            print("4. Back")

            expense_choice = input(
                "Choose an option: "
            ).strip()

            # View expenses
            if expense_choice == "1":
                if not expenses:
                    print("\nNo expenses recorded.")
                    continue

                print("\n=== Expenses ===")

                for expense in expenses:
                    print(
                        f"[{expense['id']}] "
                        f"{expense['category'].title()} | "
                        f"₹{expense['amount']:.2f}"
                    )

                total_expenses = sum(
                    expense["amount"]
                    for expense in expenses
                )

                print(
                    f"\nTotal spending: "
                    f"₹{total_expenses:.2f}"
                )

            # Add expense
            elif expense_choice == "2":
                while True:
                    category = input(
                        "Category "
                        "(food / transport / shopping / "
                        "bills / entertainment / other): "
                    ).strip().lower()

                    if category in valid_expense_categories:
                        break

                    print("Invalid category.")

                try:
                    amount = float(
                        input("Amount: ₹")
                    )

                    if amount <= 0:
                        print(
                            "Amount must be greater than 0."
                        )
                        continue

                except ValueError:
                    print("Please enter a valid amount.")
                    continue

                expense = {
                    "id": next_expense_id,
                    "category": category,
                    "amount": amount
                }

                expenses.append(expense)
                next_expense_id += 1

                print(
                    f"Expense #{expense['id']} "
                    "added successfully."
                )

            # Delete expense
            elif expense_choice == "3":
                if not expenses:
                    print("\nNo expenses recorded.")
                    continue

                try:
                    expense_id = int(
                        input("Enter expense ID to delete: ")
                    )

                    expense_found = False

                    for expense in expenses:
                        if expense["id"] == expense_id:
                            expenses.remove(expense)
                            print(
                                "Expense deleted successfully."
                            )
                            expense_found = True
                            break

                    if not expense_found:
                        print("Expense ID not found.")

                except ValueError:
                    print(
                        "Please enter a valid expense ID."
                    )

            # Back
            elif expense_choice == "4":
                break

            else:
                print(
                    "Invalid option. "
                    "Please choose between 1 and 4."
                )

    # ========================================================
    # DASHBOARD
    # ========================================================

    elif choice == "4":

        total_tasks = len(tasks)
        completed_tasks = 0
        pending_tasks = 0

        priority_counts = {
            "low": 0,
            "medium": 0,
            "high": 0
        }

        for task in tasks:
            if task["status"] == "completed":
                completed_tasks += 1
            else:
                pending_tasks += 1

            priority_counts[task["priority"]] += 1

        total_notes = len(notes)

        total_expenses = sum(
            expense["amount"]
            for expense in expenses
        )

        expense_count = len(expenses)

        print("\n=== Productivity Dashboard ===")

        print("\nTasks")
        print(f"Total: {total_tasks}")
        print(f"Completed: {completed_tasks}")
        print(f"Pending: {pending_tasks}")

        print("By priority:")
        print(f"- Low: {priority_counts['low']}")
        print(f"- Medium: {priority_counts['medium']}")
        print(f"- High: {priority_counts['high']}")

        print("\nNotes")
        print(f"Total notes: {total_notes}")

        print("\nExpenses")
        print(f"Transactions: {expense_count}")
        print(f"Total spent: ₹{total_expenses:.2f}")

    # ========================================================
    # GLOBAL SEARCH
    # ========================================================

    elif choice == "5":

        search_term = input(
            "Search tasks and notes: "
        ).strip().lower()

        if not search_term:
            print("Search term cannot be empty.")
            continue

        task_matches = []
        note_matches = []

        # Search tasks
        for task in tasks:
            if search_term in task["title"].lower():
                task_matches.append(task)

        # Search notes
        for note in notes:
            if (
                search_term in note["title"].lower()
                or search_term in note["content"].lower()
            ):
                note_matches.append(note)

        print("\n=== Search Results ===")

        if task_matches:
            print("\nTasks:")

            for task in task_matches:
                print(
                    f"- [{task['id']}] "
                    f"{task['title']} | "
                    f"{task['status'].title()}"
                )

        if note_matches:
            print("\nNotes:")

            for note in note_matches:
                print(
                    f"- [{note['id']}] "
                    f"{note['title']}"
                )

        if not task_matches and not note_matches:
            print("No matching tasks or notes found.")

    # ========================================================
    # EXIT
    # ========================================================

    elif choice == "6":
        print("\nGoodbye!")
        break

    else:
        print(
            "Invalid option. "
            "Please choose between 1 and 6."
        )

