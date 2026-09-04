# Project #21: File Utility Toolkit

A Python-based terminal toolkit for interacting with files and directories through reusable functions.

This project introduces practical filesystem programming using Python's standard library, with a particular focus on `pathlib`, file I/O, directory traversal, file metadata, searching, and filesystem operations.

It continues the function-oriented design introduced in Phase 03 while preparing for the dedicated **Files & Data Processing** phase later in the roadmap.

## Features

* Show the current working directory
* List files in a directory
* List directories
* Create directories
* Create files
* Read text files
* Write content to files
* Append content to files
* Copy files
* Rename files and directories
* Delete files
* Inspect file and directory information
* Search files recursively
* Calculate directory statistics
* Count files by extension
* Identify the largest file
* Calculate total file size
* Handle common filesystem errors

## Concepts Practiced

### Functions

* Function definitions
* Function calls
* Parameters
* Return values
* Helper functions
* Function composition
* Single-responsibility functions

### Filesystem

* `pathlib.Path`
* File paths
* Relative paths
* Absolute paths
* Current working directory
* Files
* Directories
* Directory traversal
* Recursive traversal
* File metadata

### File I/O

* Reading files
* Writing files
* Appending files
* `Path.read_text()`
* `Path.write_text()`
* `Path.open()`
* `with` statements

### Filesystem Operations

* `Path.mkdir()`
* `Path.touch()`
* `Path.rename()`
* `Path.unlink()`
* `shutil.copy2()`

### Data Processing

* Lists
* Dictionaries
* List comprehensions
* Generator expressions
* `len()`
* `sum()`
* `max()`
* `sorted()`
* Dictionary `.get()`
* Dictionary `.items()`

### Error Handling

* `try / except`
* `OSError`
* Path existence checks
* File/directory type checks

## Why This Project Exists

Previous projects primarily worked with data stored in memory:

```text
Lists
Dictionaries
Sets
Nested records
```

Project #21 introduces data that exists outside the running Python program:

```text id="3vhg3f"
Python Program
      ↓
Filesystem
      ↓
Files + Directories
```

This is an important transition because real applications frequently need to read, create, modify, search, and organize files.

## Why `pathlib`?

The project uses:

```python id="k9u8r5"
from pathlib import Path
```

`Path` provides an object-oriented way to work with filesystem paths.

For example:

```python id="c1x9p4"
path = Path("data/report.txt")
```

The program can then inspect the path:

```python id="2v4m1p"
path.exists()
path.is_file()
path.is_dir()
```

and perform operations such as:

```python id="4kg73v"
path.read_text()
path.write_text(...)
path.rename(...)
path.unlink()
```

This makes filesystem code clearer than manually manipulating path strings.

## Main Menu

```text id="wpl3s7"
=== Menu ===
1. Show current directory
2. List files
3. List directories
4. Create directory
5. Create file
6. Read file
7. Write to file
8. Append to file
9. Copy file
10. Rename file/directory
11. Delete file
12. File/path information
13. Search files
14. Directory statistics
15. Exit
```

## Current Working Directory

The program can display the directory from which it is currently running.

It uses:

```python id="r7gnx4"
Path.cwd()
```

Example:

```text id="syq2tz"
=== Current Directory ===

C:\Users\Anurag\python-mini-projects\21-file-utility-toolkit
```

This provides a reference point when working with relative paths.

## Listing Files

The toolkit can list files contained directly inside a directory.

The project uses:

```python id="9g4kqq"
directory.iterdir()
```

and filters the results:

```python id="t8m5vc"
if item.is_file()
```

The resulting files are sorted alphabetically before being displayed.

## Listing Directories

Directories can be identified similarly:

```python id="5g9x5b"
if item.is_dir()
```

This allows the user to inspect the immediate directory structure.

## Creating Directories

The toolkit can create a new directory.

For example:

```text id="k0f6eg"
data/reports/2026
```

The program uses:

