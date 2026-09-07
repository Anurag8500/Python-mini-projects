import csv
from pathlib import Path


print("=== CSV Data Analyzer ===")


# ============================================================
# File Functions
# ============================================================

def load_csv(file_path):
    """Load a CSV file and return rows as dictionaries."""

    path = Path(file_path)

    if not path.exists():
        print("CSV file does not exist.")
        return None

    if not path.is_file():
        print("The provided path is not a file.")
        return None

    try:
        with path.open(
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            rows = list(reader)

        return rows

    except OSError as error:

        print(f"Could not read CSV file: {error}")
        return None


def save_csv(file_path, rows):
    """Save rows of dictionaries to a CSV file."""

    if not rows:
        print("There is no data to export.")
        return

    try:
        with Path(file_path).open(
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=rows[0].keys()
            )

            writer.writeheader()
            writer.writerows(rows)

        print(
            f"Data exported successfully to "
            f"{file_path}"
        )

    except OSError as error:

        print(f"Could not write CSV file: {error}")


# ============================================================
# Data Conversion
# ============================================================

def convert_numeric_columns(rows):
    """
    Convert salary and experience values from strings
    into numbers.
    """

    for row in rows:

        try:
            row["salary"] = float(row["salary"])
            row["experience"] = int(row["experience"])

        except (ValueError, KeyError):
            continue


# ============================================================
# Display Functions
# ============================================================

def show_records(rows):
    """Display all records."""

    if not rows:
        print("No records found.")
        return

    print("\n=== Records ===")

    for row in rows:

        print(
            f"[{row['id']}] "
            f"{row['name']} | "
            f"{row['department']} | "
            f"₹{float(row['salary']):,.2f} | "
            f"{row['experience']} years"
        )


def show_columns(rows):
    """Display CSV column names."""

    if not rows:
        print("No records available.")
        return

    print("\n=== Columns ===")

    for number, column in enumerate(
        rows[0].keys(),
        start=1
    ):

        print(
            f"{number}. {column}"
        )


# ============================================================
# Search and Filtering
# ============================================================

def search_records(rows):
    """Search across all columns."""

    keyword = input(
        "Enter search keyword: "
    ).strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    matching_rows = []

    for row in rows:

        if any(
            keyword in str(value).lower()
            for value in row.values()
        ):

            matching_rows.append(row)

    print("\n=== Search Results ===")

    show_records(matching_rows)


def filter_by_department(rows):
    """Filter employees by department."""

    department = input(
        "Enter department: "
    ).strip().lower()

    if not department:
        print("Department cannot be empty.")
        return

    matching_rows = [
        row
        for row in rows
        if row["department"].lower() == department
    ]

    print("\n=== Filter Results ===")

    show_records(matching_rows)


def filter_by_salary(rows):
    """Filter employees by salary range."""

    try:

        minimum = float(
            input("Minimum salary: ₹").strip()
        )

        maximum = float(
            input("Maximum salary: ₹").strip()
        )

    except ValueError:

        print("Please enter valid numbers.")
        return


    if minimum > maximum:

        print(
            "Minimum salary cannot exceed "
            "maximum salary."
        )

        return


    matching_rows = [
        row
        for row in rows
        if minimum
        <= float(row["salary"])
        <= maximum
    ]


    print("\n=== Salary Filter Results ===")

    show_records(matching_rows)


# ============================================================
# Sorting
# ============================================================

def sort_records(rows):
    """Sort records by a selected field."""

    print("\n=== Sort By ===")
    print("1. Name")
    print("2. Salary")
    print("3. Experience")


    choice = input(
        "Choose field: "
    ).strip()


    print("\n1. Ascending")
    print("2. Descending")


    order = input(
        "Choose order: "
    ).strip()


    if order == "1":
        reverse = False

    elif order == "2":
        reverse = True

    else:
        print("Invalid order.")
        return


    if choice == "1":

        sorted_rows = sorted(
            rows,
            key=lambda row:
                row["name"].lower(),
            reverse=reverse
        )

    elif choice == "2":

        sorted_rows = sorted(
            rows,
            key=lambda row:
                float(row["salary"]),
            reverse=reverse
        )

    elif choice == "3":

        sorted_rows = sorted(
            rows,
            key=lambda row:
                int(row["experience"]),
            reverse=reverse
        )

    else:

        print("Invalid field.")
        return


    print("\n=== Sorted Results ===")

    show_records(sorted_rows)


# ============================================================
# Statistics
# ============================================================

def show_statistics(rows):
    """Display numeric statistics."""

    if not rows:
        print("No records available.")
        return


    salaries = [
        float(row["salary"])
        for row in rows
    ]


    experience_values = [
        int(row["experience"])
        for row in rows
    ]


    average_salary = (
        sum(salaries)
        / len(salaries)
    )


    highest_paid = max(
        rows,
        key=lambda row:
            float(row["salary"])
    )


    lowest_paid = min(
        rows,
        key=lambda row:
            float(row["salary"])
    )


    most_experienced = max(
        rows,
        key=lambda row:
            int(row["experience"])
    )


    print("\n=== Column Statistics ===")

    print(
        f"Employee count: "
        f"{len(rows)}"
    )

    print(
        f"Average salary: "
        f"₹{average_salary:,.2f}"
    )

    print(
        f"Highest salary: "
        f"{highest_paid['name']} "
        f"(₹{float(highest_paid['salary']):,.2f})"
    )

    print(
        f"Lowest salary: "
        f"{lowest_paid['name']} "
        f"(₹{float(lowest_paid['salary']):,.2f})"
    )

    print(
        f"Highest experience: "
        f"{most_experienced['name']} "
        f"({most_experienced['experience']} years)"
    )


# ============================================================
# Grouping
# ============================================================

def show_department_summary(rows):
    """Group employees by department."""

    department_data = {}


    for row in rows:

        department = row["department"]


        if department not in department_data:

            department_data[department] = {
                "employees": 0,
                "salary_total": 0
            }


        department_data[department]["employees"] += 1

        department_data[department]["salary_total"] += (
            float(row["salary"])
        )


    print("\n=== Department Summary ===")


    ranked_departments = sorted(
        department_data.items(),
        key=lambda item:
            item[1]["salary_total"],
        reverse=True
    )


    for department, data in ranked_departments:

        average_salary = (
            data["salary_total"]
            / data["employees"]
        )


        print(
            f"\n{department}"
        )

        print(
            f"  Employees: "
            f"{data['employees']}"
        )

        print(
            f"  Salary total: "
            f"₹{data['salary_total']:,.2f}"
        )

        print(
            f"  Average salary: "
            f"₹{average_salary:,.2f}"
        )


# ============================================================
# Dataset Summary
# ============================================================

def show_dataset_summary(rows):
    """Display a high-level dataset summary."""

    if not rows:
        print("No data available.")
        return


    print("\n=== Dataset Summary ===")


    print(
        f"Rows: "
        f"{len(rows)}"
    )


    print(
        f"Columns: "
        f"{len(rows[0])}"
    )


    print(
        "Column names: "
        f"{', '.join(rows[0].keys())}"
    )


# ============================================================
# Main Program
# ============================================================

file_path = input(
    "Enter CSV file path "
    "(example: data/employees.csv): "
).strip()


if not file_path:

    print("File path cannot be empty.")

else:

    data = load_csv(file_path)


    if data is not None:

        convert_numeric_columns(data)


        while True:

            print("\n=== Menu ===")
            print("1. View records")
            print("2. Show columns")
            print("3. Dataset summary")
            print("4. Search records")
            print("5. Filter by department")
            print("6. Filter by salary")
            print("7. Sort records")
            print("8. Column statistics")
            print("9. Department summary")
            print("10. Export current data")
            print("11. Exit")


            choice = input(
                "Choose an option: "
            ).strip()


            if choice == "1":

                show_records(data)


            elif choice == "2":

                show_columns(data)


            elif choice == "3":

                show_dataset_summary(data)


            elif choice == "4":

                search_records(data)


            elif choice == "5":

                filter_by_department(data)


            elif choice == "6":

                filter_by_salary(data)


            elif choice == "7":

                sort_records(data)


            elif choice == "8":

                show_statistics(data)


            elif choice == "9":

                show_department_summary(data)


            elif choice == "10":

                output_path = input(
                    "Output CSV path: "
                ).strip()


                if output_path:

                    save_csv(
                        output_path,
                        data
                    )

                else:

                    print(
                        "Output path cannot be empty."
                    )


            elif choice == "11":

                print("\nGoodbye!")
                break


            else:

                print(
                    "Invalid option. "
                    "Please choose between 1 and 11."
                )