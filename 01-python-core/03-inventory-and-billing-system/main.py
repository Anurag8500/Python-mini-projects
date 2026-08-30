print("=== Inventory & Billing System ===")

inventory = {
    "P001": {
        "name": "Keyboard",
        "price": 1200.00,
        "stock": 10
    },
    "P002": {
        "name": "Mouse",
        "price": 700.00,
        "stock": 15
    },
    "P003": {
        "name": "Headphones",
        "price": 1800.00,
        "stock": 8
    },
    "P004": {
        "name": "Monitor",
        "price": 12000.00,
        "stock": 5
    },
    "P005": {
        "name": "Webcam",
        "price": 2500.00,
        "stock": 7
    }
}

cart = {}


while True:
    print("\n=== Menu ===")
    print("1. View inventory")
    print("2. Search products")
    print("3. Add product to cart")
    print("4. View cart")
    print("5. Remove product from cart")
    print("6. Checkout")
    print("7. Exit")

    choice = input("Choose an option: ").strip()

    # View inventory
    if choice == "1":
        print("\n=== Inventory ===")

        for product_id, product in inventory.items():
            print(
                f"{product_id} | "
                f"{product['name']} | "
                f"₹{product['price']:.2f} | "
                f"Stock: {product['stock']}"
            )

    # Search products
    elif choice == "2":
        search_term = input("Search product: ").strip().lower()

        print("\n=== Search Results ===")

        found = False

        for product_id, product in inventory.items():
            if search_term in product["name"].lower():
                print(
                    f"{product_id} | "
                    f"{product['name']} | "
                    f"₹{product['price']:.2f} | "
                    f"Stock: {product['stock']}"
                )
                found = True

        if not found:
            print("No matching products found.")

    # Add product to cart
    elif choice == "3":
        product_id = input("Enter product ID: ").strip().upper()

        if product_id not in inventory:
            print("Product not found.")
            continue

        product = inventory[product_id]

        print(
            f"{product['name']} | "
            f"₹{product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        current_cart_quantity = cart.get(product_id, 0)

        if current_cart_quantity + quantity > product["stock"]:
            print("Not enough stock available.")
            continue

        cart[product_id] = current_cart_quantity + quantity

        print(
            f"Added {quantity} x {product['name']} "
            f"to the cart."
        )

    # View cart
    elif choice == "4":
        if not cart:
            print("\nCart is empty.")
            continue

        print("\n=== Cart ===")

        cart_total = 0

        for product_id, quantity in cart.items():
            product = inventory[product_id]

            item_total = product["price"] * quantity
            cart_total += item_total

            print(
                f"{product['name']} | "
                f"{quantity} x ₹{product['price']:.2f} = "
                f"₹{item_total:.2f}"
            )

        print(f"\nCart total: ₹{cart_total:.2f}")

    # Remove product from cart
    elif choice == "5":
        if not cart:
            print("\nCart is empty.")
            continue

        product_id = input("Enter product ID to remove: ").strip().upper()

        if product_id not in cart:
            print("Product is not in the cart.")
            continue

        quantity = int(input("Enter quantity to remove: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        if quantity >= cart[product_id]:
            del cart[product_id]
            print("Product removed from cart.")
        else:
            cart[product_id] -= quantity
            print(f"Removed {quantity} item(s) from cart.")

    # Checkout
    elif choice == "6":
        if not cart:
            print("\nCart is empty.")
            continue

        subtotal = 0

        print("\n=== Bill ===")

        for product_id, quantity in cart.items():
            product = inventory[product_id]

            item_total = product["price"] * quantity
            subtotal += item_total

            print(
                f"{product['name']} | "
                f"{quantity} x ₹{product['price']:.2f} = "
                f"₹{item_total:.2f}"
            )

        # Discount rules
        if subtotal >= 10000:
            discount_rate = 0.10
        elif subtotal >= 5000:
            discount_rate = 0.05
        else:
            discount_rate = 0

        discount = subtotal * discount_rate
        final_total = subtotal - discount

        print(f"\nSubtotal: ₹{subtotal:.2f}")
        print(f"Discount: {discount_rate * 100:.0f}%")
        print(f"Discount amount: ₹{discount:.2f}")
        print(f"Final total: ₹{final_total:.2f}")

        # Update inventory
        for product_id, quantity in cart.items():
            inventory[product_id]["stock"] -= quantity

        cart.clear()

        print("\nCheckout successful.")
        print("Inventory updated.")

    # Exit
    elif choice == "7":
        print("Thank you for using the Inventory & Billing System.")
        break

    else:
        print("Invalid option. Please choose between 1 and 7.")