```python id="tnt2a0"
directory.mkdir(
    parents=True
)
```

`parents=True` allows the required parent directories to be created when they do not already exist.

## Creating Files

The program can create an empty file using:

```python id="kfq3ak"
file_path.touch()
```

Parent directories are created when necessary.

For example:

```text id="91p4s2"
data/reports/report.txt
```

can be created even when the `reports` directory does not yet exist.

## Reading Files

The toolkit reads text files using:

```python id="3o7d5e"
file_path.read_text(
    encoding="utf-8"
)
```

The contents are then displayed in the terminal.

The program checks beforehand that:

* The path exists
* The path is a file

## Writing to Files

The write operation replaces the existing file contents.

The application allows multi-line input and combines the lines into one string:

```python id="fck5ef"
content = "\n".join(lines)
```

The content is then written using:

```python id="q8klf1"
file_path.write_text(
    content,
    encoding="utf-8"
)
```

## Appending to Files

Appending differs from writing because it preserves existing content.

The program opens the file in append mode:

```python id="re0nq7"
with file_path.open(
    "a",
    encoding="utf-8"
) as file:
```

and adds the new content at the end.

The `with` statement ensures that the file is properly closed after the operation.

## Copying Files

The project uses:

```python id="n0vq73"
shutil.copy2(
    source,
    destination
)
```

to copy files.

`copy2()` also attempts to preserve file metadata such as modification times.

The source is validated before copying.

## Renaming

The toolkit can rename either a file or directory using:

```python id="97w8xj"
source.rename(destination)
```

The new path is constructed using the original parent directory and the new name.

This prevents the operation from accidentally moving the item to a different directory.

## Deleting Files

Files can be deleted using:

```python id="m5w8wq"
file_path.unlink()
```

The program asks for explicit confirmation before deletion:

```text id="o8q6p6"
Delete 'report.txt'? (yes/no):
```

Only files are deleted through this menu option; directories are intentionally protected from deletion by the toolkit.

## File and Path Information

The information tool displays properties such as:

* Path
* Absolute path
* Path type
* Name
* Parent directory
* File size

Example:

```text id="9p5dso"
=== Path Information ===

Path: data/report.txt
Absolute path: C:\...\data\report.txt
Type: File
Name: report.txt
Parent: data
Size: 1248 bytes
```

File size is obtained from:

```python id="7d6ir7"
path.stat().st_size
```

## Recursive File Search

The search feature uses:

```python id="kmne9c"
directory.rglob("*")
```

to search through the directory and all nested subdirectories.

The user enters a keyword, and files whose names contain that keyword are returned.

For example:

```text id="0i8cqo"
Search keyword: report
```

might return:

```text
data/report.txt
data/reports/monthly_report.txt
backup/report_old.txt
```

The search is case-insensitive.

## Directory Statistics

The toolkit can analyze an entire directory tree.

It calculates:

* Total files
* Total directories
* Total file size
* Largest file
* File count by extension

Example:

```text id="wpk8v8"
=== Directory Statistics ===

Total files: 24
Total directories: 7
Total file size: 1,452,832 bytes
Largest file: data/dataset.csv (845632 bytes)

Files by extension:
- .csv: 4
- .json: 3
- .md: 5
- .py: 8
- .txt: 4
```

## File Extension Counting

The program builds a dictionary containing the number of files for each extension.

For example:

```python id="bvq9go"
{
    ".py": 8,
    ".txt": 4,
    ".json": 3,
    ".csv": 4
}
```

The dictionary counting pattern is:

```python id="4d4xah"
file_extensions[extension] = (
    file_extensions.get(extension, 0) + 1
)
```

Files without extensions are grouped under:

```text id="ef7ydr"
[no extension]
```

## Recursive Traversal

A key difference between:

```python id="2yx8x3"
directory.iterdir()
```

and:

```python id="5s4w1d"
directory.rglob("*")
```

is the depth of traversal.

