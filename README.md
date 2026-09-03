# 🐍 Python Mini Projects

A structured, project-based journey through Python — starting from core programming concepts and progressively moving toward advanced Python, backend development, concurrency, and production-style systems.

This repository is not a collection of random coding exercises.

The goal is to **learn Python by building increasingly meaningful projects**, while continuously improving programming fundamentals, problem-solving ability, software design, and real-world development skills.

---

## 📊 Current Progress Overview

| Phase | Status | Completed / Total | Focus |
| :--- | :--- | :--- | :--- |
| **01 — Python Core** | ✅ Completed | 8 / 8 | Basic syntax, control flow, data structures |
| **02 — Data & Logic** | ✅ Completed | 9 / 9 | Algorithms, state, graph traversal, search |
| **03 — Functions & Design** | ⏳ In Progress | 1 / 9 | Modular code, separation of concerns |
| **04 — Files & Data Processing** | 📅 Upcoming | 0 / 10 | File I/O, JSON, CSV, data pipelines |
| **05 — OOP & Domain Modeling** | 📅 Upcoming | 0 / 9 | Classes, inheritance, domain models |
| **06 — Python Tooling** | 📅 Upcoming | 0 / 8 | Virtual envs, packaging, logging, CLI |
| **07 — Networking & APIs** | 📅 Upcoming | 0 / 10 | REST APIs, HTTP, web scraping |
| **08 — Databases & Persistence** | 📅 Upcoming | 0 / 9 | SQLite, SQL, ORM, data persistence |
| **09 — Testing & Quality** | 📅 Upcoming | 0 / 7 | pytest, unit testing, refactoring |
| **10 — Backend Development** | 📅 Upcoming | 0 / 11 | FastAPI, authentication, CRUD backend |
| **11 — Advanced Python** | 📅 Upcoming | 0 / 11 | Generators, decorators, context managers |
| **12 — Concurrency & Async** | 📅 Upcoming | 0 / 10 | asyncio, threading, multiprocessing |
| **13 — Production Engineering** | 📅 Upcoming | 0 / 10 | System architecture, Docker, background jobs |
| **14 — Capstone Projects** | 📅 Upcoming | 0 / TBD | Substantial original software |

**Total Projects Completed:** `18 / 110+`

---

## 🎯 Goal

The primary goal of this repository is to become genuinely proficient in Python through consistent hands-on development.

Instead of learning Python only through tutorials and isolated syntax exercises, this repository follows a progression where every stage introduces new concepts through practical projects.

The long-term goal is to reach a point where I can:

* Understand Python deeply rather than simply recognize its syntax
* Solve programming problems independently
* Design and structure Python applications
* Work confidently with files, data, APIs, and databases
* Write maintainable and testable code
* Build backend applications and services
* Understand advanced Python concepts
* Work with asynchronous and concurrent Python
* Design production-style systems
* Approach complex Python projects independently
* Use AI as a development accelerator and learning tool rather than as a replacement for understanding

---

# 🧠 Learning Philosophy

The repository follows a simple principle:

> **Learn → Build → Break → Debug → Improve → Understand → Repeat**

Projects are deliberately chosen so that they are:

* More meaningful than basic syntax exercises
* Small enough to understand completely
* Large enough to introduce real programming problems
* Connected to concepts learned previously
* Progressively more challenging
* Useful preparation for larger projects

I am intentionally avoiding a progression filled with extremely basic projects such as simple calculators or isolated syntax demonstrations.

Instead, foundational concepts are introduced **inside useful programs**.

---

# 🏗️ Repository Structure

```text
python-mini-projects/
│
├── README.md
├── pyproject.toml
├── .gitignore
│
├── 01-python-core/
├── 02-data-and-logic/
├── 03-functions-and-design/
├── 04-files-and-data-processing/
├── 05-oop-and-domain-modeling/
├── 06-python-tooling/
├── 07-networking-and-apis/
├── 08-databases-and-persistence/
├── 09-testing-and-code-quality/
├── 10-backend-development/
├── 11-advanced-python/
├── 12-concurrency-and-async/
├── 13-production-engineering/
├── 14-capstone-projects/
│
├── _experiments/
└── _notes/
```

Each numbered directory represents a stage of the learning journey.

