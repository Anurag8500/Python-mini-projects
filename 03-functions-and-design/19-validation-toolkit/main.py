print("=== Validation Toolkit ===")


# ============================================================
# Validation Functions
# ============================================================

def is_valid_email(email):
    """
    Check whether an email has a basic valid structure.
    """

    email = email.strip().lower()

    if not email:
        return False

    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if not username or not domain:
        return False

    if "." not in domain:
        return False

    if domain.startswith("."):
        return False

    if domain.endswith("."):
        return False

    return True


def is_valid_phone(phone):
    """
    Check whether a phone number contains exactly
    10 digits.
    """

    phone = phone.strip()

    if not phone.isdigit():
        return False

    if len(phone) != 10:
        return False

    return True


def is_valid_username(username):
    """
    Check username rules:
    - 3 to 20 characters
    - starts with a letter
    - contains only letters, numbers, and underscore
    """

    username = username.strip()

    if not 3 <= len(username) <= 20:
        return False

    if not username[0].isalpha():
        return False

    for character in username:

        if not (
            character.isalnum()
            or character == "_"
        ):
            return False

    return True


def is_valid_password(password):
    """
    Check password rules:
    - minimum 8 characters
    - contains uppercase letter
    - contains lowercase letter
    - contains digit
    """

    if len(password) < 8:
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False


    for character in password:

        if character.isupper():
            has_uppercase = True

        elif character.islower():
            has_lowercase = True

        elif character.isdigit():
            has_digit = True


    return (
        has_uppercase
        and has_lowercase
        and has_digit
    )


def is_valid_age(age, minimum=1, maximum=120):
    """
    Check whether an age falls within a valid range.
    """

    if age < minimum:
        return False

    if age > maximum:
        return False

    return True


def is_valid_number(
    value,
    minimum,
    maximum
):
    """
    Check whether a number falls within
    an inclusive range.
    """

    return minimum <= value <= maximum


def is_valid_choice(choice, valid_choices):
    """
    Check whether a user's choice exists
    in a collection of valid choices.
    """

    return choice in valid_choices


def is_valid_date(date_text):
    """
    Check whether a date follows:
    YYYY-MM-DD
    """

    parts = date_text.strip().split("-")

    if len(parts) != 3:
        return False


    year, month, day = parts


    if (
        not year.isdigit()
        or not month.isdigit()
        or not day.isdigit()
    ):

        return False


    year = int(year)
    month = int(month)
    day = int(day)


    if year < 1:
        return False

    if month < 1 or month > 12:
        return False


    days_in_month = [
        31,
        28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31
    ]


    # Leap year handling

    if (
        month == 2
        and (
            year % 400 == 0
            or (
                year % 4 == 0
                and year % 100 != 0
            )
        )
    ):

        maximum_day = 29

    else:

        maximum_day = days_in_month[month - 1]


    return 1 <= day <= maximum_day


def is_valid_name(name):
    """
    Check whether a name contains only alphabetic
    characters and spaces.
    """

    name = name.strip()

    if not name:
        return False

    for character in name:

        if not (
            character.isalpha()
            or character == " "
        ):

            return False

    return True


def validate_user_data(
    name,
    username,
    email,
    phone,
    age,
    password,
    date
):
    """
    Validate multiple user fields and return
    a dictionary containing the results.
    """

    return {
        "name": is_valid_name(name),
        "username": is_valid_username(username),
        "email": is_valid_email(email),
        "phone": is_valid_phone(phone),
        "age": is_valid_age(age),
        "password": is_valid_password(password),
        "date": is_valid_date(date)
    }


# ============================================================
# Display Helper
# ============================================================

def display_validation_result(
    field_name,
    is_valid
):
    """
    Display a validation result.
    """

    if is_valid:
        print(
            f"✓ {field_name}: Valid"
        )

    else:
        print(
            f"✗ {field_name}: Invalid"
        )


# ============================================================
# Validate Email
# ============================================================

def validate_email_interactively():

    print("\n=== Email Validation ===")

    email = input(
        "Enter email: "
    )

    result = is_valid_email(email)

    display_validation_result(
        "Email",
        result
    )


# ============================================================
# Validate Phone
# ============================================================

def validate_phone_interactively():

    print("\n=== Phone Validation ===")

    phone = input(
        "Enter phone number: "
    )

    result = is_valid_phone(phone)

    display_validation_result(
        "Phone",
        result
    )


# ============================================================
# Validate Password
# ============================================================

def validate_password_interactively():

    print("\n=== Password Validation ===")

    password = input(
        "Enter password: "
    )

    result = is_valid_password(password)

    display_validation_result(
        "Password",
        result
    )


