print("=== Mini Library Management System ===")


# ============================================================
# Library Data
# ============================================================

books = [
    {
        "id": "B001",
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "category": "programming",
        "year": 2019,
        "status": "available",
        "borrower": None
    },
    {
        "id": "B002",
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "category": "programming",
        "year": 2008,
        "status": "borrowed",
        "borrower": "Anurag Bardhan"
    },
    {
        "id": "B003",
        "title": "The Pragmatic Programmer",
        "author": "David Thomas",
        "category": "programming",
        "year": 2019,
        "status": "available",
        "borrower": None
    },
    {
        "id": "B004",
        "title": "Atomic Habits",
        "author": "James Clear",
        "category": "self-help",
        "year": 2018,
        "status": "available",
        "borrower": None
    },
    {
        "id": "B005",
        "title": "Deep Work",
        "author": "Cal Newport",
        "category": "productivity",
        "year": 2016,
        "status": "borrowed",
        "borrower": "Priya Singh"
    },
    {
        "id": "B006",
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "category": "fiction",
        "year": 1988,
        "status": "available",
        "borrower": None
    },
    {
        "id": "B007",
        "title": "Sapiens",
        "author": "Yuval Noah Harari",
        "category": "history",
        "year": 2011,
        "status": "available",
        "borrower": None
    },
    {
        "id": "B008",
        "title": "Atomic Habits Workbook",
        "author": "James Clear",
        "category": "self-help",
        "year": 2020,
        "status": "available",
        "borrower": None
    }
]


valid_categories = [
    "programming",
    "fiction",
    "history",
    "self-help",
    "productivity",
    "science",
    "education",
    "other"
]


next_book_number = 9


# ============================================================
# Main Menu
# ============================================================

