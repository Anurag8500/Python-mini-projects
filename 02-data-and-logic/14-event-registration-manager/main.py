print("=== Event Registration Manager ===")


# ============================================================
# Event Data
# ============================================================

events = [
    {
        "id": 1,
        "name": "Python Workshop",
        "category": "technical",
        "capacity": 50,
        "date": "15 September 2026",
        "participants": [
            {
                "id": 1,
                "name": "Anurag Bardhan",
                "email": "anurag@example.com"
            },
            {
                "id": 2,
                "name": "Rahul Sharma",
                "email": "rahul@example.com"
            }
        ]
    },
    {
        "id": 2,
        "name": "Startup Meetup",
        "category": "business",
        "capacity": 30,
        "date": "20 September 2026",
        "participants": [
            {
                "id": 3,
                "name": "Priya Singh",
                "email": "priya@example.com"
            }
        ]
    },
    {
        "id": 3,
        "name": "Photography Walk",
        "category": "creative",
        "capacity": 20,
        "date": "25 September 2026",
        "participants": [
            {
                "id": 4,
                "name": "Rohan Das",
                "email": "rohan@example.com"
            }
        ]
    }
]


next_event_id = 4
next_participant_id = 5

valid_categories = [
    "technical",
    "business",
    "creative",
    "sports",
    "education",
    "other"
]


# ============================================================
# Main Menu
# ============================================================

