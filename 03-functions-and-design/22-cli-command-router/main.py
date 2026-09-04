print("=== CLI Command Router ===")


# ============================================================
# Task Data
# ============================================================

tasks = [
    {
        "id": 1,
        "title": "Learn Python functions",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 2,
        "title": "Build mini project",
        "priority": "medium",
        "status": "pending"
    },
    {
        "id": 3,
        "title": "Read Python documentation",
        "priority": "low",
        "status": "completed"
    }
]


next_task_id = 4

valid_priorities = [
    "low",
    "medium",
    "high"
]


# ============================================================
# Helper Functions
# ============================================================

def find_task(task_id):
    """
    Find and return a task by ID.
    """

    for task in tasks:

        if task["id"] == task_id:
            return task

    return None


def display_task(task):
    """
    Display a single task.
    """

    print(
        f"[{task['id']}] "
        f"{task['title']} | "
        f"Priority: {task['priority'].title()} | "
        f"Status: {task['status'].title()}"
    )


def parse_task_id(value):
    """
    Convert a string into an integer task ID.

    Return None if conversion fails.
    """

    try:
        return int(value)

    except ValueError:
        return None


# ============================================================
# Task Commands
# ============================================================

def add_task(arguments):
    """
    Add a new task.

    Usage:
        add Task title | priority
    """

    global next_task_id


    if not arguments:

        print(
            "Usage: add <task title> | <priority>"
        )

        return


    parts = arguments.split("|")


    title = parts[0].strip()


    if not title:

        print("Task title cannot be empty.")
        return


    if len(parts) >= 2:

        priority = parts[1].strip().lower()

    else:

        priority = "medium"


    if priority not in valid_priorities:

        print(
            "Invalid priority. "
            "Use low, medium, or high."
        )

        return


    task = {
        "id": next_task_id,
        "title": title,
        "priority": priority,
        "status": "pending"
    }


    tasks.append(task)


    print(
        f"Task added successfully "
        f"with ID {next_task_id}."
    )


    next_task_id += 1


def list_tasks(arguments):
    """
    Display tasks.

    Optional arguments:
        pending
        completed
        low
        medium
        high
    """

    filtered_tasks = tasks


    if arguments:

        filter_value = arguments.strip().lower()


        if filter_value in [
            "pending",
            "completed"
        ]:

            filtered_tasks = [
                task
                for task in tasks
                if task["status"] == filter_value
            ]


        elif filter_value in valid_priorities:

            filtered_tasks = [
                task
                for task in tasks
                if task["priority"] == filter_value
            ]


        else:

            print(
                "Invalid filter. "
                "Use pending, completed, low, medium, or high."
            )

            return


    print("\n=== Tasks ===")


    if not filtered_tasks:

        print("No tasks found.")
        return


    for task in filtered_tasks:

        display_task(task)


def complete_task(arguments):
    """
    Mark a task as completed.

    Usage:
        complete <task id>
    """

    if not arguments:

        print(
            "Usage: complete <task id>"
        )

        return


    task_id = parse_task_id(
        arguments.strip()
    )


    if task_id is None:

        print("Task ID must be a number.")
        return


    task = find_task(task_id)


    if task is None:

        print("Task not found.")
        return


    if task["status"] == "completed":

        print("Task is already completed.")
        return


    task["status"] = "completed"


    print(
        f"Task {task_id} marked as completed."
    )


def reopen_task(arguments):
    """
    Reopen a completed task.

    Usage:
        reopen <task id>
    """

    if not arguments:

        print(
            "Usage: reopen <task id>"
        )

        return


    task_id = parse_task_id(
        arguments.strip()
    )


    if task_id is None:

        print("Task ID must be a number.")
        return


    task = find_task(task_id)


    if task is None:

        print("Task not found.")
        return


    if task["status"] == "pending":

        print("Task is already pending.")
        return


    task["status"] = "pending"


    print(
        f"Task {task_id} reopened."
    )


def delete_task(arguments):
    """
    Delete a task.

    Usage:
        delete <task id>
    """

    if not arguments:

        print(
            "Usage: delete <task id>"
        )

        return


    task_id = parse_task_id(
        arguments.strip()
    )


    if task_id is None:

        print("Task ID must be a number.")
        return


    task = find_task(task_id)


    if task is None:

        print("Task not found.")
        return


    tasks.remove(task)


    print(
        f"Task {task_id} deleted successfully."
    )


def search_tasks(arguments):
    """
    Search tasks by title.

    Usage:
        search <keyword>
    """

    search_term = arguments.strip().lower()


    if not search_term:

        print(
            "Usage: search <keyword>"
        )

        return


    matching_tasks = [
        task
        for task in tasks
        if search_term in task["title"].lower()
    ]


    print("\n=== Search Results ===")


    if not matching_tasks:

        print("No matching tasks found.")
        return


    for task in matching_tasks:

        display_task(task)


