print("=== Personal Productivity CLI ===")


# ============================================================
# Data
# ============================================================

tasks = []
notes = []
expenses = []

next_task_id = 1
next_note_id = 1
next_expense_id = 1


# ============================================================
# Helpers
# ============================================================

def find_by_id(records, record_id):
    """Return a record with the given ID."""

    for record in records:
        if record["id"] == record_id:
            return record

    return None


def print_task(task):
    print(
        f"[{task['id']}] "
        f"{task['title']} | "
        f"{task['priority'].title()} | "
        f"{task['status'].title()}"
    )


def print_note(note):
    print(
        f"[{note['id']}] "
        f"{note['title']} | "
        f"{note['content']}"
    )


def print_expense(expense):
    print(
        f"[{expense['id']}] "
        f"{expense['description']} | "
        f"₹{expense['amount']:,.2f} | "
        f"{expense['category'].title()}"
    )


# ============================================================
# Task Functions
# ============================================================

def add_task(arguments):
    global next_task_id

    parts = arguments.split("|")

    title = parts[0].strip()

    if not title:
        print("Task title cannot be empty.")
        return

    priority = "medium"

    if len(parts) > 1 and parts[1].strip():
        priority = parts[1].strip().lower()

    if priority not in ["low", "medium", "high"]:
        print("Priority must be low, medium, or high.")
        return

    task = {
        "id": next_task_id,
        "title": title,
        "priority": priority,
        "status": "pending"
    }

    tasks.append(task)

    print(f"Task added with ID {next_task_id}.")
    next_task_id += 1


def list_tasks():
    print("\n=== Tasks ===")

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print_task(task)


def complete_task(arguments):
    task_id = parse_id(arguments)

    if task_id is None:
        return

    task = find_by_id(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    task["status"] = "completed"

    print("Task completed.")


def delete_task(arguments):
    task_id = parse_id(arguments)

    if task_id is None:
        return

    task = find_by_id(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    tasks.remove(task)

    print("Task deleted.")


# ============================================================
# Note Functions
# ============================================================

def add_note(arguments):
    global next_note_id

    parts = arguments.split("|", maxsplit=1)

    if len(parts) < 2:
        print("Usage: add-note <title> | <content>")
        return

    title = parts[0].strip()
    content = parts[1].strip()

    if not title or not content:
        print("Title and content are required.")
        return

    note = {
        "id": next_note_id,
        "title": title,
        "content": content
    }

    notes.append(note)

    print(f"Note added with ID {next_note_id}.")
    next_note_id += 1


def list_notes():
    print("\n=== Notes ===")

    if not notes:
        print("No notes found.")
        return

    for note in notes:
        print_note(note)


# ============================================================
# Expense Functions
# ============================================================

def add_expense(arguments):
    global next_expense_id

    parts = arguments.split("|")

    if len(parts) < 3:
        print(
            "Usage: add-expense "
            "<description> | <amount> | <category>"
        )
        return

    description = parts[0].strip()
    amount_text = parts[1].strip()
    category = parts[2].strip().lower()

    if not description:
        print("Description cannot be empty.")
        return

    try:
        amount = float(amount_text)

    except ValueError:
        print("Amount must be a number.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    expense = {
        "id": next_expense_id,
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print(
        f"Expense added with ID "
        f"{next_expense_id}."
    )

    next_expense_id += 1


def list_expenses():
    print("\n=== Expenses ===")

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print_expense(expense)


# ============================================================
# Search
# ============================================================

def search(arguments):
    keyword = arguments.strip().lower()

    if not keyword:
        print("Usage: search <keyword>")
        return

    found = False

    print("\n=== Search Results ===")

    for task in tasks:
        if keyword in task["title"].lower():
            print("Task:", end=" ")
            print_task(task)
            found = True

    for note in notes:
        if (
            keyword in note["title"].lower()
            or keyword in note["content"].lower()
        ):
            print("Note:", end=" ")
            print_note(note)
            found = True

    for expense in expenses:
        if (
            keyword in expense["description"].lower()
            or keyword in expense["category"].lower()
        ):
            print("Expense:", end=" ")
            print_expense(expense)
            found = True

    if not found:
        print("No matching records found.")


# ============================================================
# Statistics
# ============================================================

def show_stats():
    total_expense = sum(
        expense["amount"]
        for expense in expenses
    )

    completed_tasks = sum(
        1
        for task in tasks
        if task["status"] == "completed"
    )

    print("\n=== Statistics ===")

    print(
        f"Tasks: {len(tasks)}"
    )

    print(
        f"Completed tasks: {completed_tasks}"
    )

    print(
        f"Notes: {len(notes)}"
    )

    print(
        f"Expenses: {len(expenses)}"
    )

    print(
        f"Total spending: "
        f"₹{total_expense:,.2f}"
    )


# ============================================================
# General Helpers
# ============================================================

def parse_id(value):
    try:
        return int(value.strip())

    except ValueError:
        print("ID must be a number.")
        return None


def show_help():
    print("\n=== Commands ===")

    print("add-task <title> | <priority>")
    print("list-tasks")
    print("complete <id>")
    print("delete-task <id>")

    print("add-note <title> | <content>")
    print("list-notes")

    print(
        "add-expense "
        "<description> | <amount> | <category>"
    )
    print("list-expenses")

    print("search <keyword>")
    print("stats")
    print("help")
    print("exit")


# ============================================================
# Command Router
# ============================================================

commands = {
    "add-task": add_task,
    "list-tasks": lambda arguments: list_tasks(),
    "complete": complete_task,
    "delete-task": delete_task,

    "add-note": add_note,
    "list-notes": lambda arguments: list_notes(),

    "add-expense": add_expense,
    "list-expenses": lambda arguments: list_expenses(),

    "search": search,
    "stats": lambda arguments: show_stats(),
    "help": lambda arguments: show_help()
}


# ============================================================
# Main Command Loop
# ============================================================

show_help()


while True:

    command_line = input("\n> ").strip()

    if not command_line:
        continue

    parts = command_line.split(
        maxsplit=1
    )

    command_name = parts[0].lower()

    arguments = ""

    if len(parts) > 1:
        arguments = parts[1]

    if command_name == "exit":
        print("Goodbye!")
        break

    command_function = commands.get(
        command_name
    )

    if command_function is None:

        print(
            f"Unknown command: "
            f"{command_name}"
        )

        continue

    command_function(arguments)