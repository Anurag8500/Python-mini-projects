# Project #15: Graph / Route Explorer

A Python-based terminal application that represents a network of connected locations and allows users to explore relationships, search locations, manage connections, and find routes between locations.

This project introduces the fundamentals of **graph data structures and Breadth-First Search (BFS)** while continuing to reinforce dictionaries, lists, filtering, sorting, aggregation, and interactive menu-driven programming.

## Features

* View all locations
* View connections between locations
* Add new locations
* Add connections between locations
* Remove existing connections
* Search locations
* View direct connections for a location
* Find a route between two locations
* Identify the most connected locations
* Calculate network statistics
* Detect isolated locations
* Rank locations by number of connections

## Concepts Practiced

### Data Structures

* Dictionaries
* Lists
* Sets
* Dictionary values
* Dictionary items
* Nested collections
* Graph representation using an adjacency list

### Control Flow

* `while` loops
* `for` loops
* Nested loops
* `if / elif / else`
* `break`
* `continue`

### Data Processing

* `len()`
* `sum()`
* `max()`
* `sorted()`
* `enumerate()`
* List comprehensions
* List slicing
* Dictionary operations
* Aggregation

### Algorithms

* Graph traversal
* Breadth-First Search (BFS)
* Visited-node tracking
* Queue-based exploration
* Route reconstruction
* Degree / connection counting

## What Is a Graph?

A graph is a data structure used to represent relationships between objects.

In this project:

```text
Locations = Nodes
Connections = Edges
```

For example:

```text
Kolkata ─── Delhi
   │          │
   │          │
Guwahati    Jaipur
```

Each city is a **node**, while a connection between two cities is an **edge**.

## Graph Representation

The application represents the graph using a dictionary containing lists of neighboring locations.

Example:

```python id="q4ml1w"
graph = {
    "Kolkata": ["Delhi", "Guwahati", "Mumbai"],
    "Delhi": ["Kolkata", "Jaipur", "Mumbai"],
    "Guwahati": ["Kolkata"],
    "Mumbai": ["Kolkata", "Delhi", "Chennai"],
    "Jaipur": ["Delhi"],
    "Chennai": ["Mumbai"]
}
```

This representation is commonly called an **adjacency list**.

The key represents a location, and its list contains locations directly connected to it.

For example:

```python id="u9xj6a"
graph["Kolkata"]
```

produces:

```python id="t2v3mu"
["Delhi", "Guwahati", "Mumbai"]
```

meaning Kolkata has direct connections to those three locations.

## Undirected Connections

The graph models connections as two-way relationships.

For example:

```text
Kolkata ↔ Delhi
```

is stored as:

```python id="8h5w6t"
graph["Kolkata"].append("Delhi")
graph["Delhi"].append("Kolkata")
```

Both directions are required because traveling from Kolkata to Delhi also means Delhi is connected back to Kolkata.

The same principle is followed when removing connections.

## Main Menu

```text id="n4vo8k"
=== Menu ===
1. View all locations
2. View connections
3. Add location
4. Add connection
5. Remove connection
6. Search location
7. Find direct connections
8. Find route between locations
9. Most connected locations
10. Network statistics
11. Exit
```

## Viewing Locations

The program displays every location stored in the graph.

Locations are sorted alphabetically before display:

```python id="fdrn0y"
for location in sorted(graph):
    print(location)
```

`sorted()` is used here to make the output predictable and easier to read.

## Managing Locations

New locations can be added dynamically.

For example:

```text id="mcrf51"
Location name: Pune

Location 'Pune' added successfully.
```

A newly created location starts with no connections:

```python id="ahzhwd"
graph["Pune"] = []
```

Connections can then be added separately.

## Managing Connections

Users can create a connection between two existing locations.

The program validates that:

* Both locations exist
* A location is not connected to itself
* The connection does not already exist

For an undirected graph, the connection is stored in both directions.

Example:

```text id="b7zd3d"
First location: Pune
Second location: Mumbai

Connection added between Pune and Mumbai.
```

## Searching Locations

The search feature allows partial, case-insensitive matching.

For example:

```text id="b18qg0"
Search location: mum
```

can match:

```text
Mumbai
```

The search result also displays the number of direct connections for each matching location.

## Direct Connections

A user can select a location and view its immediate neighbors.

For example:

```text id="50asbi"
=== Direct Connections ===

Direct connections of Kolkata:

1. Delhi
2. Guwahati
3. Mumbai

Total direct connections: 3
```

This is useful for understanding the local structure of the graph.

## Route Finding with BFS

The most important algorithm introduced in this project is **Breadth-First Search (BFS)**.

BFS explores a graph level by level.

Suppose the graph contains:

```text id="qdc6b4"
Kolkata
   ↓
Delhi
   ↓
Jaipur
```

To find a route from Kolkata to Jaipur, BFS explores:

```text id="g2d1gs"
Kolkata
   ↓
Delhi
   ↓
Jaipur
```

The resulting route is:

```text id="1lbyei"
Kolkata -> Delhi -> Jaipur
```

## Queue-Based Exploration

The route-search algorithm maintains a queue:

```python id="4x0x1v"
queue = [[start]]
```