def show_task(arguments):
    """
    Show one task.

    Usage:
        show <task id>
    """

    if not arguments:

        print(
            "Usage: show <task id>"
        )

        return


    task_id = parse_task_id(
        arguments.strip()
    )


    if task_id is None:

        print("Task ID must be a number.")
        return


    task = find_task(task_id)


    if task is None:

        print("Task not found.")
        return


    print("\n=== Task ===")

    display_task(task)


def show_stats(arguments):
    """
    Display task statistics.
    """

    total_tasks = len(tasks)


    completed_tasks = sum(
        1
        for task in tasks
        if task["status"] == "completed"
    )


    pending_tasks = sum(
        1
        for task in tasks
        if task["status"] == "pending"
    )


    priority_counts = {}


    for task in tasks:

        priority = task["priority"]

        priority_counts[priority] = (
            priority_counts.get(priority, 0) + 1
        )


    print("\n=== Task Statistics ===")


    print(
        f"Total tasks: "
        f"{total_tasks}"
    )


    print(
        f"Pending tasks: "
        f"{pending_tasks}"
    )


    print(
        f"Completed tasks: "
        f"{completed_tasks}"
    )


    print("\nTasks by priority:")


    for priority, count in sorted(
        priority_counts.items()
    ):

        print(
            f"- {priority.title()}: "
            f"{count}"
        )


def clear_completed(arguments):
    """
    Delete all completed tasks.
    """

    completed_tasks = [
        task
        for task in tasks
        if task["status"] == "completed"
    ]


    if not completed_tasks:

        print("No completed tasks to clear.")
        return


    for task in completed_tasks:

        tasks.remove(task)


    print(
        f"Removed "
        f"{len(completed_tasks)} "
        f"completed task(s)."
    )


# ============================================================
# Help and Information
# ============================================================

def show_help(arguments):
    """
    Display available commands.
    """

    print("\n=== Available Commands ===")

    print(
        "add <title> | <priority>"
        "  Add a new task"
    )

    print(
        "list [filter]"
        "                     List tasks"
    )

    print(
        "show <id>"
        "                       Show one task"
    )

    print(
        "complete <id>"
        "                   Complete a task"
    )

    print(
        "reopen <id>"
        "                     Reopen a task"
    )

    print(
        "delete <id>"
        "                     Delete a task"
    )

    print(
        "search <keyword>"
        "                Search tasks"
    )

    print(
        "stats"
        "                          Show statistics"
    )

    print(
        "clear-completed"
        "                Remove completed tasks"
    )

    print(
        "help"
        "                           Show this help"
    )

    print(
        "exit"
        "                           Exit program"
    )


def show_command_info(arguments):
    """
    Display information about a specific command.

    Usage:
        info <command>
    """

    command_name = arguments.strip().lower()


    command_information = {

        "add":
            "add <title> | <priority>",

        "list":
            "list [pending|completed|low|medium|high]",

        "show":
            "show <task id>",

        "complete":
            "complete <task id>",

        "reopen":
            "reopen <task id>",

        "delete":
            "delete <task id>",

        "search":
            "search <keyword>",

        "stats":
            "stats",

        "clear-completed":
            "clear-completed",

        "help":
            "help"

    }


    if command_name in command_information:

        print(
            f"\nUsage: "
            f"{command_information[command_name]}"
        )

    else:

        print(
            f"No information available "
            f"for '{command_name}'."
        )


# ============================================================
# Command Router
# ============================================================

commands = {
    "add": add_task,
    "list": list_tasks,
    "show": show_task,
    "complete": complete_task,
    "reopen": reopen_task,
    "delete": delete_task,
    "search": search_tasks,
    "stats": show_stats,
    "clear-completed": clear_completed,
    "help": show_help,
    "info": show_command_info
}


# ============================================================
# Command Loop
# ============================================================

print("\nType 'help' to see available commands.")


while True:

    command_line = input("\n> ").strip()


    if not command_line:

        continue


    parts = command_line.split(
        maxsplit=1
    )


    command_name = parts[0].lower()


    if len(parts) > 1:

        arguments = parts[1]

    else:

        arguments = ""


    if command_name == "exit":

        print("Goodbye!")
        break


    command_function = commands.get(
        command_name
    )


    if command_function is None:

        print(
            f"Unknown command: "
            f"'{command_name}'"
        )

        print(
            "Type 'help' to see available commands."
        )

        continue


    command_function(arguments)