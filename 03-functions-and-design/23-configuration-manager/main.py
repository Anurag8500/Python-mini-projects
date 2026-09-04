import json
from pathlib import Path


print("=== Configuration Manager ===")


# ============================================================
# Configuration
# ============================================================

CONFIG_FILE = Path("config.json")

default_config = {
    "app": {
        "name": "Python Toolkit",
        "debug": False
    },
    "user": {
        "username": "anurag",
        "theme": "dark"
    },
    "display": {
        "page_size": 20,
        "show_timestamps": True
    }
}


# ============================================================
# Configuration Functions
# ============================================================

def load_config():
    """Load configuration from JSON or use defaults."""

    if not CONFIG_FILE.exists():
        return default_config.copy()

    try:
        with CONFIG_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Could not load config. Using defaults.")
        return default_config.copy()


def save_config():
    """Save current configuration to JSON."""

    try:
        with CONFIG_FILE.open("w", encoding="utf-8") as file:
            json.dump(
                config,
                file,
                indent=4
            )

        print("Configuration saved.")

    except OSError as error:
        print(f"Could not save configuration: {error}")


def get_setting(path):
    """Get a nested setting using dot notation."""

    keys = path.split(".")
    current = config

    for key in keys:

        if key not in current:
            return None

        current = current[key]

    return current


def set_setting(path, value):
    """Set a nested setting using dot notation."""

    keys = path.split(".")
    current = config


    for key in keys[:-1]:

        if key not in current:
            return False

        if not isinstance(current[key], dict):
            return False

        current = current[key]


    final_key = keys[-1]

    if final_key not in current:
        return False

    current[final_key] = value

    return True


def convert_value(value):
    """Convert text input into a basic Python value."""

    value = value.strip()


    if value.lower() == "true":
        return True

    if value.lower() == "false":
        return False


    try:
        return int(value)

    except ValueError:
        return value


def validate_config():
    """Check a few required configuration values."""

    errors = []


    if not isinstance(
        get_setting("app.name"),
        str
    ):
        errors.append("app.name must be text.")


    if not isinstance(
        get_setting("app.debug"),
        bool
    ):
        errors.append("app.debug must be True or False.")


    page_size = get_setting(
        "display.page_size"
    )


    if not isinstance(page_size, int) or page_size <= 0:
        errors.append(
            "display.page_size must be greater than 0."
        )


    theme = get_setting("user.theme")


    if theme not in ["dark", "light"]:
        errors.append(
            "user.theme must be dark or light."
        )


    return errors


def display_config():
    """Display the complete configuration."""

    print("\n=== Configuration ===")

    print(
        json.dumps(
            config,
            indent=4
        )
    )


# ============================================================
# Load Configuration
# ============================================================

config = load_config()


# ============================================================
# Main Menu
# ============================================================

while True:

    print("\n=== Menu ===")
    print("1. View configuration")
    print("2. Get setting")
    print("3. Set setting")
    print("4. Reset configuration")
    print("5. Search setting")
    print("6. Validate configuration")
    print("7. Save configuration")
    print("8. Exit")


    choice = input(
        "Choose an option: "
    ).strip()


    # ========================================================
    # VIEW CONFIGURATION
    # ========================================================

    if choice == "1":

        display_config()


    # ========================================================
    # GET SETTING
    # ========================================================

    elif choice == "2":

        path = input(
            "Setting path (example: user.theme): "
        ).strip()


        value = get_setting(path)


        if value is None:
            print("Setting not found.")

        else:
            print(
                f"{path} = {value}"
            )


    # ========================================================
    # SET SETTING
    # ========================================================

    elif choice == "3":

        path = input(
            "Setting path: "
        ).strip()


        new_value = input(
            "New value: "
        )


        value = convert_value(
            new_value
        )


        if set_setting(path, value):

            print("Setting updated.")

        else:

            print(
                "Setting not found or path is invalid."
            )


    # ========================================================
    # RESET CONFIGURATION
    # ========================================================

    elif choice == "4":

        config = json.loads(
            json.dumps(default_config)
        )

        print(
            "Configuration reset to defaults."
        )


    # ========================================================
    # SEARCH SETTING
    # ========================================================

    elif choice == "5":

        search_term = input(
            "Search setting name: "
        ).strip().lower()


        if not search_term:

            print("Search term cannot be empty.")
            continue


        def search_recursive(data, prefix=""):
            results = []

            for key, value in data.items():

                path = (
                    f"{prefix}.{key}"
                    if prefix
                    else key
                )


                if search_term in key.lower():

                    results.append(
                        (path, value)
                    )


                if isinstance(value, dict):

                    results.extend(
                        search_recursive(
                            value,
                            path
                        )
                    )

            return results


        results = search_recursive(config)


        if not results:

            print("No matching settings found.")

        else:

            print("\n=== Search Results ===")

            for path, value in results:

                print(
                    f"{path} = {value}"
                )


    # ========================================================
    # VALIDATE CONFIGURATION
    # ========================================================

    elif choice == "6":

        errors = validate_config()


        if not errors:

            print(
                "Configuration is valid."
            )

        else:

            print(
                "\nConfiguration errors:"
            )

            for error in errors:

                print(
                    f"- {error}"
                )


    # ========================================================
    # SAVE CONFIGURATION
    # ========================================================

    elif choice == "7":

        save_config()


    # ========================================================
    # EXIT
    # ========================================================

    elif choice == "8":

        print("\nGoodbye!")
        break


    else:

        print(
            "Invalid option. "
            "Please choose between 1 and 8."
        )