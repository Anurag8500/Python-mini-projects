# Bank Account Simulator

A command-line Python application that simulates basic banking operations such as deposits, withdrawals, balance checking, transaction history, and account summaries.

The project focuses on managing changing application state, validating user input, handling exceptions, and maintaining a record of financial transactions.

## Features

* Create a simulated bank account
* Enter account holder and account number
* Set an opening balance
* Check current balance
* Deposit money
* Withdraw money
* Prevent negative deposits and withdrawals
* Prevent withdrawals exceeding the available balance
* Record transaction history
* Display balance after each transaction
* Display account summary
* Handle invalid numeric input
* Interactive command-line menu

## Concepts Practiced

* Variables and data types
* Strings and string methods
* `.strip()`
* `.title()`
* `.upper()`
* Lists
* Dictionaries
* Nested data structures
* List of dictionaries
* `while True`
* `for` loops
* `if / elif / else`
* `break`
* `continue`
* `try` / `except`
* `ValueError`
* Dictionary access and updates
* `append()`
* `enumerate()`
* `len()`
* Arithmetic operations
* Boolean conditions
* Input validation
* State management
* Transaction tracking
* F-strings
* Number formatting with `:.2f`

## Data Structure

The current account state is stored in a dictionary:

```python id="2r9w3b"
account = {
    "holder": "Anurag",
    "account_number": "AC1001",
    "balance": 6000.0
}
```

Transactions are stored as a list of dictionaries:

```python id="i5k7bh"
transactions = [
    {
        "type": "Deposit",
        "amount": 1500.0,
        "balance_after": 6500.0
    },
    {
        "type": "Withdrawal",
        "amount": 500.0,
        "balance_after": 6000.0
    }
]
```

This separates the **current account state** from the **history of state changes**.

## How It Works

```text
Account setup
     ↓
Initialize account state
     ↓
Display menu
     ↓
Choose operation
     ↓
Validate input
     ↓
Update account state
     ↓
Record transaction
     ↓
Display result
     ↓
Return to menu
     ↓
Exit when requested
```

## Example

```text id="3b5mdq"
=== Bank Account Simulator ===

Account holder name: Anurag
Account number: ac1001
Opening balance: ₹5000

=== Menu ===
1. Check balance
2. Deposit money
3. Withdraw money
4. View transaction history
5. Account summary
6. Exit

Choose an option: 2

Amount to deposit: ₹1500
Deposit successful.
New balance: ₹6500.00

Choose an option: 3

Amount to withdraw: ₹500
Withdrawal successful.
New balance: ₹6000.00

Choose an option: 4

=== Transaction History ===
1. Deposit - ₹1500.00 | Balance: ₹6500.00
2. Withdrawal - ₹500.00 | Balance: ₹6000.00

Choose an option: 5

=== Account Summary ===
Account holder: Anurag
Account number: AC1001
Current balance: ₹6000.00
Total transactions: 2
```

## What I Learned

* How to represent the current state of an application using a dictionary
* How to store a sequence of related records using a list of dictionaries
* How to update dictionary values as the program runs
* How to maintain transaction history separately from current state
* How `try` / `except` can prevent invalid input from crashing a program
* How `ValueError` can occur during numeric conversion
* How `while True` can be used for an interactive application menu
* How `break` and `continue` control program flow
* How to enforce business rules such as preventing overdrafts
* How to validate user input before modifying application state
* How to use `enumerate()` for numbered transaction history

## Business Rules

The simulator currently enforces these rules:

* Opening balance cannot be negative
* Deposit amount must be greater than zero
* Withdrawal amount must be greater than zero
* Withdrawal cannot exceed the current balance
* Invalid numeric input is handled without terminating the application

## Possible Improvements

* Add transaction dates and timestamps
* Calculate total deposited amount
* Calculate total withdrawn amount
* Generate a mini bank statement
* Add transaction IDs
* Add multiple bank accounts
* Support account-to-account transfers
* Add transaction search and filtering
* Save account data to a file
* Load existing account data
* Refactor operations into reusable functions
* Rebuild using object-oriented programming
* Add automated tests
* Persist data using a database

## Project Structure

```text id="cn5whs"
05-bank-account-simulator/
│
├── main.py
└── README.md
```

## Status

**Completed — Phase 01: Python Core**

Project 05 of the Python Mini Projects curriculum.
