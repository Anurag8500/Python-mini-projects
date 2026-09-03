print("=== Graph / Route Explorer ===")


# ============================================================
# Graph Data
# ============================================================

graph = {
    "Kolkata": ["Delhi", "Guwahati", "Mumbai"],
    "Delhi": ["Kolkata", "Jaipur", "Mumbai"],
    "Guwahati": ["Kolkata"],
    "Mumbai": ["Kolkata", "Delhi", "Chennai"],
    "Jaipur": ["Delhi"],
    "Chennai": ["Mumbai"]
}


# ============================================================
# Main Menu
# ============================================================

while True:

    print("\n=== Menu ===")
    print("1. View all locations")
    print("2. View connections")
    print("3. Add location")
    print("4. Add connection")
    print("5. Remove connection")
    print("6. Search location")
    print("7. Find direct connections")
    print("8. Find route between locations")
    print("9. Most connected locations")
    print("10. Network statistics")
    print("11. Exit")

    choice = input("Choose an option: ").strip()


    # ========================================================
    # VIEW ALL LOCATIONS
    # ========================================================

    if choice == "1":

        print("\n=== All Locations ===")

        if not graph:
            print("No locations available.")
            continue


        for location in sorted(graph):
            print(f"- {location}")


    # ========================================================
    # VIEW CONNECTIONS
    # ========================================================

    elif choice == "2":

        print("\n=== Connections ===")

        if not graph:
            print("No locations available.")
            continue


        for location in sorted(graph):

            connections = graph[location]

            if connections:
                print(
                    f"{location} -> "
                    f"{', '.join(sorted(connections))}"
                )

            else:
                print(
                    f"{location} -> No connections"
                )


    # ========================================================
    # ADD LOCATION
    # ========================================================

    elif choice == "3":

        print("\n=== Add Location ===")

        location = input(
            "Location name: "
        ).strip().title()


        if not location:
            print("Location name cannot be empty.")
            continue


        if location in graph:
            print("Location already exists.")
            continue


        graph[location] = []

        print(
            f"Location '{location}' "
            f"added successfully."
        )


    # ========================================================
    # ADD CONNECTION
    # ========================================================

    elif choice == "4":

        print("\n=== Add Connection ===")

        first_location = input(
            "First location: "
        ).strip().title()


        second_location = input(
            "Second location: "
        ).strip().title()


        if first_location not in graph:
            print(
                f"Location '{first_location}' "
                f"does not exist."
            )
            continue


        if second_location not in graph:
            print(
                f"Location '{second_location}' "
                f"does not exist."
            )
            continue


        if first_location == second_location:
            print(
                "A location cannot be connected "
                "to itself."
            )
            continue


        if second_location in graph[first_location]:
            print("Connection already exists.")
            continue


        # Add connection in both directions.
        graph[first_location].append(
            second_location
        )

        graph[second_location].append(
            first_location
        )


        print(
            f"Connection added between "
            f"{first_location} and "
            f"{second_location}."
        )


    # ========================================================
    # REMOVE CONNECTION
    # ========================================================

    elif choice == "5":

        print("\n=== Remove Connection ===")

        first_location = input(
            "First location: "
        ).strip().title()


        second_location = input(
            "Second location: "
        ).strip().title()


        if first_location not in graph:
            print("First location does not exist.")
            continue


        if second_location not in graph:
            print("Second location does not exist.")
            continue


        if second_location not in graph[first_location]:
            print("Connection does not exist.")
            continue


        graph[first_location].remove(
            second_location
        )

        graph[second_location].remove(
            first_location
        )


        print(
            f"Connection removed between "
            f"{first_location} and "
            f"{second_location}."
        )


    # ========================================================
    # SEARCH LOCATION
    # ========================================================

    elif choice == "6":

        search_term = input(
            "Search location: "
        ).strip().lower()


        if not search_term:
            print("Search term cannot be empty.")
            continue


        matching_locations = [
            location
            for location in graph
            if search_term in location.lower()
        ]


        if not matching_locations:
            print("No matching locations found.")
            continue


        print("\n=== Search Results ===")


        for location in sorted(matching_locations):

            print(
                f"- {location} "
                f"({len(graph[location])} connections)"
            )


    # ========================================================
    # FIND DIRECT CONNECTIONS
    # ========================================================

    elif choice == "7":

        print("\n=== Direct Connections ===")

        location = input(
            "Enter location: "
        ).strip().title()


        if location not in graph:
            print("Location not found.")
            continue


        connections = sorted(
            graph[location]
        )


        print(
            f"\nDirect connections of "
            f"{location}:"
        )


        if not connections:
            print("No direct connections.")
            continue


        for number, connection in enumerate(
            connections,
            start=1
        ):

            print(
                f"{number}. "
                f"{connection}"
            )


        print(
            f"\nTotal direct connections: "
            f"{len(connections)}"
        )


    # ========================================================
    # FIND ROUTE BETWEEN LOCATIONS
    # ========================================================

    elif choice == "8":

        print("\n=== Find Route ===")

        start = input(
            "Starting location: "
        ).strip().title()


        destination = input(
            "Destination: "
        ).strip().title()


        if start not in graph:
            print(
                f"Starting location "
                f"'{start}' does not exist."
            )
            continue


        if destination not in graph:
            print(
                f"Destination "
                f"'{destination}' does not exist."
            )
            continue


        if start == destination:
            print(
                f"Already at {destination}."
            )
            continue


        # ----------------------------------------------------
        # Queue for Breadth-First Search
        # ----------------------------------------------------

        queue = [
            [start]
        ]

        visited = {
            start
        }

        found_route = None


        while queue:

            current_route = queue.pop(0)

            current_location = current_route[-1]


            for neighbor in sorted(
                graph[current_location]
            ):

                if neighbor in visited:
                    continue


                new_route = (
                    current_route
                    + [neighbor]
                )


                if neighbor == destination:

                    found_route = new_route
                    queue = []
                    break


                visited.add(neighbor)

                queue.append(
                    new_route
                )


        if found_route is None:

            print(
                f"No route found from "
                f"{start} to {destination}."
            )

        else:

            print("\n=== Route Found ===")

            print(
                " -> ".join(found_route)
            )

            print(
                f"Number of connections: "
                f"{len(found_route) - 1}"
            )


    # ========================================================
    # MOST CONNECTED LOCATIONS
    # ========================================================

    elif choice == "9":

        if not graph:
            print("No locations available.")
            continue


        ranked_locations = sorted(
            graph.items(),
            key=lambda item: len(item[1]),
            reverse=True
        )


        print(
            "\n=== Most Connected Locations ==="
        )


        for rank, (location, connections) in enumerate(
            ranked_locations[:5],
            start=1
        ):

            print(
                f"{rank}. "
                f"{location} — "
                f"{len(connections)} connections"
            )


    # ========================================================
    # NETWORK STATISTICS
    # ========================================================

    elif choice == "10":

        if not graph:
            print("No locations available.")
            continue


        total_locations = len(graph)


        total_connection_entries = sum(
            len(connections)
            for connections in graph.values()
        )


        # Because every connection is stored twice:
        #
        # Kolkata -> Delhi
        # Delhi   -> Kolkata
        #
        # divide by 2 to get the actual number
        # of unique connections.

        unique_connections = (
            total_connection_entries
            // 2
        )


        most_connected_location = max(
            graph.items(),
            key=lambda item: len(item[1])
        )


        locations_without_connections = [
            location
            for location, connections in graph.items()
            if not connections
        ]


        average_connections = (
            total_connection_entries
            / total_locations
        )


        print("\n=== Network Statistics ===")


        print(
            f"Total locations: "
            f"{total_locations}"
        )


        print(
            f"Total unique connections: "
            f"{unique_connections}"
        )


        print(
            f"Average connections per location: "
            f"{average_connections:.2f}"
        )


        print(
            f"Most connected location: "
            f"{most_connected_location[0]} "
            f"({len(most_connected_location[1])} connections)"
        )


        print(
            f"Locations without connections: "
            f"{len(locations_without_connections)}"
        )


        if locations_without_connections:

            print("\nIsolated locations:")

            for location in sorted(
                locations_without_connections
            ):

                print(
                    f"- {location}"
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