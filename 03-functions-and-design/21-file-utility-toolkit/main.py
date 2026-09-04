from pathlib import Path
import shutil


print("=== File Utility Toolkit ===")


# ============================================================
# Helper Functions
# ============================================================

def get_path():
    """
    Ask the user for a path and return it as a Path object.
    """

    path_text = input("Enter path: ").strip()

    if not path_text:
        print("Path cannot be empty.")
        return None

    return Path(path_text)


def show_path_type(path):
    """
    Display whether a path is a file or directory.
    """

    if path.is_file():
        print("Type: File")

    elif path.is_dir():
        print("Type: Directory")

    else:
        print("Type: Path does not exist")


# ============================================================
# Directory Functions
# ============================================================

def show_current_directory():
    """
    Display the current working directory.
    """

    current_directory = Path.cwd()

    print("\n=== Current Directory ===")
    print(current_directory)


def list_files():
    """
    Display files in a directory.
    """

    directory = get_path()

    if directory is None:
        return

    if not directory.exists():
        print("Directory does not exist.")
        return

    if not directory.is_dir():
        print("The provided path is not a directory.")
        return


    files = [
        item
        for item in directory.iterdir()
        if item.is_file()
    ]


    if not files:
        print("No files found.")
        return


    print("\n=== Files ===")


    for number, file in enumerate(
        sorted(files, key=lambda item: item.name.lower()),
        start=1
    ):

        print(
            f"{number}. "
            f"{file.name}"
        )


def list_directories():
    """
    Display directories inside a directory.
    """

    directory = get_path()

    if directory is None:
        return

    if not directory.exists():
        print("Directory does not exist.")
        return

    if not directory.is_dir():
        print("The provided path is not a directory.")
        return


    directories = [
        item
        for item in directory.iterdir()
        if item.is_dir()
    ]


    if not directories:
        print("No directories found.")
        return


    print("\n=== Directories ===")


    for number, directory_item in enumerate(
        sorted(
            directories,
            key=lambda item: item.name.lower()
        ),
        start=1
    ):

        print(
            f"{number}. "
            f"{directory_item.name}"
        )


def create_directory():
    """
    Create a directory.
    """

    directory = get_path()

    if directory is None:
        return


    if directory.exists():

        print(
            "A file or directory already exists "
            "at this path."
        )

        return


    try:

        directory.mkdir(
            parents=True
        )

        print(
            f"Directory created successfully: "
            f"{directory}"
        )

    except OSError as error:

        print(
            f"Could not create directory: "
            f"{error}"
        )


# ============================================================
# File Creation and I/O
# ============================================================

def create_file():
    """
    Create an empty file.
    """

    file_path = get_path()

    if file_path is None:
        return


    if file_path.exists():

        print(
            "A file or directory already exists "
            "at this path."
        )

        return


    parent_directory = file_path.parent


    try:

        if (
            parent_directory != Path(".")
            and not parent_directory.exists()
        ):

            parent_directory.mkdir(
                parents=True
            )


        file_path.touch()


        print(
            f"File created successfully: "
            f"{file_path}"
        )

    except OSError as error:

        print(
            f"Could not create file: "
            f"{error}"
        )


def read_file():
    """
    Read and display the contents of a text file.
    """

    file_path = get_path()

    if file_path is None:
        return


    if not file_path.exists():

        print("File does not exist.")
        return


    if not file_path.is_file():

        print("The provided path is not a file.")
        return


    try:

        content = file_path.read_text(
            encoding="utf-8"
        )


        print("\n=== File Contents ===")

        if content:

            print(content)

        else:

            print("The file is empty.")


    except OSError as error:

        print(
            f"Could not read file: "
            f"{error}"
        )


