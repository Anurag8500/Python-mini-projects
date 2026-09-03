print("=== Search & Filtering Engine ===")


# ============================================================
# Product Data
# ============================================================

products = [
    {
        "id": "P001",
        "name": "Mechanical Keyboard",
        "category": "peripherals",
        "brand": "Logitech",
        "price": 4500.00,
        "rating": 4.5,
        "stock": 12
    },
    {
        "id": "P002",
        "name": "Wireless Mouse",
        "category": "peripherals",
        "brand": "Logitech",
        "price": 1800.00,
        "rating": 4.3,
        "stock": 25
    },
    {
        "id": "P003",
        "name": "Gaming Headset",
        "category": "audio",
        "brand": "HyperX",
        "price": 3200.00,
        "rating": 4.6,
        "stock": 8
    },
    {
        "id": "P004",
        "name": "4K Monitor",
        "category": "displays",
        "brand": "Samsung",
        "price": 28000.00,
        "rating": 4.8,
        "stock": 5
    },
    {
        "id": "P005",
        "name": "Webcam",
        "category": "peripherals",
        "brand": "Logitech",
        "price": 3500.00,
        "rating": 4.2,
        "stock": 4
    },
    {
        "id": "P006",
        "name": "USB Microphone",
        "category": "audio",
        "brand": "Razer",
        "price": 6200.00,
        "rating": 4.7,
        "stock": 7
    },
    {
        "id": "P007",
        "name": "1TB SSD",
        "category": "storage",
        "brand": "Samsung",
        "price": 7200.00,
        "rating": 4.9,
        "stock": 10
    },
    {
        "id": "P008",
        "name": "2TB HDD",
        "category": "storage",
        "brand": "Western Digital",
        "price": 5800.00,
        "rating": 4.4,
        "stock": 14
    },
    {
        "id": "P009",
        "name": "Laptop Stand",
        "category": "accessories",
        "brand": "Portronics",
        "price": 2200.00,
        "rating": 4.1,
        "stock": 18
    },
    {
        "id": "P010",
        "name": "USB-C Hub",
        "category": "accessories",
        "brand": "Anker",
        "price": 2600.00,
        "rating": 4.5,
        "stock": 20
    },
    {
        "id": "P011",
        "name": "Gaming Mouse",
        "category": "peripherals",
        "brand": "Razer",
        "price": 2900.00,
        "rating": 4.6,
        "stock": 9
    },
    {
        "id": "P012",
        "name": "Bluetooth Speaker",
        "category": "audio",
        "brand": "JBL",
        "price": 4800.00,
        "rating": 4.7,
        "stock": 6
    }
]


# ============================================================
# Main Menu
# ============================================================