The progression is intentional: later stages depend on concepts and skills developed earlier.

---

# ⚡ Quick Start / How to Run

To run any of the completed projects:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Anurag8500/Python-mini-projects.git
   cd Python-mini-projects
   ```

2. **Run a project directly with Python (3.11+):**
   ```bash
   python 01-python-core/01-personal-finance-analyzer/main.py
   ```
   or
   ```bash
   python 02-data-and-logic/17-mini-library-management-system/main.py
   ```
   or
   ```bash
   python 03-functions-and-design/18-modular-expense-tracker/main.py
   ```

---

# 🗺️ Curriculum Roadmap

## 01 — Python Core (Completed ✅)

**Goal:** Build strong Python fundamentals through useful programs.

Topics include:
* Variables and data types, Strings, User input, Type conversion
* Conditions, Loops, Lists, Tuples, Dictionaries, Sets
* Built-in functions, String and collection methods, Formatted output

### Projects

* [x] [01 — Personal Finance Analyzer](01-python-core/01-personal-finance-analyzer) — Income/expense logging, summary statistics, savings rate calculation
* [x] [02 — Student Performance Analyzer](01-python-core/02-student-performance-analyzer) — Grade tracking, subject averages, GPA calculation, pass/fail status
* [x] [03 — Inventory & Billing System](01-python-core/03-inventory-and-billing-system) — Product catalog, stock updates, shopping cart, automated receipt generation
* [x] [04 — CLI Quiz Engine](01-python-core/04-cli-quiz-engine) — Multiple choice questions, immediate feedback, scoring system, detailed summary
* [x] [05 — Bank Account Simulator](01-python-core/05-bank-account-simulator) — Account creation, deposits/withdrawals, balance checks, transaction history log
* [x] [06 — Text Analyzer](01-python-core/06-text-analyzer) — Word/character count, frequency analysis, reading time estimation, basic sentiment checks
* [x] [07 — Mini Task Manager](01-python-core/07-mini-task-manager) — Task creation, priority tagging, completion tracking, list filtering
* [x] [08 — Terminal Productivity Suite](01-python-core/08-terminal-productivity-suite) **(Milestone 01)** — Integrated suite combining tasks, notes, habits, and time management

### Milestone 01

🎉 **[08 — Terminal Productivity Suite](01-python-core/08-terminal-productivity-suite)** (Completed)

---

## 02 — Data and Logic (Completed ✅)

**Goal:** Improve problem-solving ability and learn how to represent and manipulate structured information.

Topics include:
* Advanced list/dictionary usage, Searching, Filtering, Sorting, Aggregation
* Nested data, Data modeling, Basic algorithms, Graph concepts (BFS / DFS), State management

### Projects

* [x] [09 — Contact Management System](02-data-and-logic/09-contact-management-system) — Phonebook lookup, multi-field search, tag filtering, contact exporting
* [x] [10 — Inventory Analytics Engine](02-data-and-logic/10-inventory-analytics-engine) — Low-stock alerts, category aggregation, price re-indexing, profit estimation
* [x] [11 — Expense Categorization Engine](02-data-and-logic/11-expense-categorization-engine) — Rule-based categorization, spending breakdown by tag/month, budget threshold warnings
* [x] [12 — Document Analyzer](02-data-and-logic/12-document-analyzer) — Keyword indexing, word cloud simulation, readability score, stop-word filtering
* [x] [13 — Student Records & Ranking System](02-data-and-logic/13-student-records-ranking-system) — Multi-attribute sorting, grade percentile rank, top performers filter, report generation
* [x] [14 — Event Registration Manager](02-data-and-logic/14-event-registration-manager) — Capacity tracking, waitlist queue handling, duplicate registration prevention, attendee search
* [x] [15 — Graph / Route Explorer](02-data-and-logic/15-graph-route-explorer) — City network graph modeling, shortest path discovery, connection validation, BFS/DFS traversal
* [x] [16 — Search & Filtering Engine](02-data-and-logic/16-search-filtering-engine) — Multi-criteria search, fuzzy string matching, pagination, dynamic query filtering
* [x] [17 — Mini Library Management System](02-data-and-logic/17-mini-library-management-system) **(Milestone 02)** — Complete book checkout/return engine, borrower records, fine calculation, availability indexing

### Milestone 02

🎉 **[17 — Mini Library Management System](02-data-and-logic/17-mini-library-management-system)** (Completed)

---

## 03 — Functions and Program Design (In Progress ⏳)

**Goal:** Move from writing scripts to designing reusable programs.

Topics include:
* Functions, Parameters, Return values, Scope, Reusability
* Modules, Separation of concerns, Program decomposition, Basic architecture, Command routing

### Projects

* [x] [18 — Modular Expense Tracker](03-functions-and-design/18-modular-expense-tracker) — Modular CLI expense tracker built with clean function decomposition and decoupled helper modules
* [ ] 19 — Validation Toolkit
* [ ] 20 — Text Processing Toolkit
* [ ] 21 — File Utility Toolkit
* [ ] 22 — CLI Command Router
* [ ] 23 — Configuration Manager
* [ ] 24 — Reporting Engine
* [ ] 25 — Refactor an Earlier Project
* [ ] 26 — Personal Productivity CLI **(Milestone 03)**

### Milestone 03

🎯 **Personal Productivity CLI** (Upcoming)

---

## 04 — Files and Data Processing

**Goal:** Make applications work with persistent and real-world data.

Topics include: File I/O, `pathlib`, JSON, CSV, Serialization, Data cleaning, Logging, Data pipelines.

### Projects

* [ ] CSV Data Analyzer
* [ ] JSON Data Management System
* [ ] Log File Analyzer
* [ ] Directory Organizer
* [ ] Duplicate File Detector
* [ ] Automatic Backup Tool
* [ ] File Metadata Analyzer
* [ ] Dataset Cleaning Pipeline
* [ ] CSV / JSON / Database Converter
* [ ] Local Data Processing Pipeline **(Milestone 04)**

---

## 05 — Object-Oriented Python

**Goal:** Learn how to model real-world systems using objects and interacting components.

Topics include: Classes, Objects, Encapsulation, Properties, Inheritance, Composition, Polymorphism, Dataclasses, Domain modeling.

### Projects

* [ ] Banking Domain Model
* [ ] Library Domain Model
* [ ] E-Commerce Cart System
* [ ] Parking Lot System
* [ ] Hotel Booking System
* [ ] Inventory Management System
* [ ] RPG / Game Domain Engine
* [ ] Workflow / State Machine Engine
* [ ] Business Management System **(Milestone 05)**

---

## 06 — Python Tooling

**Goal:** Start developing Python projects using professional development practices.

Topics include: Virtual environments, `pyproject.toml`, Type hints, Logging, Configuration, Environment variables, Packaging.

### Projects

* [ ] Reusable Python Utility Package
* [ ] Advanced CLI Tool
* [ ] Environment Configuration System
* [ ] Structured Logging Utility
* [ ] Python Project Generator
* [ ] Custom Command-Line Application
* [ ] Publishable Python Package
* [ ] Own Python CLI Toolkit **(Milestone 06)**

---

## 07 — Networking and APIs

**Goal:** Learn how Python communicates with external systems.

Topics include: HTTP, Requests, REST APIs, JSON APIs, Authentication, Query parameters, Rate limiting, Web scraping fundamentals.

### Projects

* [ ] HTTP Client
* [ ] REST API Client
* [ ] GitHub Data Analyzer
* [ ] Weather / Data Aggregator
* [ ] Multi-API Aggregator
* [ ] Authenticated API Client
* [ ] Pagination & Rate-Limited Client
* [ ] Website Metadata Collector
* [ ] Web Data Extraction Pipeline
* [ ] Personal Research Aggregator **(Milestone 07)**

---

## 08 — Databases and Persistence

**Goal:** Move from file-based storage to proper data persistence.

Topics include: SQLite, SQL, Tables, Relationships, CRUD, Indexes, Transactions, ORM concepts, Repository patterns.

### Projects

* [ ] SQLite Contact Database
* [ ] Expense Database
* [ ] Inventory Database
* [ ] Library Database
* [ ] Student Management Database
* [ ] Database Analytics Tool
* [ ] Data Migration / Import Tool
* [ ] Repository Pattern Project
* [ ] Database-Backed Task Management System **(Milestone 08)**

---

## 09 — Testing and Code Quality

**Goal:** Learn how to write Python that is reliable, maintainable, and easier to change.

Topics include: Testing principles, `pytest`, Unit tests, Integration tests, Fixtures, Mocking, Debugging, Refactoring.

### Projects

* [ ] Test the Expense System
* [ ] Test the Task Manager
* [ ] Validation Library with Tests
* [ ] Refactor an Earlier Project
* [ ] Configuration Library with Tests
* [ ] Unit + Integration Tested Service
* [ ] Production-Quality CLI Application **(Milestone 09)**

---

## 10 — Backend Development

**Goal:** Learn how to build real Python backend services.

Topics include: HTTP APIs, FastAPI, Routing, Validation, CRUD, Authentication, Authorization, Database integration, Service layers.

### Projects

* [ ] Basic REST API
* [ ] CRUD API
* [ ] Database-Backed API
* [ ] Authentication API
* [ ] User Management API
* [ ] File Upload API
* [ ] Pagination / Filtering API
* [ ] API Validation Layer
* [ ] API Testing
* [ ] Background Task API
* [ ] Full Task Management Backend **(Milestone 10)**

---

## 11 — Advanced Python

**Goal:** Understand powerful Python language features beyond everyday syntax.

Topics include: Iterators, Generators, Decorators, Context managers, Custom exceptions, Advanced typing, Protocols, Dynamic behavior.

### Projects

* [ ] Iterator Toolkit
* [ ] Generator-Based File Processor
* [ ] Decorator Framework
* [ ] Caching Decorator
* [ ] Retry / Backoff Decorator
* [ ] Context Manager Library
* [ ] Lazy Data Processing System
* [ ] Event Dispatcher
* [ ] Typed Data Transformation Library
* [ ] Plugin Architecture
* [ ] Mini Python Framework **(Milestone 11)**

---

## 12 — Concurrency and Async

**Goal:** Understand how Python handles multiple tasks and I/O-heavy workloads.

Topics include: Threads, Processes, `concurrent.futures`, `asyncio`, Coroutines, Queues, Synchronization.

### Projects

* [ ] Threaded File Processor
* [ ] Concurrent URL Checker
* [ ] Parallel File Hasher
* [ ] Concurrent Downloader
* [ ] Async HTTP Client
* [ ] Async Web Scraper
* [ ] Async Data Collector
* [ ] Producer / Consumer Queue
* [ ] Background Worker System
* [ ] Concurrent Data Processing Pipeline **(Milestone 12)**

---

## 13 — Production Engineering

**Goal:** Bring together the skills needed to build more realistic software systems.

Topics include: Application architecture, Background jobs, Logging, Monitoring, Docker, Reliability, Service boundaries.

### Projects

* [ ] Job Scheduler
* [ ] Background Job Queue
* [ ] File Synchronization Service
* [ ] Monitoring / Health Check Service
* [ ] Log Aggregation System
* [ ] Local Search Engine
* [ ] Document Processing Service
* [ ] Data Synchronization Service
* [ ] Service-to-Service API System
* [ ] Production-Style Backend **(Milestone 13)**

---

## 14 — Capstone Projects

**Goal:** Combine knowledge from multiple previous stages to build substantial original software.

Possible directions: AI-powered applications, Automation systems, Data engineering systems, Developer tools, Real-time applications, Distributed systems.

---

# 📈 Difficulty Progression

```text
Useful Programs
      ↓