def write_file():
    """
    Overwrite a text file with new content.
    """

    file_path = get_path()

    if file_path is None:
        return


    print(
        "\nEnter content."
    )

    print(
        "Press Enter on an empty line "
        "when finished."
    )


    lines = []


    while True:

        line = input()

        if line == "":
            break

        lines.append(line)


    content = "\n".join(lines)


    try:

        file_path.write_text(
            content,
            encoding="utf-8"
        )


        print(
            f"File written successfully: "
            f"{file_path}"
        )

    except OSError as error:

        print(
            f"Could not write file: "
            f"{error}"
        )


def append_to_file():
    """
    Append text to an existing text file.
    """

    file_path = get_path()

    if file_path is None:
        return


    if not file_path.exists():

        print("File does not exist.")
        return


    if not file_path.is_file():

        print("The provided path is not a file.")
        return


    print(
        "\nEnter content to append."
    )

    print(
        "Press Enter on an empty line "
        "when finished."
    )


    lines = []


    while True:

        line = input()

        if line == "":
            break

        lines.append(line)


    content = "\n".join(lines)


    try:

        with file_path.open(
            "a",
            encoding="utf-8"
        ) as file:

            if file_path.stat().st_size > 0:

                file.write("\n")

            file.write(content)


        print(
            f"Content appended successfully "
            f"to {file_path}"
        )

    except OSError as error:

        print(
            f"Could not append to file: "
            f"{error}"
        )


# ============================================================
# File Operations
# ============================================================

def copy_file():
    """
    Copy a file to another location.
    """

    source = get_path()

    if source is None:
        return


    if not source.exists():

        print("Source file does not exist.")
        return


    if not source.is_file():

        print("Source path is not a file.")
        return


    destination = input(
        "Destination path: "
    ).strip()


    if not destination:

        print("Destination cannot be empty.")
        return


    destination = Path(destination)


    try:

        shutil.copy2(
            source,
            destination
        )


        print(
            f"File copied successfully:\n"
            f"From: {source}\n"
            f"To: {destination}"
        )

    except OSError as error:

        print(
            f"Could not copy file: "
            f"{error}"
        )


def rename_path():
    """
    Rename a file or directory.
    """

    source = get_path()

    if source is None:
        return


    if not source.exists():

        print("Path does not exist.")
        return


    new_name = input(
        "Enter new name: "
    ).strip()


    if not new_name:

        print("New name cannot be empty.")
        return


    destination = source.parent / new_name


    if destination.exists():

        print(
            "A file or directory with that name "
            "already exists."
        )

        return


    try:

        source.rename(destination)


        print(
            f"Renamed successfully:\n"
            f"From: {source.name}\n"
            f"To: {destination.name}"
        )

    except OSError as error:

        print(
            f"Could not rename path: "
            f"{error}"
        )


def delete_path():
    """
    Delete a file.
    """

    file_path = get_path()

    if file_path is None:
        return


    if not file_path.exists():

        print("Path does not exist.")
        return


    if not file_path.is_file():

        print(
            "This option only deletes files."
        )

        return


    confirmation = input(
        f"Delete '{file_path.name}'? "
        f"(yes/no): "
    ).strip().lower()


    if confirmation != "yes":

        print("Deletion cancelled.")
        return


    try:

        file_path.unlink()


        print(
            f"File deleted successfully: "
            f"{file_path}"
        )

    except OSError as error:

        print(
            f"Could not delete file: "
            f"{error}"
        )


# ============================================================
# File Information
# ============================================================

def show_file_information():
    """
    Display metadata for a file or directory.
    """

    path = get_path()

    if path is None:
        return


    if not path.exists():

        print("Path does not exist.")
        return


    print("\n=== Path Information ===")


    print(
        f"Path: "
        f"{path}"
    )


    print(
        f"Absolute path: "
        f"{path.resolve()}"
    )


    show_path_type(path)


    print(
        f"Name: "
        f"{path.name}"
    )


    print(
        f"Parent: "
        f"{path.parent}"
    )


    if path.is_file():

        try:

            file_size = path.stat().st_size


            print(
                f"Size: "
                f"{file_size} bytes"
            )

        except OSError as error:

            print(
                f"Could not read file metadata: "
                f"{error}"
            )


