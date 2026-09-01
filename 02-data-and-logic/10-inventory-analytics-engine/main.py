print("=== Inventory Analytics Engine ===")


# ============================================================
# Inventory Data
# ============================================================

products = [
    {
        "id": "P001",
        "name": "Mechanical Keyboard",
        "category": "peripherals",
        "price": 4500.00,
        "stock": 12
    },
    {
        "id": "P002",
        "name": "Wireless Mouse",
        "category": "peripherals",
        "price": 1800.00,
        "stock": 25
    },
    {
        "id": "P003",
        "name": "Gaming Headset",
        "category": "audio",
        "price": 3200.00,
        "stock": 8
    },
    {
        "id": "P004",
        "name": "4K Monitor",
        "category": "displays",
        "price": 28000.00,
        "stock": 5
    },
    {
        "id": "P005",
        "name": "Webcam",
        "category": "peripherals",
        "price": 3500.00,
        "stock": 4
    },
    {
        "id": "P006",
        "name": "USB Microphone",
        "category": "audio",
        "price": 6200.00,
        "stock": 7
    },
    {
        "id": "P007",
        "name": "1TB SSD",
        "category": "storage",
        "price": 7200.00,
        "stock": 10
    },
    {
        "id": "P008",
        "name": "2TB HDD",
        "category": "storage",
        "price": 5800.00,
        "stock": 14
    },
    {
        "id": "P009",
        "name": "Laptop Stand",
        "category": "accessories",
        "price": 2200.00,
        "stock": 18
    },
    {
        "id": "P010",
        "name": "USB-C Hub",
        "category": "accessories",
        "price": 2600.00,
        "stock": 20
    }
]


LOW_STOCK_LIMIT = 5


# ============================================================
# Main Menu
# ============================================================