`iterdir()` examines direct children:

```text
directory/
├── file.txt
├── report.txt
└── data/
```

while `rglob("*")` also explores:

```text
directory/
└── data/
    ├── users.json
    └── reports/
        └── monthly.txt
```

This distinction becomes important in larger data-processing applications.

## Error Handling

Filesystem operations can fail for many reasons, such as:

* A path does not exist
* The path points to the wrong type
* Permission problems
* Invalid filesystem operations
* Operating-system errors

The project handles many filesystem operations with:

```python id="vpc4oy"
try:
    ...
except OSError as error:
    ...
```

This allows the program to report the problem instead of terminating unexpectedly.

## Helper Functions

The project includes helper functions such as:

```python id="2k0hql"
get_path()
show_path_type()
```

This reduces repeated input and path-checking logic.

For example:

```python id="h1e0ry"
directory = get_path()
```

is reused by several directory-related operations.

This reinforces the function-design principles introduced in Projects #18–#20.

## Separation of Responsibilities

The project follows a simple structure:

```text id="47c80d"
Input
  ↓
Filesystem function
  ↓
Validation / operation
  ↓
Result
  ↓
Display
```

For example:

```text id="t5rsd7"
read_file()
    ↓
validate path
    ↓
read contents
    ↓
return / display result
```

This is an early example of designing utilities around clear responsibilities.

## Project Structure

```text id="rzfvq4"
21-file-utility-toolkit/
│
├── main.py
└── README.md
```

The project remains in a single file intentionally.

Later projects will begin separating reusable functionality into modules and eventually packages.

## How to Run

From the project directory:

```bash id="ys5w9p"
python main.py
```

Make sure your Python virtual environment is activated before running the project.

## Example Workflow

```text id="6xm9h8"
Check current directory
        ↓
Create a workspace directory
        ↓
Create / write a text file
        ↓
Read the file
        ↓
Append more content
        ↓
Copy or rename the file
        ↓
Search the directory
        ↓
Inspect file information
        ↓
Generate directory statistics
```

## Learning Progression

Project #21 builds directly on the function-oriented design introduced in Phase 03:

```text id="vby9em"
Project #18
Functions + modular expense workflows
        ↓
Project #19
Reusable validation functions
        ↓
Project #20
Reusable text-processing functions
        ↓
Project #21
Reusable filesystem utilities
```

The project also prepares the foundation for later file-processing work:

```text id="j3d4k4"
File / Directory APIs
        ↓
Text files
        ↓
Directory traversal
        ↓
File searching
        ↓
Metadata analysis
        ↓
Future data-processing pipelines
```

## Why This Project Matters

Almost every practical Python application eventually interacts with the filesystem.

Common examples include:

```text id="8qco8n"
Configuration files
Logs
Datasets
Reports
Backups
Uploaded files
Cached data
Documents
```

Project #21 provides a foundation for interacting with these resources safely and programmatically.

The larger lesson is learning how to combine:

```text id="vct62f"
Functions
+
Standard library
+
Error handling
+
Filesystem APIs
+
Data processing
```

into reusable utilities.

## Future Improvements

Possible extensions include:

* Move utilities into separate modules
* Add recursive directory creation helpers
* Support directory deletion with safeguards
* Detect duplicate files
* Calculate file hashes
* Compare files
* Search file contents
* Filter files by extension
* Filter files by size
* Sort files by modification time
* Create automated backup utilities
* Add CSV and JSON processing
* Add unit tests
* Package the toolkit for reuse

These improvements will be introduced progressively throughout the later file-processing and tooling stages.

## Development Philosophy

This repository follows:

```text id="h5f5ok"
Learn
  ↓
Build
  ↓
Break
  ↓
Debug
  ↓
Improve
  ↓
Understand
  ↓
Repeat
```

The objective is not simply to make filesystem operations work, but to understand how Python represents paths, interacts with files, handles errors, and packages repeated operations into reusable functions.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.
