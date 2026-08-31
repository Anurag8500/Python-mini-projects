print("=== Mini Task Manager ===")

tasks = []
next_task_id = 1

valid_priorities = ["low", "medium", "high"]

while True:
    print("\n=== Menu ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Search tasks")
    print("6. Filter by status")
    print("7. Filter by priority")
    print("8. Show statistics")
    print("9. Exit")

    choice = input("Choose an option: ").strip()

    # View tasks
    if choice == "1":
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
    elif choice == "2":
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

            print("Invalid priority. Choose low, medium, or high.")

        task = {
            "id": next_task_id,
            "title": title,
            "priority": priority,
            "status": "pending"
        }

        tasks.append(task)
        next_task_id += 1

        print(f"Task #{task['id']} added successfully.")

    # Mark task as completed
    elif choice == "3":
        if not tasks:
            print("\nNo tasks available.")
            continue

        try:
            task_id = int(input("Enter task ID: "))

            task_found = False

            for task in tasks:
                if task["id"] == task_id:
                    if task["status"] == "completed":
                        print("Task is already completed.")
                    else:
                        task["status"] = "completed"
                        print("Task marked as completed.")

                    task_found = True
                    break

            if not task_found:
                print("Task ID not found.")

        except ValueError:
            print("Please enter a valid task ID.")

    # Delete task
    elif choice == "4":
        if not tasks:
            print("\nNo tasks available.")
            continue

        try:
            task_id = int(input("Enter task ID to delete: "))

            task_found = False

            for task in tasks:
                if task["id"] == task_id:
                    tasks.remove(task)
                    print("Task deleted successfully.")
                    task_found = True
                    break

            if not task_found:
                print("Task ID not found.")

        except ValueError:
            print("Please enter a valid task ID.")

    # Search tasks
    elif choice == "5":
        if not tasks:
            print("\nNo tasks available.")
            continue

        search_term = input("Search task: ").strip().lower()

        matching_tasks = []

        for task in tasks:
            if search_term in task["title"].lower():
                matching_tasks.append(task)

        if not matching_tasks:
            print("No matching tasks found.")
            continue

        print("\n=== Search Results ===")

        for task in matching_tasks:
            print(
                f"[{task['id']}] "
                f"{task['title']} | "
                f"Priority: {task['priority'].title()} | "
                f"Status: {task['status'].title()}"
            )

    # Filter by status
    elif choice == "6":
        if not tasks:
            print("\nNo tasks available.")
            continue

        status = input(
            "Enter status (pending / completed): "
        ).strip().lower()

        if status not in ["pending", "completed"]:
            print("Invalid status.")
            continue

        filtered_tasks = [
            task for task in tasks
            if task["status"] == status
        ]

        if not filtered_tasks:
            print(f"No {status} tasks found.")
            continue

        print(f"\n=== {status.title()} Tasks ===")

        for task in filtered_tasks:
            print(
                f"[{task['id']}] "
                f"{task['title']} | "
                f"Priority: {task['priority'].title()}"
            )

    # Filter by priority
    elif choice == "7":
        if not tasks:
            print("\nNo tasks available.")
            continue

        priority = input(
            "Enter priority (low / medium / high): "
        ).strip().lower()

        if priority not in valid_priorities:
            print("Invalid priority.")
            continue

        filtered_tasks = [
            task for task in tasks
            if task["priority"] == priority
        ]

        if not filtered_tasks:
            print(f"No {priority}-priority tasks found.")
            continue

        print(f"\n=== {priority.title()} Priority Tasks ===")

        for task in filtered_tasks:
            print(
                f"[{task['id']}] "
                f"{task['title']} | "
                f"Status: {task['status'].title()}"
            )

    # Statistics
    elif choice == "8":
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

        print("\n=== Task Statistics ===")
        print(f"Total tasks: {total_tasks}")
        print(f"Completed: {completed_tasks}")
        print(f"Pending: {pending_tasks}")

        print("\nBy priority:")
        print(f"- Low: {priority_counts['low']}")
        print(f"- Medium: {priority_counts['medium']}")
        print(f"- High: {priority_counts['high']}")

    # Exit
    elif choice == "9":
        print("\nGoodbye!")
        break

    else:
        print("Invalid option. Please choose between 1 and 9.")