while True:

    print("\n=== Menu ===")
    print("1. View all books")
    print("2. Add book")
    print("3. Search books")
    print("4. Filter books")
    print("5. Sort books")
    print("6. Borrow book")
    print("7. Return book")
    print("8. View borrowed books")
    print("9. Library statistics")
    print("10. Detailed report")
    print("11. Exit")

    choice = input("Choose an option: ").strip()


    # ========================================================
    # VIEW ALL BOOKS
    # ========================================================

    if choice == "1":

        print("\n=== All Books ===")

        if not books:
            print("No books available.")
            continue


        for book in books:

            print(
                f"\n[{book['id']}] "
                f"{book['title']}"
            )

            print(
                f"  Author: "
                f"{book['author']}"
            )

            print(
                f"  Category: "
                f"{book['category'].title()}"
            )

            print(
                f"  Year: "
                f"{book['year']}"
            )

            print(
                f"  Status: "
                f"{book['status'].title()}"
            )

            if book["borrower"] is not None:

                print(
                    f"  Borrower: "
                    f"{book['borrower']}"
                )


    # ========================================================
    # ADD BOOK
    # ========================================================

    elif choice == "2":

        print("\n=== Add Book ===")


        title = input(
            "Book title: "
        ).strip()


        if not title:

            print("Title cannot be empty.")
            continue


        author = input(
            "Author: "
        ).strip()


        if not author:

            print("Author cannot be empty.")
            continue


        print("\nAvailable categories:")

        for category in valid_categories:
            print(f"- {category.title()}")


        while True:

            category = input(
                "Category: "
            ).strip().lower()


            if category in valid_categories:
                break


            print("Invalid category.")


        while True:

            try:

                year = int(
                    input("Publication year: ").strip()
                )


                if year <= 0:

                    print(
                        "Publication year must "
                        "be greater than 0."
                    )

                    continue


                break


            except ValueError:

                print(
                    "Please enter a valid year."
                )


        # Check duplicate title + author

        duplicate_book = False

        for book in books:

            if (
                book["title"].lower() == title.lower()
                and book["author"].lower() == author.lower()
            ):

                duplicate_book = True
                break


        if duplicate_book:

            print(
                "This book by this author "
                "already exists."
            )

            continue


        book_id = f"B{next_book_number:03d}"


        books.append(
            {
                "id": book_id,
                "title": title.title(),
                "author": author.title(),
                "category": category,
                "year": year,
                "status": "available",
                "borrower": None
            }
        )


        print(
            f"Book added successfully "
            f"with ID {book_id}."
        )


        next_book_number += 1


    # ========================================================
    # SEARCH BOOKS
    # ========================================================

    elif choice == "3":

        search_term = input(
            "Search by title, author, or category: "
        ).strip().lower()


        if not search_term:

            print("Search term cannot be empty.")
            continue


        matching_books = [

            book

            for book in books

            if (
                search_term in book["title"].lower()
                or search_term in book["author"].lower()
                or search_term in book["category"].lower()
            )
        ]


        if not matching_books:

            print("No matching books found.")
            continue


        print("\n=== Search Results ===")


        for book in matching_books:

            print(
                f"[{book['id']}] "
                f"{book['title']} | "
                f"{book['author']} | "
                f"{book['category'].title()} | "
                f"{book['status'].title()}"
            )


    # ========================================================
    # FILTER BOOKS
    # ========================================================

    elif choice == "4":

        print("\n=== Filter Books ===")
        print("1. By category")
        print("2. Available books")
        print("3. Borrowed books")
        print("4. Published after a year")


        filter_choice = input(
            "Choose filter: "
        ).strip()


        if filter_choice == "1":

            print("\nAvailable categories:")

            for category in valid_categories:
                print(f"- {category.title()}")


            category = input(
                "Enter category: "
            ).strip().lower()


            if category not in valid_categories:

                print("Invalid category.")
                continue


            matching_books = [

                book

                for book in books

                if book["category"] == category
            ]


        elif filter_choice == "2":

            matching_books = [

                book

                for book in books

                if book["status"] == "available"
            ]


        elif filter_choice == "3":

            matching_books = [

                book

                for book in books

                if book["status"] == "borrowed"
            ]


        elif filter_choice == "4":

            while True:

                try:

                    minimum_year = int(
                        input(
                            "Show books published after: "
                        ).strip()
                    )


                    if minimum_year <= 0:

                        print(
                            "Enter a valid year."
                        )

                        continue


                    break


                except ValueError:

                    print(
                        "Please enter a valid year."
                    )


            matching_books = [

                book

                for book in books

                if book["year"] > minimum_year
            ]


        else:

            print("Invalid filter option.")
            continue


        if not matching_books:

            print("No books matched the filter.")
            continue


        print("\n=== Filter Results ===")


        for book in matching_books:

            print(
                f"[{book['id']}] "
                f"{book['title']} | "
                f"{book['author']} | "
                f"{book['year']} | "
                f"{book['status'].title()}"
            )


    # ========================================================
    # SORT BOOKS
    # ========================================================

    elif choice == "5":

        print("\n=== Sort Books ===")
        print("1. Title")
        print("2. Author")
        print("3. Publication year")


        sort_choice = input(
            "Choose sorting field: "
        ).strip()


        print("\n1. Ascending")
        print("2. Descending")


        order_choice = input(
            "Choose order: "
        ).strip()


        if order_choice == "1":

            reverse = False

        elif order_choice == "2":

            reverse = True

        else:

            print("Invalid sorting order.")
            continue


        if sort_choice == "1":

            sorted_books = sorted(
                books,
                key=lambda book:
                    book["title"].lower(),
                reverse=reverse
            )

        elif sort_choice == "2":

            sorted_books = sorted(
                books,
                key=lambda book:
                    book["author"].lower(),
                reverse=reverse
            )

        elif sort_choice == "3":

            sorted_books = sorted(
                books,
                key=lambda book:
                    book["year"],
                reverse=reverse
            )

        else:

            print("Invalid sorting field.")
            continue


        print("\n=== Sorted Books ===")


        for book in sorted_books:

            print(
                f"[{book['id']}] "
                f"{book['title']} | "
                f"{book['author']} | "
                f"{book['year']}"
            )


    # ========================================================
    # BORROW BOOK
    # ========================================================

    elif choice == "6":

        print("\n=== Borrow Book ===")


        book_id = input(
            "Enter book ID: "
        ).strip().upper()


        selected_book = None


        for book in books:

            if book["id"] == book_id:

                selected_book = book
                break


        if selected_book is None:

            print("Book not found.")
            continue


        if selected_book["status"] == "borrowed":

            print(
                f"Book is already borrowed by "
                f"{selected_book['borrower']}."
            )

            continue


        borrower = input(
            "Borrower name: "
        ).strip()


        if not borrower:

            print("Borrower name cannot be empty.")
            continue


        selected_book["status"] = "borrowed"

        selected_book["borrower"] = (
            borrower.title()
        )


        print(
            f"'{selected_book['title']}' "
            f"borrowed successfully by "
            f"{selected_book['borrower']}."
        )


    # ========================================================
    # RETURN BOOK
    # ========================================================

    elif choice == "7":

        print("\n=== Return Book ===")


        book_id = input(
            "Enter book ID: "
        ).strip().upper()


        selected_book = None


        for book in books:

            if book["id"] == book_id:

                selected_book = book
                break


        if selected_book is None:

            print("Book not found.")
            continue


        if selected_book["status"] == "available":

            print(
                "This book is already available."
            )

            continue


        print(
            f"Borrowed by: "
            f"{selected_book['borrower']}"
        )


        selected_book["status"] = "available"

        selected_book["borrower"] = None


        print(
            f"'{selected_book['title']}' "
            f"returned successfully."
        )


    # ========================================================
    # VIEW BORROWED BOOKS
    # ========================================================

    elif choice == "8":

        borrowed_books = [

            book

            for book in books

            if book["status"] == "borrowed"
        ]


        print("\n=== Borrowed Books ===")


        if not borrowed_books:

            print("No books are currently borrowed.")
            continue


        for number, book in enumerate(
            borrowed_books,
            start=1
        ):

            print(
                f"{number}. "
                f"{book['title']} | "
                f"Borrower: "
                f"{book['borrower']}"
            )


        print(
            f"\nTotal borrowed books: "
            f"{len(borrowed_books)}"
        )


    # ========================================================
    # LIBRARY STATISTICS
    # ========================================================

    elif choice == "9":

        if not books:

            print("No books available.")
            continue


        total_books = len(books)


        available_books = sum(
            1
            for book in books
            if book["status"] == "available"
        )


        borrowed_books = sum(
            1
            for book in books
            if book["status"] == "borrowed"
        )


        oldest_book = min(
            books,
            key=lambda book: book["year"]
        )


        newest_book = max(
            books,
            key=lambda book: book["year"]
        )


        category_counts = {}


        for book in books:

            category = book["category"]

            category_counts[category] = (
                category_counts.get(category, 0) + 1
            )


        most_common_category = max(
            category_counts.items(),
            key=lambda item: item[1]
        )


        print("\n=== Library Statistics ===")


        print(
            f"Total books: "
            f"{total_books}"
        )


        print(
            f"Available books: "
            f"{available_books}"
        )


        print(
            f"Borrowed books: "
            f"{borrowed_books}"
        )


        print(
            f"Oldest book: "
            f"{oldest_book['title']} "
            f"({oldest_book['year']})"
        )


        print(
            f"Newest book: "
            f"{newest_book['title']} "
            f"({newest_book['year']})"
        )


        print(
            f"Most common category: "
            f"{most_common_category[0].title()} "
            f"({most_common_category[1]} books)"
        )


        print("\nBooks by category:")


        for category, count in sorted(
            category_counts.items()
        ):

            print(
                f"- {category.title()}: "
                f"{count}"
            )


    # ========================================================
    # DETAILED REPORT
    # ========================================================

    elif choice == "10":

        if not books:

            print("No books available.")
            continue


        total_books = len(books)


        available_books = sum(
            1
            for book in books
            if book["status"] == "available"
        )


        borrowed_books = sum(
            1
            for book in books
            if book["status"] == "borrowed"
        )


        borrowing_rate = (
            borrowed_books
            / total_books
            * 100
        )


        category_counts = {}


        for book in books:

            category = book["category"]

            category_counts[category] = (
                category_counts.get(category, 0) + 1
            )


        ranked_categories = sorted(
            category_counts.items(),
            key=lambda item: item[1],
            reverse=True
        )


        most_borrowed_books = sorted(
            [
                book
                for book in books
                if book["status"] == "borrowed"
            ],
            key=lambda book: book["title"].lower()
        )


        print("\n========================================")
        print("        DETAILED LIBRARY REPORT")
        print("========================================")


        print(
            f"\nTotal books     : "
            f"{total_books}"
        )


        print(
            f"Available books : "
            f"{available_books}"
        )


        print(
            f"Borrowed books  : "
            f"{borrowed_books}"
        )


        print(
            f"Borrowing rate  : "
            f"{borrowing_rate:.2f}%"
        )


        print("\nCategories:")


        for category, count in ranked_categories:

            print(
                f"- {category.title()}: "
                f"{count}"
            )


        print("\nCurrently borrowed:")


        if not most_borrowed_books:

            print("- None")

        else:

            for book in most_borrowed_books:

                print(
                    f"- {book['title']} "
                    f"→ {book['borrower']}"
                )


        print("\nRecently published books:")


        recent_books = sorted(
            books,
            key=lambda book: book["year"],
            reverse=True
        )[:5]


        for rank, book in enumerate(
            recent_books,
            start=1
        ):

            print(
                f"{rank}. "
                f"{book['title']} "
                f"({book['year']})"
            )


    # ========================================================
    # EXIT
    # ========================================================

    elif choice == "11":

        print("\nGoodbye!")
        break


    # ========================================================
    # INVALID OPTION
    # ========================================================

    else:

        print(
            "Invalid option. "
            "Please choose between 1 and 11."
        )