while True:

    print("\n=== Menu ===")
    print("1. View all products")
    print("2. Search by keyword")
    print("3. Filter by category")
    print("4. Filter by price range")
    print("5. Filter by stock range")
    print("6. Advanced filter")
    print("7. Sort products")
    print("8. Search + filters")
    print("9. Search statistics")
    print("10. Detailed report")
    print("11. Exit")

    choice = input("Choose an option: ").strip()


    # ========================================================
    # VIEW ALL PRODUCTS
    # ========================================================

    if choice == "1":

        print("\n=== All Products ===")

        for product in products:

            print(
                f"[{product['id']}] "
                f"{product['name']} | "
                f"{product['category'].title()} | "
                f"{product['brand']} | "
                f"₹{product['price']:,.2f} | "
                f"Rating: {product['rating']:.1f} | "
                f"Stock: {product['stock']}"
            )


    # ========================================================
    # SEARCH BY KEYWORD
    # ========================================================

    elif choice == "2":

        search_term = input(
            "Enter keyword: "
        ).strip().lower()


        if not search_term:

            print("Search keyword cannot be empty.")
            continue


        matching_products = [
            product
            for product in products
            if (
                search_term in product["name"].lower()
                or search_term in product["category"].lower()
                or search_term in product["brand"].lower()
            )
        ]


        if not matching_products:

            print("No matching products found.")
            continue


        print("\n=== Search Results ===")


        for product in matching_products:

            print(
                f"[{product['id']}] "
                f"{product['name']} | "
                f"{product['category'].title()} | "
                f"{product['brand']} | "
                f"₹{product['price']:,.2f} | "
                f"Rating: {product['rating']:.1f}"
            )


    # ========================================================
    # FILTER BY CATEGORY
    # ========================================================

    elif choice == "3":

        category = input(
            "Enter category: "
        ).strip().lower()


        if not category:

            print("Category cannot be empty.")
            continue


        matching_products = [
            product
            for product in products
            if product["category"] == category
        ]


        if not matching_products:

            print(
                "No products found in this category."
            )

            continue


        print(
            f"\n=== {category.title()} Products ==="
        )


        for product in matching_products:

            print(
                f"[{product['id']}] "
                f"{product['name']} | "
                f"{product['brand']} | "
                f"₹{product['price']:,.2f} | "
                f"Rating: {product['rating']:.1f}"
            )


    # ========================================================
    # FILTER BY PRICE RANGE
    # ========================================================

    elif choice == "4":

        print("\n=== Price Range Filter ===")


        while True:

            try:

                minimum_price = float(
                    input("Minimum price: ₹").strip()
                )

                maximum_price = float(
                    input("Maximum price: ₹").strip()
                )


                if minimum_price < 0:

                    print(
                        "Minimum price cannot be negative."
                    )

                    continue


                if maximum_price < minimum_price:

                    print(
                        "Maximum price must be greater "
                        "than or equal to minimum price."
                    )

                    continue


                break


            except ValueError:

                print(
                    "Please enter valid numeric values."
                )


        matching_products = [
            product
            for product in products
            if (
                minimum_price
                <= product["price"]
                <= maximum_price
            )
        ]


        if not matching_products:

            print(
                "No products found in this price range."
            )

            continue


        print("\n=== Price Filter Results ===")


        for product in matching_products:

            print(
                f"[{product['id']}] "
                f"{product['name']} | "
                f"₹{product['price']:,.2f}"
            )


    # ========================================================
    # FILTER BY STOCK RANGE
    # ========================================================

    elif choice == "5":

        print("\n=== Stock Range Filter ===")


        while True:

            try:

                minimum_stock = int(
                    input("Minimum stock: ").strip()
                )

                maximum_stock = int(
                    input("Maximum stock: ").strip()
                )


                if minimum_stock < 0:

                    print(
                        "Minimum stock cannot be negative."
                    )

                    continue


                if maximum_stock < minimum_stock:

                    print(
                        "Maximum stock must be greater "
                        "than or equal to minimum stock."
                    )

                    continue


                break


            except ValueError:

                print(
                    "Please enter valid whole numbers."
                )


        matching_products = [
            product
            for product in products
            if (
                minimum_stock
                <= product["stock"]
                <= maximum_stock
            )
        ]


        if not matching_products:

            print(
                "No products found in this stock range."
            )

            continue


        print("\n=== Stock Filter Results ===")


        for product in matching_products:

            print(
                f"[{product['id']}] "
                f"{product['name']} | "
                f"Stock: {product['stock']}"
            )


    # ========================================================
    # ADVANCED FILTER
    # ========================================================

    elif choice == "6":

        print("\n=== Advanced Filter ===")
        print("Press Enter to skip any filter.")


        category = input(
            "Category: "
        ).strip().lower()


        brand = input(
            "Brand: "
        ).strip().lower()


        while True:

            minimum_price_input = input(
                "Minimum price: ₹"
            ).strip()


            if minimum_price_input == "":
                minimum_price = None
                break


            try:

                minimum_price = float(
                    minimum_price_input
                )


                if minimum_price < 0:

                    print(
                        "Minimum price cannot be negative."
                    )

                    continue


                break


            except ValueError:

                print(
                    "Please enter a valid number."
                )


        while True:

            maximum_price_input = input(
                "Maximum price: ₹"
            ).strip()


            if maximum_price_input == "":
                maximum_price = None
                break


            try:

                maximum_price = float(
                    maximum_price_input
                )


                if maximum_price < 0:

                    print(
                        "Maximum price cannot be negative."
                    )

                    continue


                if (
                    minimum_price is not None
                    and maximum_price < minimum_price
                ):

                    print(
                        "Maximum price must be greater "
                        "than or equal to minimum price."
                    )

                    continue


                break


            except ValueError:

                print(
                    "Please enter a valid number."
                )


        while True:

            minimum_rating_input = input(
                "Minimum rating (0-5): "
            ).strip()


            if minimum_rating_input == "":
                minimum_rating = None
                break


            try:

                minimum_rating = float(
                    minimum_rating_input
                )


                if (
                    minimum_rating < 0
                    or minimum_rating > 5
                ):

                    print(
                        "Rating must be between 0 and 5."
                    )

                    continue


                break


            except ValueError:

                print(
                    "Please enter a valid rating."
                )


        while True:

            minimum_stock_input = input(
                "Minimum stock: "
            ).strip()


            if minimum_stock_input == "":
                minimum_stock = None
                break


            try:

                minimum_stock = int(
                    minimum_stock_input
                )


                if minimum_stock < 0:

                    print(
                        "Minimum stock cannot be negative."
                    )

                    continue


                break


            except ValueError:

                print(
                    "Please enter a valid whole number."
                )


        matching_products = []


        for product in products:

            if category:

                if product["category"] != category:
                    continue


            if brand:

                if product["brand"].lower() != brand:
                    continue


            if (
                minimum_price is not None
                and product["price"] < minimum_price
            ):

                continue


            if (
                maximum_price is not None
                and product["price"] > maximum_price
            ):

                continue


            if (
                minimum_rating is not None
                and product["rating"] < minimum_rating
            ):

                continue


            if (
                minimum_stock is not None
                and product["stock"] < minimum_stock
            ):

                continue


            matching_products.append(product)


        print("\n=== Advanced Filter Results ===")


        if not matching_products:

            print("No products matched all filters.")
            continue


        for product in matching_products:

            print(
                f"[{product['id']}] "
                f"{product['name']} | "
                f"{product['category'].title()} | "
                f"{product['brand']} | "
                f"₹{product['price']:,.2f} | "
                f"Rating: {product['rating']:.1f} | "
                f"Stock: {product['stock']}"
            )


        print(
            f"\nMatching products: "
            f"{len(matching_products)}"
        )


    # ========================================================
    # SORT PRODUCTS
    # ========================================================

    elif choice == "7":

        print("\n=== Sort Products ===")
        print("1. Price")
        print("2. Rating")
        print("3. Stock")
        print("4. Name")


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

            sorted_products = sorted(
                products,
                key=lambda product: product["price"],
                reverse=reverse
            )

        elif sort_choice == "2":

            sorted_products = sorted(
                products,
                key=lambda product: product["rating"],
                reverse=reverse
            )

        elif sort_choice == "3":

            sorted_products = sorted(
                products,
                key=lambda product: product["stock"],
                reverse=reverse
            )

        elif sort_choice == "4":

            sorted_products = sorted(
                products,
                key=lambda product: product["name"].lower(),
                reverse=reverse
            )

        else:

            print("Invalid sorting field.")
            continue


        print("\n=== Sorted Products ===")


        for product in sorted_products:

            print(
                f"[{product['id']}] "
                f"{product['name']} | "
                f"₹{product['price']:,.2f} | "
                f"Rating: {product['rating']:.1f} | "
                f"Stock: {product['stock']}"
            )


    # ========================================================
    # SEARCH + FILTERS
    # ========================================================

    elif choice == "8":

        print("\n=== Search + Filters ===")
        print("Press Enter to skip any filter.")


        search_term = input(
            "Keyword: "
        ).strip().lower()


        category = input(
            "Category: "
        ).strip().lower()


        brand = input(
            "Brand: "
        ).strip().lower()


        while True:

            minimum_price_input = input(
                "Minimum price: ₹"
            ).strip()


            if minimum_price_input == "":
                minimum_price = None
                break


            try:

                minimum_price = float(
                    minimum_price_input
                )


                if minimum_price < 0:

                    print(
                        "Minimum price cannot be negative."
                    )

                    continue


                break


            except ValueError:

                print(
                    "Please enter a valid number."
                )


        while True:

            maximum_price_input = input(
                "Maximum price: ₹"
            ).strip()


            if maximum_price_input == "":
                maximum_price = None
                break


            try:

                maximum_price = float(
                    maximum_price_input
                )


                if maximum_price < 0:

                    print(
                        "Maximum price cannot be negative."
                    )

                    continue


                if (
                    minimum_price is not None
                    and maximum_price < minimum_price
                ):

                    print(
                        "Maximum price must be greater "
                        "than or equal to minimum price."
                    )

                    continue


                break


            except ValueError:

                print(
                    "Please enter a valid number."
                )


        while True:

            minimum_rating_input = input(
                "Minimum rating: "
            ).strip()


            if minimum_rating_input == "":
                minimum_rating = None
                break


            try:

                minimum_rating = float(
                    minimum_rating_input
                )


                if (
                    minimum_rating < 0
                    or minimum_rating > 5
                ):

                    print(
                        "Rating must be between 0 and 5."
                    )

                    continue


                break


            except ValueError:

                print(
                    "Please enter a valid rating."
                )


        matching_products = []


        for product in products:

            # Keyword condition

            if search_term:

                keyword_match = (
                    search_term in product["name"].lower()
                    or search_term in product["category"].lower()
                    or search_term in product["brand"].lower()
                )


                if not keyword_match:
                    continue


            # Category condition

            if category:

                if product["category"] != category:
                    continue


            # Brand condition

            if brand:

                if product["brand"].lower() != brand:
                    continue


            # Minimum price condition

            if (
                minimum_price is not None
                and product["price"] < minimum_price
            ):

                continue


            # Maximum price condition

            if (
                maximum_price is not None
                and product["price"] > maximum_price
            ):

                continue


            # Rating condition

            if (
                minimum_rating is not None
                and product["rating"] < minimum_rating
            ):

                continue


            matching_products.append(product)


        print("\n=== Combined Search Results ===")


        if not matching_products:

            print(
                "No products matched the selected "
                "search criteria."
            )

            continue


        for product in matching_products:

            print(
                f"[{product['id']}] "
                f"{product['name']} | "
                f"{product['category'].title()} | "
                f"{product['brand']} | "
                f"₹{product['price']:,.2f} | "
                f"Rating: {product['rating']:.1f} | "
                f"Stock: {product['stock']}"
            )


        print(
            f"\nMatching products: "
            f"{len(matching_products)}"
        )


    # ========================================================
    # SEARCH STATISTICS
    # ========================================================

    elif choice == "9":

        print("\n=== Search Statistics ===")


        total_products = len(products)


        average_price = (
            sum(
                product["price"]
                for product in products
            )
            / total_products
        )


        average_rating = (
            sum(
                product["rating"]
                for product in products
            )
            / total_products
        )


        average_stock = (
            sum(
                product["stock"]
                for product in products
            )
            / total_products
        )


        highest_rated = max(
            products,
            key=lambda product: product["rating"]
        )


        lowest_price = min(
            products,
            key=lambda product: product["price"]
        )


        highest_price = max(
            products,
            key=lambda product: product["price"]
        )


        in_stock_count = sum(
            1
            for product in products
            if product["stock"] > 0
        )


        out_of_stock_count = sum(
            1
            for product in products
            if product["stock"] == 0
        )


        category_counts = {}


        for product in products:

            category = product["category"]

            category_counts[category] = (
                category_counts.get(category, 0) + 1
            )


        print(
            f"Total products: "
            f"{total_products}"
        )


        print(
            f"Average price: "
            f"₹{average_price:,.2f}"
        )


        print(
            f"Average rating: "
            f"{average_rating:.2f}"
        )


        print(
            f"Average stock: "
            f"{average_stock:.2f}"
        )


        print(
            f"Highest rated: "
            f"{highest_rated['name']} "
            f"({highest_rated['rating']:.1f})"
        )


        print(
            f"Lowest price: "
            f"{lowest_price['name']} "
            f"(₹{lowest_price['price']:,.2f})"
        )


        print(
            f"Highest price: "
            f"{highest_price['name']} "
            f"(₹{highest_price['price']:,.2f})"
        )


        print(
            f"In-stock products: "
            f"{in_stock_count}"
        )


        print(
            f"Out-of-stock products: "
            f"{out_of_stock_count}"
        )


        print("\nProducts by category:")


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

        if not products:

            print("No products available.")
            continue


        total_products = len(products)


        average_price = (
            sum(
                product["price"]
                for product in products
            )
            / total_products
        )


        average_rating = (
            sum(
                product["rating"]
                for product in products
            )
            / total_products
        )


        average_stock = (
            sum(
                product["stock"]
                for product in products
            )
            / total_products
        )


        highest_rated = max(
            products,
            key=lambda product: product["rating"]
        )


        most_expensive = max(
            products,
            key=lambda product: product["price"]
        )


        cheapest = min(
            products,
            key=lambda product: product["price"]
        )


        most_stocked = max(
            products,
            key=lambda product: product["stock"]
        )


        category_counts = {}


        for product in products:

            category = product["category"]

            category_counts[category] = (
                category_counts.get(category, 0) + 1
            )


        top_rated_products = sorted(
            products,
            key=lambda product: product["rating"],
            reverse=True
        )[:5]


        print("\n========================================")
        print("       DETAILED SEARCH REPORT")
        print("========================================")


        print(
            f"\nTotal products : "
            f"{total_products}"
        )


        print(
            f"Average price  : "
            f"₹{average_price:,.2f}"
        )


        print(
            f"Average rating : "
            f"{average_rating:.2f}"
        )


        print(
            f"Average stock   : "
            f"{average_stock:.2f}"
        )


        print(
            f"Highest rated  : "
            f"{highest_rated['name']} "
            f"({highest_rated['rating']:.1f})"
        )


        print(
            f"Most expensive: "
            f"{most_expensive['name']} "
            f"(₹{most_expensive['price']:,.2f})"
        )


        print(
            f"Cheapest       : "
            f"{cheapest['name']} "
            f"(₹{cheapest['price']:,.2f})"
        )


        print(
            f"Most stocked   : "
            f"{most_stocked['name']} "
            f"({most_stocked['stock']} units)"
        )


        print("\nProducts by category:")


        for category, count in sorted(
            category_counts.items()
        ):

            print(
                f"- {category.title()}: "
                f"{count}"
            )


        print("\nTop 5 rated products:")


        for rank, product in enumerate(
            top_rated_products,
            start=1
        ):

            print(
                f"{rank}. "
                f"{product['name']} — "
                f"{product['rating']:.1f}"
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