# ============================================================
# Search Functions
# ============================================================

def search_files():
    """
    Search for files whose names contain a keyword.
    """

    directory = get_path()

    if directory is None:
        return


    if not directory.exists():

        print("Directory does not exist.")
        return


    if not directory.is_dir():

        print("The provided path is not a directory.")
        return


    keyword = input(
        "Search keyword: "
    ).strip().lower()


    if not keyword:

        print("Keyword cannot be empty.")
        return


    matching_files = [

        file

        for file in directory.rglob("*")

        if (
            file.is_file()
            and keyword in file.name.lower()
        )
    ]


    print("\n=== Search Results ===")


    if not matching_files:

        print("No matching files found.")
        return


    for number, file in enumerate(
        sorted(
            matching_files,
            key=lambda item: str(item).lower()
        ),
        start=1
    ):

        print(
            f"{number}. "
            f"{file}"
        )


# ============================================================
# Directory Statistics
# ============================================================

def show_directory_statistics():
    """
    Calculate basic statistics for a directory.
    """

    directory = get_path()

    if directory is None:
        return


    if not directory.exists():

        print("Directory does not exist.")
        return


    if not directory.is_dir():

        print("The provided path is not a directory.")
        return


    all_items = list(
        directory.rglob("*")
    )


    files = [
        item
        for item in all_items
        if item.is_file()
    ]


    directories = [
        item
        for item in all_items
        if item.is_dir()
    ]


    total_file_size = sum(
        file.stat().st_size
        for file in files
    )


    file_extensions = {}


    for file in files:

        extension = (
            file.suffix.lower()
            if file.suffix
            else "[no extension]"
        )


        file_extensions[extension] = (
            file_extensions.get(extension, 0) + 1
        )


    largest_file = None


    if files:

        largest_file = max(
            files,
            key=lambda file: file.stat().st_size
        )


    print("\n=== Directory Statistics ===")


    print(
        f"Total files: "
        f"{len(files)}"
    )


    print(
        f"Total directories: "
        f"{len(directories)}"
    )


    print(
        f"Total file size: "
        f"{total_file_size} bytes"
    )


    if largest_file:

        print(
            f"Largest file: "
            f"{largest_file} "
            f"({largest_file.stat().st_size} bytes)"
        )


    print("\nFiles by extension:")


    if file_extensions:

        for extension, count in sorted(
            file_extensions.items(),
            key=lambda item: item[0]
        ):

            print(
                f"- {extension}: "
                f"{count}"
            )

    else:

        print("- No files found")


# ============================================================
# Main Menu
# ============================================================

while True:

    print("\n=== Menu ===")
    print("1. Show current directory")
    print("2. List files")
    print("3. List directories")
    print("4. Create directory")
    print("5. Create file")
    print("6. Read file")
    print("7. Write to file")
    print("8. Append to file")
    print("9. Copy file")
    print("10. Rename file/directory")
    print("11. Delete file")
    print("12. File/path information")
    print("13. Search files")
    print("14. Directory statistics")
    print("15. Exit")


    choice = input(
        "Choose an option: "
    ).strip()


    if choice == "1":

        show_current_directory()


    elif choice == "2":

        list_files()


    elif choice == "3":

        list_directories()


    elif choice == "4":

        create_directory()


    elif choice == "5":

        create_file()


    elif choice == "6":

        read_file()


    elif choice == "7":

        write_file()


    elif choice == "8":

        append_to_file()


    elif choice == "9":

        copy_file()


    elif choice == "10":

        rename_path()


    elif choice == "11":

        delete_path()


    elif choice == "12":

        show_file_information()


    elif choice == "13":

        search_files()


    elif choice == "14":

        show_directory_statistics()


    elif choice == "15":

        print("\nGoodbye!")
        break


    else:

        print(
            "Invalid option. "
            "Please choose between 1 and 15."
        )