Mini Applications
      ↓
Multi-Component Applications
      ↓
Data Processing Systems
      ↓
Object-Oriented Systems
      ↓
Reusable Packages & CLI Tools
      ↓
API Clients
      ↓
Database Applications
      ↓
Tested Applications
      ↓
Backend Services
      ↓
Advanced Python Systems
      ↓
Concurrent / Async Systems
      ↓
Production-Style Applications
      ↓
Advanced Capstone Projects
```

---

# 🧩 Project Design Rules

### 1. No random projects
Every project must teach something relevant to the next stage.

### 2. No unnecessary complexity
A project should only introduce concepts that make sense at that point in the curriculum.

### 3. Existing concepts should be reused
New projects should reinforce earlier knowledge instead of completely replacing it.

### 4. Projects should grow in complexity
Early projects use a single file; later projects evolve into modules, packages, tests, databases, APIs, and production architectures.

### 5. AI is a tool, not the learner
AI is used for explanations, debugging, review, and feedback — but not to replace core understanding.

### 6. Understand before moving forward
A smaller project that is fully understood is far more valuable than a larger project that was blindly generated.

---

# 🔄 Project Workflow

```text
Learn → Plan → Attempt → Get stuck → Research / Ask → Implement → Test → Debug → Extend → Refactor → Document → Commit
```

---

# 🧪 Experiments & 📝 Notes

- **`_experiments/`**: Temporary playground to experiment with syntax, decorators, generators, asyncio, regex, etc.
- **`_notes/`**: Personal cheat-sheets and core reference material ([Notes.md](_notes/Notes.md)).

---

## 🏆 Completed Projects Catalog (18 Completed)

| # | Project Name | Phase | Directory Link |
| :--- | :--- | :--- | :--- |
| 01 | Personal Finance Analyzer | 01 — Core | [`01-personal-finance-analyzer`](01-python-core/01-personal-finance-analyzer) |
| 02 | Student Performance Analyzer | 01 — Core | [`02-student-performance-analyzer`](01-python-core/02-student-performance-analyzer) |
| 03 | Inventory & Billing System | 01 — Core | [`03-inventory-and-billing-system`](01-python-core/03-inventory-and-billing-system) |
| 04 | CLI Quiz Engine | 01 — Core | [`04-cli-quiz-engine`](01-python-core/04-cli-quiz-engine) |
| 05 | Bank Account Simulator | 01 — Core | [`05-bank-account-simulator`](01-python-core/05-bank-account-simulator) |
| 06 | Text Analyzer | 01 — Core | [`06-text-analyzer`](01-python-core/06-text-analyzer) |
| 07 | Mini Task Manager | 01 — Core | [`07-mini-task-manager`](01-python-core/07-mini-task-manager) |
| 08 | Terminal Productivity Suite (Milestone 01) | 01 — Core | [`08-terminal-productivity-suite`](01-python-core/08-terminal-productivity-suite) |
| 09 | Contact Management System | 02 — Data & Logic | [`09-contact-management-system`](02-data-and-logic/09-contact-management-system) |
| 10 | Inventory Analytics Engine | 02 — Data & Logic | [`10-inventory-analytics-engine`](02-data-and-logic/10-inventory-analytics-engine) |
| 11 | Expense Categorization Engine | 02 — Data & Logic | [`11-expense-categorization-engine`](02-data-and-logic/11-expense-categorization-engine) |
| 12 | Document Analyzer | 02 — Data & Logic | [`12-document-analyzer`](02-data-and-logic/12-document-analyzer) |
| 13 | Student Records & Ranking System | 02 — Data & Logic | [`13-student-records-ranking-system`](02-data-and-logic/13-student-records-ranking-system) |
| 14 | Event Registration Manager | 02 — Data & Logic | [`14-event-registration-manager`](02-data-and-logic/14-event-registration-manager) |
| 15 | Graph / Route Explorer | 02 — Data & Logic | [`15-graph-route-explorer`](02-data-and-logic/15-graph-route-explorer) |
| 16 | Search & Filtering Engine | 02 — Data & Logic | [`16-search-filtering-engine`](02-data-and-logic/16-search-filtering-engine) |
| 17 | Mini Library Management System (Milestone 02) | 02 — Data & Logic | [`17-mini-library-management-system`](02-data-and-logic/17-mini-library-management-system) |
| 18 | Modular Expense Tracker | 03 — Functions & Design | [`18-modular-expense-tracker`](03-functions-and-design/18-modular-expense-tracker) |

---

## 🎯 What Success Looks Like

Success is reaching the point where I can receive a new Python project idea and independently:

1. Understand the problem
2. Break it into smaller components
3. Decide which Python concepts and tools are needed
4. Design the data structures
5. Build the solution
6. Debug problems
7. Test the important behavior
8. Refactor the code
9. Learn unfamiliar technologies when necessary
10. Use AI to accelerate development without losing understanding

---

# 🚀 Final Objective

```text
Python Beginner
      ↓
Python Programmer
      ↓
Application Developer
      ↓
Backend Developer
      ↓
Advanced Python Developer
      ↓
Software Engineer
```