# ============================================================
# Validate Username
# ============================================================

def validate_username_interactively():

    print("\n=== Username Validation ===")

    username = input(
        "Enter username: "
    )

    result = is_valid_username(username)

    display_validation_result(
        "Username",
        result
    )


# ============================================================
# Validate Age
# ============================================================

def validate_age_interactively():

    print("\n=== Age Validation ===")

    while True:

        try:

            age = int(
                input("Enter age: ").strip()
            )

            break

        except ValueError:

            print(
                "Please enter a valid whole number."
            )


    result = is_valid_age(age)

    display_validation_result(
        "Age",
        result
    )


# ============================================================
# Validate Number Range
# ============================================================

def validate_number_range_interactively():

    print("\n=== Number Range Validation ===")


    while True:

        try:

            value = float(
                input("Enter value: ").strip()
            )

            minimum = float(
                input("Minimum allowed: ").strip()
            )

            maximum = float(
                input("Maximum allowed: ").strip()
            )


            if minimum > maximum:

                print(
                    "Minimum cannot be greater "
                    "than maximum."
                )

                continue


            break

        except ValueError:

            print(
                "Please enter valid numbers."
            )


    result = is_valid_number(
        value,
        minimum,
        maximum
    )


    display_validation_result(
        "Number",
        result
    )


# ============================================================
# Validate Choice
# ============================================================

def validate_choice_interactively():

    print("\n=== Choice Validation ===")


    valid_choices = [
        "yes",
        "no",
        "maybe"
    ]


    print(
        f"Valid choices: "
        f"{', '.join(valid_choices)}"
    )


    choice = input(
        "Enter choice: "
    ).strip().lower()


    result = is_valid_choice(
        choice,
        valid_choices
    )


    display_validation_result(
        "Choice",
        result
    )


# ============================================================
# Validate Date
# ============================================================

def validate_date_interactively():

    print("\n=== Date Validation ===")


    date_text = input(
        "Enter date (YYYY-MM-DD): "
    )


    result = is_valid_date(
        date_text
    )


    display_validation_result(
        "Date",
        result
    )


# ============================================================
# Complete User Data Validation
# ============================================================

def validate_complete_user():

    print("\n=== Complete User Validation ===")


    name = input(
        "Name: "
    ).strip()


    username = input(
        "Username: "
    ).strip()


    email = input(
        "Email: "
    ).strip()


    phone = input(
        "Phone: "
    ).strip()


    while True:

        try:

            age = int(
                input("Age: ").strip()
            )

            break

        except ValueError:

            print(
                "Please enter a valid age."
            )


    password = input(
        "Password: "
    )


    date = input(
        "Date (YYYY-MM-DD): "
    ).strip()


    results = validate_user_data(
        name,
        username,
        email,
        phone,
        age,
        password,
        date
    )


    print("\n=== Validation Results ===")


    for field, result in results.items():

        display_validation_result(
            field.title(),
            result
        )


    valid_fields = sum(
        1
        for result in results.values()
        if result
    )


    total_fields = len(results)


    print(
        f"\nValid fields: "
        f"{valid_fields}/{total_fields}"
    )


    if valid_fields == total_fields:

        print(
            "All user data is valid."
        )

    else:

        print(
            "Some user data needs correction."
        )


# ============================================================
# Main Menu
# ============================================================

while True:

    print("\n=== Menu ===")
    print("1. Validate email")
    print("2. Validate phone number")
    print("3. Validate password")
    print("4. Validate username")
    print("5. Validate age")
    print("6. Validate number range")
    print("7. Validate choice")
    print("8. Validate date")
    print("9. Validate name")
    print("10. Validate complete user data")
    print("11. Exit")


    choice = input(
        "Choose an option: "
    ).strip()


    if choice == "1":

        validate_email_interactively()


    elif choice == "2":

        validate_phone_interactively()


    elif choice == "3":

        validate_password_interactively()


    elif choice == "4":

        validate_username_interactively()


    elif choice == "5":

        validate_age_interactively()


    elif choice == "6":

        validate_number_range_interactively()


    elif choice == "7":

        validate_choice_interactively()


    elif choice == "8":

        validate_date_interactively()


    elif choice == "9":

        print("\n=== Name Validation ===")


        name = input(
            "Enter name: "
        )


        result = is_valid_name(name)


        display_validation_result(
            "Name",
            result
        )


    elif choice == "10":

        validate_complete_user()


    elif choice == "11":

        print("\nGoodbye!")
        break


    else:

        print(
            "Invalid option. "
            "Please choose between 1 and 11."
        )