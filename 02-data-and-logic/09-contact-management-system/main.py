print("=== Contact Management System ===")


# ============================================================
# Application Data
# ============================================================

contacts = [
    {
        "id": 1,
        "name": "Anurag Bardhan",
        "phone": "9876543210",
        "email": "anurag@example.com",
        "category": "friend"
    },
    {
        "id": 2,
        "name": "Rahul Sharma",
        "phone": "9123456780",
        "email": "rahul@example.com",
        "category": "work"
    },
    {
        "id": 3,
        "name": "Priya Singh",
        "phone": "9988776655",
        "email": "priya@example.com",
        "category": "family"
    }
]

next_contact_id = 4

valid_categories = [
    "friend",
    "family",
    "work",
    "other"
]


# ============================================================
# Main Application
# ============================================================

while True:
    print("\n=== Menu ===")
    print("1. View contacts")
    print("2. Add contact")
    print("3. Search contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Filter contacts")
    print("7. Sort contacts")
    print("8. Show statistics")
    print("9. Exit")

    choice = input("Choose an option: ").strip()


    # ========================================================
    # VIEW CONTACTS
    # ========================================================

    if choice == "1":

        if not contacts:
            print("\nNo contacts available.")
            continue

        print("\n=== Contacts ===")

        for contact in contacts:
            print(
                f"[{contact['id']}] "
                f"{contact['name']} | "
                f"{contact['phone']} | "
                f"{contact['email']} | "
                f"{contact['category'].title()}"
            )


    # ========================================================
    # ADD CONTACT
    # ========================================================

    elif choice == "2":

        name = input("Name: ").strip()

        if not name:
            print("Name cannot be empty.")
            continue

        phone = input("Phone: ").strip()

        if not phone:
            print("Phone number cannot be empty.")
            continue

        # Check duplicate phone number
        duplicate_phone = False

        for contact in contacts:
            if contact["phone"] == phone:
                duplicate_phone = True
                break

        if duplicate_phone:
            print("A contact with this phone number already exists.")
            continue


        email = input("Email: ").strip().lower()

        if not email:
            print("Email cannot be empty.")
            continue


        while True:
            category = input(
                "Category (friend / family / work / other): "
            ).strip().lower()

            if category in valid_categories:
                break

            print(
                "Invalid category. "
                "Choose friend, family, work, or other."
            )


        contact = {
            "id": next_contact_id,
            "name": name.title(),
            "phone": phone,
            "email": email,
            "category": category
        }

        contacts.append(contact)
        next_contact_id += 1

        print(
            f"Contact #{contact['id']} "
            "added successfully."
        )


    # ========================================================
    # SEARCH CONTACTS
    # ========================================================

    elif choice == "3":

        if not contacts:
            print("\nNo contacts available.")
            continue

        search_term = input(
            "Search by name, phone, or email: "
        ).strip().lower()

        if not search_term:
            print("Search term cannot be empty.")
            continue

        matching_contacts = []

        for contact in contacts:
            if (
                search_term in contact["name"].lower()
                or search_term in contact["phone"]
                or search_term in contact["email"].lower()
            ):
                matching_contacts.append(contact)

        if not matching_contacts:
            print("No matching contacts found.")
            continue

        print("\n=== Search Results ===")

        for contact in matching_contacts:
            print(
                f"[{contact['id']}] "
                f"{contact['name']} | "
                f"{contact['phone']} | "
                f"{contact['email']} | "
                f"{contact['category'].title()}"
            )


    # ========================================================
    # UPDATE CONTACT
    # ========================================================

    elif choice == "4":

        if not contacts:
            print("\nNo contacts available.")
            continue

        try:
            contact_id = int(
                input("Enter contact ID to update: ")
            )

        except ValueError:
            print("Please enter a valid contact ID.")
            continue


        contact_found = False

        for contact in contacts:

            if contact["id"] == contact_id:

                print(
                    f"\nCurrent name: {contact['name']}"
                )
                new_name = input(
                    "New name (press Enter to keep current): "
                ).strip()

                if new_name:
                    contact["name"] = new_name.title()


                print(
                    f"Current phone: {contact['phone']}"
                )
                new_phone = input(
                    "New phone (press Enter to keep current): "
                ).strip()

                if new_phone:

                    duplicate_phone = False

                    for other_contact in contacts:
                        if (
                            other_contact["id"] != contact_id
                            and other_contact["phone"] == new_phone
                        ):
                            duplicate_phone = True
                            break

                    if duplicate_phone:
                        print(
                            "Phone number already belongs "
                            "to another contact."
                        )
                    else:
                        contact["phone"] = new_phone


                print(
                    f"Current email: {contact['email']}"
                )
                new_email = input(
                    "New email (press Enter to keep current): "
                ).strip().lower()

                if new_email:
                    contact["email"] = new_email


                while True:
                    new_category = input(
                        "New category "
                        "(press Enter to keep current): "
                    ).strip().lower()

                    if not new_category:
                        break

                    if new_category in valid_categories:
                        contact["category"] = new_category
                        break

                    print(
                        "Invalid category. "
                        "Choose friend, family, work, or other."
                    )


                print("Contact updated successfully.")
                contact_found = True
                break


        if not contact_found:
            print("Contact ID not found.")


    # ========================================================
    # DELETE CONTACT
    # ========================================================

    elif choice == "5":

        if not contacts:
            print("\nNo contacts available.")
            continue

        try:
            contact_id = int(
                input("Enter contact ID to delete: ")
            )

        except ValueError:
            print("Please enter a valid contact ID.")
            continue


        contact_found = False

        for contact in contacts:

            if contact["id"] == contact_id:
                contacts.remove(contact)
                print("Contact deleted successfully.")
                contact_found = True
                break


        if not contact_found:
            print("Contact ID not found.")


    # ========================================================
    # FILTER CONTACTS
    # ========================================================

    elif choice == "6":

        if not contacts:
            print("\nNo contacts available.")
            continue

        category = input(
            "Filter by category "
            "(friend / family / work / other): "
        ).strip().lower()

        if category not in valid_categories:
            print("Invalid category.")
            continue


        filtered_contacts = [
            contact
            for contact in contacts
            if contact["category"] == category
        ]


        if not filtered_contacts:
            print(
                f"No contacts found in the "
                f"{category} category."
            )
            continue


        print(
            f"\n=== {category.title()} Contacts ==="
        )

        for contact in filtered_contacts:
            print(
                f"[{contact['id']}] "
                f"{contact['name']} | "
                f"{contact['phone']} | "
                f"{contact['email']}"
            )


    # ========================================================
    # SORT CONTACTS
    # ========================================================

    elif choice == "7":

        if not contacts:
            print("\nNo contacts available.")
            continue

        print("\nSort by:")
        print("1. Name")
        print("2. Category")
        print("3. ID")

        sort_choice = input(
            "Choose sorting option: "
        ).strip()


        if sort_choice == "1":

            sorted_contacts = sorted(
                contacts,
                key=lambda contact: contact["name"].lower()
            )

        elif sort_choice == "2":

            sorted_contacts = sorted(
                contacts,
                key=lambda contact: contact["category"]
            )

        elif sort_choice == "3":

            sorted_contacts = sorted(
                contacts,
                key=lambda contact: contact["id"]
            )

        else:
            print("Invalid sorting option.")
            continue


        print("\n=== Sorted Contacts ===")

        for contact in sorted_contacts:
            print(
                f"[{contact['id']}] "
                f"{contact['name']} | "
                f"{contact['phone']} | "
                f"{contact['email']} | "
                f"{contact['category'].title()}"
            )


    # ========================================================
    # STATISTICS
    # ========================================================

    elif choice == "8":

        total_contacts = len(contacts)

        category_counts = {
            "friend": 0,
            "family": 0,
            "work": 0,
            "other": 0
        }


        for contact in contacts:
            category_counts[contact["category"]] += 1


        print("\n=== Contact Statistics ===")
        print(f"Total contacts: {total_contacts}")

        print("\nBy category:")
        print(f"- Friends: {category_counts['friend']}")
        print(f"- Family: {category_counts['family']}")
        print(f"- Work: {category_counts['work']}")
        print(f"- Other: {category_counts['other']}")


    # ========================================================
    # EXIT
    # ========================================================

    elif choice == "9":

        print("\nGoodbye!")
        break


    else:

        print(
            "Invalid option. "
            "Please choose between 1 and 9."
        )

