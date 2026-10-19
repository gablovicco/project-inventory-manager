# Decision Log

This document records important product, process and technical decisions made during the project.

The purpose of the log is to preserve the reasoning behind important choices, including alternatives considered and the consequences of each decision.

---

## D-001 — Choose a Simple Inventory Management System as the Project

**Status:** Accepted

### Decision

The semester project will be a Simple Inventory Management System.

### Reason

The project was selected because it is complex enough to demonstrate the main course requirements, including a database, REST API, business rules, automated testing, CI and iterative development, while still remaining manageable for a single student.

The domain is also easy to understand and does not require complicated external integrations, payments, authentication or other features that would add unnecessary complexity.

This makes it possible to focus not only on building the product, but also on understanding and documenting the development process.

### Consequences

The project will focus on core inventory operations such as product management, stock changes, low-stock identification and stock movement history.

More advanced features such as supplier management, invoicing, barcode scanning and multiple warehouses are not part of the initial scope.

---

## D-002 — Keep the Initial Product Scope Intentionally Small

**Status:** Accepted

### Decision

Only the core inventory-management workflow will be included in the initial project scope.

Optional features will only be considered after the core product and required course evidence are complete.

### Reason

The project is being developed individually and also requires learning and applying Git/GitHub workflow, REST API development, automated testing, CI and an iterative software-development process.

Keeping the scope limited reduces the risk of an incomplete project and leaves enough time for testing, documentation and process evidence.

### Consequences

Authentication, supplier management, barcode scanning, sales, invoicing, multiple warehouses and similar advanced features are currently out of scope.

The backlog may later contain lower-priority improvements, but they must not endanger completion of the core product.

---

## D-003 — Develop the Project Individually

**Status:** Accepted

### Decision

The project will be developed as an individual project with the instructor's approval.

### Reason

The original course structure is designed for small student teams. However, I decided to work individually because I believe this will allow me to use my effort more effectively for learning and development.

Working in a group where several members may also be using GitHub and collaborative development practices for the first time could require a significant amount of effort for coordination, task management and resolving workflow issues.

By working individually, I can focus more directly on my own strengths and weaknesses, understand every part of the project, and spend more time improving my knowledge of Git/GitHub, REST APIs, testing, CI and software-development methodology.

I also expect this to make it easier to understand the reasons behind each technical and process decision, which is important for the final project defense.

### Consequences

All implementation, documentation and process evidence will be produced and maintained by one developer.

Team-oriented course practices will be adapted where necessary for individual work, for example by using a Solo Working Agreement, individual retrospectives and self-review instead of artificial team activity.

No fake peer-review or artificial team contribution evidence will be created.

---

## D-004 — Use Python as the Main Programming Language

**Status:** Accepted

### Decision

Python will be used as the main programming language for the project.

### Reason

The project requires a REST API, database access, automated testing and a desktop interface.

Python allows these parts to be implemented with relatively little setup and boilerplate, which is important for a project developed by one person.

The developer already has programming experience, mainly in C++, so the main challenge is learning Python syntax and libraries rather than learning programming concepts from the beginning.

Using Python also allows more development effort to be spent on the course objectives such as Git workflow, testing, CI, REST APIs and iterative development.

### Consequences

Python syntax and project-specific libraries will need to be learned during development.

The implementation should remain simple and avoid unnecessary language features or abstractions.

---

## D-005 — Use FastAPI for the REST API

**Status:** Accepted

### Decision

FastAPI will be used to implement the REST API.

### Reason

The project requires REST/API usage, and FastAPI provides a relatively simple way to define HTTP endpoints in Python.

It also supports request validation and automated API documentation, which should make the API easier to develop, test and understand.

### Consequences

The desktop application will not access the database directly.

Inventory operations will be performed through REST endpoints provided by the FastAPI backend.

---

## D-006 — Use PySide6 for the Desktop Interface

**Status:** Accepted

### Decision

PySide6 will be used to implement the desktop user interface.

### Reason

The project only requires a small desktop interface and does not need the additional complexity of a web frontend.

PySide6 provides the Qt GUI framework for Python and is sufficient for forms, buttons, product lists and other interface components required by the application.

### Consequences

The desktop client will communicate with the backend through HTTP requests instead of accessing the database directly.

---

## D-007 — Use SQLite for Persistent Storage

**Status:** Accepted

### Decision

SQLite will be used as the project database.

### Reason

The application is a small single-user inventory system and does not require a separate database server.

SQLite provides persistent relational storage while keeping installation and configuration simple.

It is sufficient for storing products and stock movements required by the current project scope.

### Consequences

The database will be stored locally.

The current architecture is not intended for multiple simultaneous users or distributed deployment.---

## D-004 — Use Python as the Main Programming Language

**Status:** Accepted

### Decision

Python will be used as the main programming language for the project.

### Reason

The project requires a REST API, database access, automated testing and a desktop interface.

Python allows these parts to be implemented with relatively little setup and boilerplate, which is important for a project developed by one person.

Using Python also allows more development effort to be spent on the course objectives such as Git workflow, testing, CI, REST APIs and iterative development.

### Consequences

The implementation should remain simple and avoid unnecessary language features or abstractions.

---

## D-005 — Use FastAPI for the REST API

**Status:** Accepted

### Decision

FastAPI will be used to implement the REST API.

### Reason

The project requires REST/API usage, and FastAPI provides a relatively simple way to define HTTP endpoints in Python.

It also supports request validation and automated API documentation, which should make the API easier to develop, test and understand.

### Consequences

The desktop application will not access the database directly.

Inventory operations will be performed through REST endpoints provided by the FastAPI backend.

---

## D-006 — Use PySide6 for the Desktop Interface

**Status:** Accepted

### Decision

PySide6 will be used to implement the desktop user interface.

### Reason

The project only requires a small desktop interface and does not need the additional complexity of a web frontend.

PySide6 provides the Qt GUI framework for Python and is sufficient for forms, buttons, product lists and other interface components required by the application.

### Consequences

The desktop client will communicate with the backend through HTTP requests instead of accessing the database directly.

---
---

## D-007 — Use SQLite for Local Persistent Storage

**Status:** Accepted

### Decision

SQLite will be used as the persistent database for the initial version of the Inventory Management System.

The database will be stored locally and accessed only by the FastAPI backend.

### Reason

The current product scope is a small inventory system designed for a single inventory operator and a single inventory location.

The project does not require a separate database server, multiple simultaneous users or distributed deployment.

SQLite provides the relational persistence required by the project while keeping setup, development and testing simple.

Using a server-based database such as PostgreSQL would introduce additional infrastructure work, including database server setup, connection configuration and environment management, without solving a requirement in the current product scope.

Keeping the database local also makes the application easier to reproduce and run during development and demonstration.

### Consequences

- Product and stock movement data will be stored in a local SQLite database.
- The PySide6 desktop client will not access the database directly.
- All database access will go through the FastAPI backend.
- The initial architecture is intended primarily for a local, single-user environment.
- If the product later requires multiple simultaneous users, centralized remote access or distributed deployment, the database choice may need to be reconsidered.