while True:

    print("\n=== Menu ===")
    print("1. View all events")
    print("2. Create event")
    print("3. Register participant")
    print("4. Cancel registration")
    print("5. View event participants")
    print("6. Search events")
    print("7. Filter events")
    print("8. Event statistics")
    print("9. Registration statistics")
    print("10. Detailed report")
    print("11. Exit")

    choice = input("Choose an option: ").strip()


    # ========================================================
    # VIEW ALL EVENTS
    # ========================================================

    if choice == "1":

        print("\n=== All Events ===")

        if not events:
            print("No events available.")
            continue


        for event in events:

            participant_count = len(
                event["participants"]
            )

            available_seats = (
                event["capacity"]
                - participant_count
            )


            print(
                f"\n[{event['id']}] "
                f"{event['name']}"
            )

            print(
                f"  Category: "
                f"{event['category'].title()}"
            )

            print(
                f"  Date: "
                f"{event['date']}"
            )

            print(
                f"  Capacity: "
                f"{event['capacity']}"
            )

            print(
                f"  Registered: "
                f"{participant_count}"
            )

            print(
                f"  Available seats: "
                f"{available_seats}"
            )


    # ========================================================
    # CREATE EVENT
    # ========================================================

    elif choice == "2":

        print("\n=== Create Event ===")

        name = input(
            "Event name: "
        ).strip()


        if not name:
            print("Event name cannot be empty.")
            continue


        # Check duplicate event names

        duplicate_event = False

        for event in events:

            if event["name"].lower() == name.lower():

                duplicate_event = True
                break


        if duplicate_event:

            print(
                "An event with this name already exists."
            )

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


        date = input(
            "Event date: "
        ).strip()


        if not date:

            print("Date cannot be empty.")
            continue


        while True:

            try:

                capacity = int(
                    input("Capacity: ").strip()
                )


                if capacity <= 0:

                    print(
                        "Capacity must be greater than 0."
                    )

                    continue


                break


            except ValueError:

                print(
                    "Please enter a valid whole number."
                )


        events.append(
            {
                "id": next_event_id,
                "name": name.title(),
                "category": category,
                "capacity": capacity,
                "date": date,
                "participants": []
            }
        )


        print(
            f"Event created successfully "
            f"with ID {next_event_id}."
        )


        next_event_id += 1


    # ========================================================
    # REGISTER PARTICIPANT
    # ========================================================

    elif choice == "3":

        print("\n=== Register Participant ===")


        if not events:

            print("No events available.")
            continue


        try:

            event_id = int(
                input("Enter event ID: ").strip()
            )

        except ValueError:

            print("Please enter a valid event ID.")
            continue


        selected_event = None


        for event in events:

            if event["id"] == event_id:

                selected_event = event
                break


        if selected_event is None:

            print("Event not found.")
            continue


        current_participants = len(
            selected_event["participants"]
        )


        if (
            current_participants
            >= selected_event["capacity"]
        ):

            print(
                "Registration is full. "
                "No seats are available."
            )

            continue


        print(
            f"\nEvent: "
            f"{selected_event['name']}"
        )

        print(
            f"Available seats: "
            f"{selected_event['capacity'] - current_participants}"
        )


        name = input(
            "Participant name: "
        ).strip()


        if not name:

            print("Participant name cannot be empty.")
            continue


        email = input(
            "Participant email: "
        ).strip().lower()


        if not email:

            print("Email cannot be empty.")
            continue


        # Check duplicate email in this event

        duplicate_participant = False

        for participant in selected_event["participants"]:

            if participant["email"] == email:

                duplicate_participant = True
                break


        if duplicate_participant:

            print(
                "This participant is already "
                "registered for this event."
            )

            continue


        selected_event["participants"].append(
            {
                "id": next_participant_id,
                "name": name.title(),
                "email": email
            }
        )


        print(
            f"Participant registered successfully "
            f"with ID {next_participant_id}."
        )


        next_participant_id += 1


    # ========================================================
    # CANCEL REGISTRATION
    # ========================================================

    elif choice == "4":

        print("\n=== Cancel Registration ===")


        try:

            event_id = int(
                input("Enter event ID: ").strip()
            )

        except ValueError:

            print("Please enter a valid event ID.")
            continue


        selected_event = None


        for event in events:

            if event["id"] == event_id:

                selected_event = event
                break


        if selected_event is None:

            print("Event not found.")
            continue


        if not selected_event["participants"]:

            print(
                "There are no registered participants."
            )

            continue


        print(
            f"\nParticipants in "
            f"{selected_event['name']}:"
        )


        for participant in selected_event["participants"]:

            print(
                f"[{participant['id']}] "
                f"{participant['name']} | "
                f"{participant['email']}"
            )


        try:

            participant_id = int(
                input(
                    "\nEnter participant ID to cancel: "
                ).strip()
            )

        except ValueError:

            print("Please enter a valid participant ID.")
            continue


        selected_participant = None


        for participant in selected_event["participants"]:

            if participant["id"] == participant_id:

                selected_participant = participant
                break


        if selected_participant is None:

            print(
                "Participant not found in this event."
            )

            continue


        selected_event["participants"].remove(
            selected_participant
        )


        print(
            f"Registration for "
            f"'{selected_participant['name']}' "
            f"cancelled successfully."
        )


    # ========================================================
    # VIEW EVENT PARTICIPANTS
    # ========================================================

    elif choice == "5":

        print("\n=== Event Participants ===")


        try:

            event_id = int(
                input("Enter event ID: ").strip()
            )

        except ValueError:

            print("Please enter a valid event ID.")
            continue


        selected_event = None


        for event in events:

            if event["id"] == event_id:

                selected_event = event
                break


        if selected_event is None:

            print("Event not found.")
            continue


        print(
            f"\n=== Participants: "
            f"{selected_event['name']} ==="
        )


        participants = selected_event["participants"]


        if not participants:

            print("No participants registered.")
            continue


        for number, participant in enumerate(
            participants,
            start=1
        ):

            print(
                f"{number}. "
                f"{participant['name']} | "
                f"{participant['email']}"
            )


        print(
            f"\nRegistered: "
            f"{len(participants)}"
        )

        print(
            f"Capacity: "
            f"{selected_event['capacity']}"
        )

        print(
            f"Available seats: "
            f"{selected_event['capacity'] - len(participants)}"
        )


    # ========================================================
    # SEARCH EVENTS
    # ========================================================

    elif choice == "6":

        search_term = input(
            "Search by event name or category: "
        ).strip().lower()


        if not search_term:

            print("Search term cannot be empty.")
            continue


        matching_events = [

            event

            for event in events

            if (
                search_term in event["name"].lower()
                or search_term in event["category"].lower()
            )
        ]


        if not matching_events:

            print("No matching events found.")
            continue


        print("\n=== Search Results ===")


        for event in matching_events:

            print(
                f"[{event['id']}] "
                f"{event['name']} | "
                f"{event['category'].title()} | "
                f"{event['date']}"
            )


    # ========================================================
    # FILTER EVENTS
    # ========================================================

    elif choice == "7":

        print("\n=== Filter Events ===")
        print("1. By category")
        print("2. Events with available seats")
        print("3. Full events")


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


            matching_events = [

                event

                for event in events

                if event["category"] == category
            ]


        elif filter_choice == "2":

            matching_events = [

                event

                for event in events

                if len(event["participants"])
                < event["capacity"]
            ]


        elif filter_choice == "3":

            matching_events = [

                event

                for event in events

                if len(event["participants"])
                >= event["capacity"]
            ]


        else:

            print("Invalid filter option.")
            continue


        if not matching_events:

            print("No events matched the filter.")
            continue


        print("\n=== Filter Results ===")


        for event in matching_events:

            registered = len(
                event["participants"]
            )

            available = (
                event["capacity"]
                - registered
            )


            print(
                f"[{event['id']}] "
                f"{event['name']} | "
                f"Registered: {registered}/"
                f"{event['capacity']} | "
                f"Available: {available}"
            )


    # ========================================================
    # EVENT STATISTICS
    # ========================================================

    elif choice == "8":

        if not events:

            print("No events available.")
            continue


        total_events = len(events)


        total_capacity = sum(
            event["capacity"]
            for event in events
        )


        total_registrations = sum(
            len(event["participants"])
            for event in events
        )


        available_seats = (
            total_capacity
            - total_registrations
        )


        most_popular_event = max(
            events,
            key=lambda event:
                len(event["participants"])
        )


        highest_capacity_event = max(
            events,
            key=lambda event:
                event["capacity"]
        )


        print("\n=== Event Statistics ===")


        print(
            f"Total events: "
            f"{total_events}"
        )


        print(
            f"Total capacity: "
            f"{total_capacity}"
        )


        print(
            f"Total registrations: "
            f"{total_registrations}"
        )


        print(
            f"Available seats: "
            f"{available_seats}"
        )


        print(
            f"Most popular event: "
            f"{most_popular_event['name']} "
            f"({len(most_popular_event['participants'])} registrations)"
        )


        print(
            f"Largest event: "
            f"{highest_capacity_event['name']} "
            f"({highest_capacity_event['capacity']} seats)"
        )


    # ========================================================
    # REGISTRATION STATISTICS
    # ========================================================

    elif choice == "9":

        if not events:

            print("No events available.")
            continue


        category_data = {}


        for event in events:

            category = event["category"]

            if category not in category_data:

                category_data[category] = {
                    "event_count": 0,
                    "registrations": 0,
                    "capacity": 0
                }


            category_data[category]["event_count"] += 1

            category_data[category]["registrations"] += (
                len(event["participants"])
            )

            category_data[category]["capacity"] += (
                event["capacity"]
            )


        total_registrations = sum(
            data["registrations"]
            for data in category_data.values()
        )


        print("\n=== Registration Statistics ===")


        for category, data in sorted(
            category_data.items(),
            key=lambda item: item[1]["registrations"],
            reverse=True
        ):

            fill_rate = (
                data["registrations"]
                / data["capacity"]
                * 100
            )


            print(
                f"\n{category.title()}"
            )

            print(
                f"  Events: "
                f"{data['event_count']}"
            )

            print(
                f"  Registrations: "
                f"{data['registrations']}"
            )

            print(
                f"  Capacity: "
                f"{data['capacity']}"
            )

            print(
                f"  Fill rate: "
                f"{fill_rate:.2f}%"
            )


        print(
            f"\nTotal registrations: "
            f"{total_registrations}"
        )


    # ========================================================
    # DETAILED REPORT
    # ========================================================

    elif choice == "10":

        if not events:

            print("No events available.")
            continue


        total_capacity = sum(
            event["capacity"]
            for event in events
        )


        total_registrations = sum(
            len(event["participants"])
            for event in events
        )


        available_seats = (
            total_capacity
            - total_registrations
        )


        average_registrations = (
            total_registrations
            / len(events)
        )


        most_popular_event = max(
            events,
            key=lambda event:
                len(event["participants"])
        )


        category_counts = {}


        for event in events:

            category = event["category"]

            category_counts[category] = (
                category_counts.get(category, 0) + 1
            )


        print("\n========================================")
        print("       DETAILED EVENT REPORT")
        print("========================================")


        print(
            f"\nTotal events          : "
            f"{len(events)}"
        )


        print(
            f"Total capacity       : "
            f"{total_capacity}"
        )


        print(
            f"Total registrations   : "
            f"{total_registrations}"
        )


        print(
            f"Available seats       : "
            f"{available_seats}"
        )


        print(
            f"Average registrations: "
            f"{average_registrations:.2f}"
        )


        print(
            f"Most popular event   : "
            f"{most_popular_event['name']}"
        )


        print("\nEvents by category:")


        for category, count in sorted(
            category_counts.items()
        ):

            print(
                f"- {category.title()}: "
                f"{count}"
            )


        print("\nEvent occupancy:")


        ranked_events = sorted(
            events,
            key=lambda event:
                len(event["participants"])
                / event["capacity"],
            reverse=True
        )


        for rank, event in enumerate(
            ranked_events,
            start=1
        ):

            registered = len(
                event["participants"]
            )


            occupancy = (
                registered
                / event["capacity"]
                * 100
            )


            print(
                f"{rank}. "
                f"{event['name']} — "
                f"{registered}/{event['capacity']} "
                f"({occupancy:.2f}%)"
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