print("=== Inventory & Billing System — Refactored ===")


# ============================================================
# Inventory Data
# ============================================================

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


# ============================================================
# Product Functions
# ============================================================

def find_product(product_id):
    """Return a product by ID or None."""

    return inventory.get(product_id)


def display_inventory():
    """Display all products."""

    print("\n=== Inventory ===")

    for product_id, product in inventory.items():

        print(
            f"[{product_id}] "
            f"{product['name']} | "
            f"₹{product['price']:,.2f} | "
            f"Stock: {product['stock']}"
        )


def search_products():
    """Search products by ID or name."""

    search_term = input(
        "Search product: "
    ).strip().lower()


    if not search_term:
        print("Search term cannot be empty.")
        return


    results = [

        (product_id, product)

        for product_id, product in inventory.items()

        if (
            search_term in product_id.lower()
            or search_term in product["name"].lower()
        )
    ]


    if not results:
        print("No matching products found.")
        return


    print("\n=== Search Results ===")


    for product_id, product in results:

        print(
            f"[{product_id}] "
            f"{product['name']} | "
            f"₹{product['price']:,.2f} | "
            f"Stock: {product['stock']}"
        )


# ============================================================
# Cart Functions
# ============================================================

def add_to_cart():
    """Add a product to the cart."""

    product_id = input(
        "Enter product ID: "
    ).strip().upper()


    product = find_product(product_id)


    if product is None:

        print("Product not found.")
        return


    if product["stock"] <= 0:

        print("Product is out of stock.")
        return


    try:

        quantity = int(
            input("Quantity: ").strip()
        )

    except ValueError:

        print("Quantity must be a whole number.")
        return


    if quantity <= 0:

        print("Quantity must be greater than 0.")
        return


    current_quantity = cart.get(
        product_id,
        0
    )


    if current_quantity + quantity > product["stock"]:

        print(
            f"Only {product['stock'] - current_quantity} "
            f"units are available."
        )

        return


    cart[product_id] = (
        current_quantity + quantity
    )


    print(
        f"Added {quantity} "
        f"{product['name']} to cart."
    )


def remove_from_cart():
    """Remove a product from the cart."""

    if not cart:

        print("Cart is empty.")
        return


    product_id = input(
        "Enter product ID to remove: "
    ).strip().upper()


    if product_id not in cart:

        print("Product is not in the cart.")
        return


    del cart[product_id]


    print("Product removed from cart.")


def calculate_cart_total():
    """Return the total cost of all cart items."""

    total = 0


    for product_id, quantity in cart.items():

        product = inventory[product_id]

        total += (
            product["price"]
            * quantity
        )


    return total


def calculate_discount(total):
    """Return discount amount based on total."""

    if total >= 10000:

        return total * 0.10


    elif total >= 5000:

        return total * 0.05


    return 0


def display_cart():
    """Display cart contents and totals."""

    if not cart:

        print("\nCart is empty.")
        return


    print("\n=== Cart ===")


    for product_id, quantity in cart.items():

        product = inventory[product_id]

        item_total = (
            product["price"]
            * quantity
        )


        print(
            f"{product['name']} | "
            f"₹{product['price']:,.2f} × "
            f"{quantity} = "
            f"₹{item_total:,.2f}"
        )


    total = calculate_cart_total()

    discount = calculate_discount(total)

    final_total = total - discount


    print(
        f"\nSubtotal: "
        f"₹{total:,.2f}"
    )

    print(
        f"Discount: "
        f"₹{discount:,.2f}"
    )

    print(
        f"Final total: "
        f"₹{final_total:,.2f}"
    )


# ============================================================
# Checkout
# ============================================================

def checkout():
    """Complete the purchase and update inventory."""

    if not cart:

        print("Cart is empty.")
        return


    display_cart()


    confirmation = input(
        "\nProceed with checkout? (yes/no): "
    ).strip().lower()


    if confirmation != "yes":

        print("Checkout cancelled.")
        return


    # Update stock

    for product_id, quantity in cart.items():

        inventory[product_id]["stock"] -= quantity


    total = calculate_cart_total()

    discount = calculate_discount(total)

    final_total = total - discount


    print("\n=== Checkout Complete ===")

    print(
        f"Subtotal: "
        f"₹{total:,.2f}"
    )

    print(
        f"Discount: "
        f"₹{discount:,.2f}"
    )

    print(
        f"Amount paid: "
        f"₹{final_total:,.2f}"
    )


    cart.clear()


    print("Thank you for your purchase!")


# ============================================================
# Main Menu
# ============================================================

while True:

    print("\n=== Menu ===")
    print("1. View inventory")
    print("2. Search products")
    print("3. Add to cart")
    print("4. View cart")
    print("5. Remove from cart")
    print("6. Checkout")
    print("7. Exit")


    choice = input(
        "Choose an option: "
    ).strip()


    if choice == "1":

        display_inventory()


    elif choice == "2":

        search_products()


    elif choice == "3":

        add_to_cart()


    elif choice == "4":

        display_cart()


    elif choice == "5":

        remove_from_cart()


    elif choice == "6":

        checkout()


    elif choice == "7":

        print("\nGoodbye!")
        break


    else:

        print(
            "Invalid option. "
            "Please choose between 1 and 7."
        )