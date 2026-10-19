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