Each queue entry represents a possible route.

The first route is removed using:

```python id="v0n08r"
current_route = queue.pop(0)
```

This ensures routes are explored in the order they were discovered.

That is the fundamental idea behind BFS.

## Visited Locations

Graphs can contain cycles.

For example:

```text id="7zr76k"
Kolkata → Delhi → Mumbai → Kolkata
```

Without tracking visited locations, the algorithm could repeatedly explore the same locations.

The program therefore maintains:

```python id="7i8e7p"
visited = {start}
```

When a location has already been visited:

```python id="kflb8f"
if neighbor in visited:
    continue
```

the algorithm skips it.

This prevents unnecessary repeated traversal and infinite cycling.

## Building a Route

When a new location is discovered, the existing route is extended:

```python id="z0lqvh"
new_route = current_route + [neighbor]
```

For example:

```python id="zq2o1f"
current_route = ["Kolkata", "Delhi"]
neighbor = "Jaipur"
```

produces:

```python id="w8hf45"
["Kolkata", "Delhi", "Jaipur"]
```

This allows the complete route to be reconstructed when the destination is reached.

## Example Route Search

```text id="s9z5d1"
=== Find Route ===

Starting location: Kolkata
Destination: Jaipur

=== Route Found ===

Kolkata -> Delhi -> Jaipur

Number of connections: 2
```

The number of connections is calculated as:

```python id="xqz1gi"
len(found_route) - 1
```

There are three locations but only two connections between them.

## Why `sorted()` Is Used

The project uses `sorted()` in several places.

Its purpose is generally to make output and traversal order **consistent and predictable**.

For example:

```python id="ee8bzs"
sorted(graph)
```

displays locations alphabetically.

Similarly:

```python id="e25ohh"
sorted(graph[current_location])
```

processes neighboring locations in alphabetical order during BFS.

`sorted()` is not required for the graph itself to function.

In the BFS algorithm, sorting ensures that when multiple equally valid routes exist, the algorithm explores neighbors in a consistent order.

Conceptually:

```text
sorted()
    ↓
predictable order
    ↓
consistent output / traversal
```

## Most Connected Locations

The program ranks locations according to the number of direct connections they have.

For example:

```text id="3id9yp"
=== Most Connected Locations ===

1. Kolkata — 3 connections
2. Delhi — 3 connections
3. Mumbai — 3 connections
```

This uses the number of neighbors as a simple measure of how connected a location is.

## Network Statistics

The program calculates:

* Total locations
* Total unique connections
* Average connections per location
* Most connected location
* Number of isolated locations

Example:

```text id="yq06xj"
=== Network Statistics ===

Total locations: 6
Total unique connections: 7
Average connections per location: 2.33
Most connected location: Kolkata (3 connections)
Locations without connections: 0
```

## Counting Unique Connections

Because each undirected connection is stored twice:

```text id="vv27vb"
Kolkata → Delhi
Delhi → Kolkata
```

the total number of stored connection entries is twice the number of actual connections.

Therefore:

```python id="tdf4as"
unique_connections = total_connection_entries // 2
```

converts the number of stored directional entries into the number of unique undirected connections.

## Isolated Locations

An isolated location is a location with no connections.

For example:

```python id="xiz70m"
"Pune": []
```

means Pune exists in the network but is not connected to anything.

The program identifies these locations and displays them separately.

## Project Structure

```text id="h8j9ml"
15-graph-route-explorer/
│
├── main.py
└── README.md
```

The application intentionally remains a single-file program at this stage of the roadmap.

Functions and modular design will be introduced in the next phase.

## How to Run

From the project directory:

```bash id="yq4zlu"
python main.py
```

Make sure your Python virtual environment is activated before running the program.

## Example Workflow

```text id="0bq8gx"
View the network
      ↓
Search for a location
      ↓
Inspect direct connections
      ↓
Add or remove connections
      ↓
Find a route between locations
      ↓
Analyze network connectivity
```

## Learning Progression

Project #15 represents a major shift in the type of problems being solved:

```text id="j2p9uc"
Project #09
CRUD + searching
        ↓
Project #10
Aggregation + ranking
        ↓
Project #11
Grouping + statistics
        ↓
Project #13
Nested records
        ↓
Project #14
Relationships between records
        ↓
Project #15
Graph representation + traversal algorithms
```

Instead of treating data as independent records, the program now works with **relationships and paths between entities**.

## What This Project Teaches

The central idea is that many real-world systems can be represented as graphs.

Examples include:

```text
Cities       → Road networks
People       → Social networks
Web pages    → Links
Computers    → Network topology
Dependencies → Software packages
```

The project demonstrates how a simple dictionary and list structure can represent such relationships and how BFS can be used to explore them.

## Future Improvements

Possible extensions include:

* Weighted connections
* Distance or travel-time between locations
* Shortest-path calculations
* Depth-First Search (DFS)
* Multiple route suggestions
* Route cost calculation
* Importing graphs from files
* Visual graph representation
* Saving graph data between program runs

These improvements are intentionally reserved for later stages of the roadmap.

## Development Philosophy

This repository follows:

```text
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

The goal is to understand the data structures and algorithms behind each project rather than simply producing working output.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.