while True:
    print("\n=== Menu ===")
    print("1. View all products")
    print("2. Inventory overview")
    print("3. Low-stock products")
    print("4. Most valuable inventory")
    print("5. Category analysis")
    print("6. Price analysis")
    print("7. Stock analysis")
    print("8. Search products")
    print("9. Detailed inventory report")
    print("10. Exit")

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
                f"Category: {product['category'].title()} | "
                f"Price: ₹{product['price']:.2f} | "
                f"Stock: {product['stock']}"
            )


    # ========================================================
    # INVENTORY OVERVIEW
    # ========================================================

    elif choice == "2":

        total_products = len(products)

        total_units = sum(
            product["stock"]
            for product in products
        )

        total_inventory_value = sum(
            product["price"] * product["stock"]
            for product in products
        )

        average_price = (
            sum(product["price"] for product in products)
            / total_products
        )

        average_stock = total_units / total_products


        most_expensive = max(
            products,
            key=lambda product: product["price"]
        )

        cheapest = min(
            products,
            key=lambda product: product["price"]
        )

        highest_value_product = max(
            products,
            key=lambda product:
                product["price"] * product["stock"]
        )


        print("\n=== Inventory Overview ===")
        print(f"Total products: {total_products}")
        print(f"Total units: {total_units}")
        print(
            f"Total inventory value: "
            f"₹{total_inventory_value:,.2f}"
        )

        print(
            f"Average product price: "
            f"₹{average_price:,.2f}"
        )

        print(
            f"Average stock per product: "
            f"{average_stock:.2f}"
        )

        print(
            f"Most expensive product: "
            f"{most_expensive['name']} "
            f"(₹{most_expensive['price']:,.2f})"
        )

        print(
            f"Cheapest product: "
            f"{cheapest['name']} "
            f"(₹{cheapest['price']:,.2f})"
        )

        print(
            f"Highest inventory value: "
            f"{highest_value_product['name']} "
            f"(₹"
            f"{highest_value_product['price'] * highest_value_product['stock']:,.2f}"
            f")"
        )


    # ========================================================
    # LOW-STOCK PRODUCTS
    # ========================================================

    elif choice == "3":

        low_stock_products = [
            product
            for product in products
            if product["stock"] <= LOW_STOCK_LIMIT
        ]


        print("\n=== Low-Stock Products ===")

        if not low_stock_products:
            print("No low-stock products.")
            continue


        for product in sorted(
            low_stock_products,
            key=lambda product: product["stock"]
        ):
            print(
                f"[{product['id']}] "
                f"{product['name']} | "
                f"Stock: {product['stock']} | "
                f"Price: ₹{product['price']:,.2f}"
            )


    # ========================================================
    # MOST VALUABLE INVENTORY
    # ========================================================

    elif choice == "4":

        valuable_products = sorted(
            products,
            key=lambda product:
                product["price"] * product["stock"],
            reverse=True
        )


        print("\n=== Most Valuable Inventory ===")

        for rank, product in enumerate(
            valuable_products[:5],
            start=1
        ):

            inventory_value = (
                product["price"] * product["stock"]
            )

            print(
                f"{rank}. {product['name']} | "
                f"Stock: {product['stock']} | "
                f"Inventory value: "
                f"₹{inventory_value:,.2f}"
            )


    # ========================================================
    # CATEGORY ANALYSIS
    # ========================================================

    elif choice == "5":

        category_data = {}


        for product in products:

            category = product["category"]

            if category not in category_data:
                category_data[category] = {
                    "product_count": 0,
                    "total_units": 0,
                    "total_value": 0
                }


            category_data[category]["product_count"] += 1

            category_data[category]["total_units"] += (
                product["stock"]
            )

            category_data[category]["total_value"] += (
                product["price"] * product["stock"]
            )


        print("\n=== Category Analysis ===")


        ranked_categories = sorted(
            category_data.items(),
            key=lambda item: item[1]["total_value"],
            reverse=True
        )


        for category, data in ranked_categories:

            print(f"\n{category.title()}")

            print(
                f"  Products: "
                f"{data['product_count']}"
            )

            print(
                f"  Units: "
                f"{data['total_units']}"
            )

            print(
                f"  Inventory value: "
                f"₹{data['total_value']:,.2f}"
            )


    # ========================================================
    # PRICE ANALYSIS
    # ========================================================

    elif choice == "6":

        sorted_by_price = sorted(
            products,
            key=lambda product: product["price"],
            reverse=True
        )


        print("\n=== Price Analysis ===")

        print("\nMost expensive products:")

        for product in sorted_by_price[:5]:
            print(
                f"- {product['name']}: "
                f"₹{product['price']:,.2f}"
            )


        print("\nCheapest products:")

        for product in sorted(
            products,
            key=lambda product: product["price"]
        )[:5]:

            print(
                f"- {product['name']}: "
                f"₹{product['price']:,.2f}"
            )


    # ========================================================
    # STOCK ANALYSIS
    # ========================================================

    elif choice == "7":

        highest_stock = max(
            products,
            key=lambda product: product["stock"]
        )

        lowest_stock = min(
            products,
            key=lambda product: product["stock"]
        )


        total_units = sum(
            product["stock"]
            for product in products
        )

        average_stock = total_units / len(products)


        print("\n=== Stock Analysis ===")

        print(
            f"Highest stock: "
            f"{highest_stock['name']} "
            f"({highest_stock['stock']} units)"
        )

        print(
            f"Lowest stock: "
            f"{lowest_stock['name']} "
            f"({lowest_stock['stock']} units)"
        )

        print(
            f"Average stock: "
            f"{average_stock:.2f} units"
        )


    # ========================================================
    # SEARCH PRODUCTS
    # ========================================================

    elif choice == "8":

        search_term = input(
            "Search by product name or category: "
        ).strip().lower()


        if not search_term:
            print("Search term cannot be empty.")
            continue


        matching_products = [
            product
            for product in products
            if (
                search_term in product["name"].lower()
                or search_term in product["category"].lower()
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
                f"₹{product['price']:,.2f} | "
                f"Stock: {product['stock']}"
            )


    # ========================================================
    # DETAILED INVENTORY REPORT
    # ========================================================

    elif choice == "9":

        total_products = len(products)

        total_units = sum(
            product["stock"]
            for product in products
        )

        total_inventory_value = sum(
            product["price"] * product["stock"]
            for product in products
        )


        low_stock_count = sum(
            1
            for product in products
            if product["stock"] <= LOW_STOCK_LIMIT
        )


        category_counts = {}

        for product in products:

            category = product["category"]

            category_counts[category] = (
                category_counts.get(category, 0) + 1
            )


        print("\n========================================")
        print("       DETAILED INVENTORY REPORT")
        print("========================================")

        print(f"\nTotal products       : {total_products}")
        print(f"Total units          : {total_units}")
        print(
            f"Total inventory value: "
            f"₹{total_inventory_value:,.2f}"
        )

        print(f"Low-stock products   : {low_stock_count}")


        print("\nProducts by category:")

        for category, count in category_counts.items():
            print(
                f"- {category.title()}: "
                f"{count}"
            )


        print("\nTop 3 products by inventory value:")

        top_products = sorted(
            products,
            key=lambda product:
                product["price"] * product["stock"],
            reverse=True
        )[:3]


        for rank, product in enumerate(
            top_products,
            start=1
        ):

            value = product["price"] * product["stock"]

            print(
                f"{rank}. "
                f"{product['name']} — "
                f"₹{value:,.2f}"
            )


    # ========================================================
    # EXIT
    # ========================================================

    elif choice == "10":

        print("\nGoodbye!")
        break


    else:

        print(
            "Invalid option. "
            "Please choose between 1 and 10."
        )
