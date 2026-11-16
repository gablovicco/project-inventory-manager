# Inventory Manager — Living Report

## 1. Project Overview

Inventory Manager is a solo semester project developed for the Software Development Methodologies course.

The project aims to provide a simple inventory management system for a small business or inventory operator. The system will support product management, stock increases and decreases, stock movement tracking, and low-stock identification.

The project scope is intentionally kept small so that the complete development process, architecture, implementation, testing, and project decisions remain understandable and explainable.

---

## 2. Product Goal

The goal of the project is to create a simple inventory management application that allows an inventory operator to:

- add and view products;
- track current stock quantities;
- record stock increases;
- record stock decreases safely;
- prevent stock from becoming negative;
- record stock movements;
- identify products below their minimum stock level.

Authentication, multiple user roles, suppliers, orders, invoices, barcode scanning, multiple warehouses, payments, advanced analytics, and cloud deployment are outside the initial project scope.

For the detailed product definition, see:

[Project Definition](project-definition.md)

---

## 3. Current Architecture

The current architecture consists of three main parts:

```text
Browser-based Frontend
        ↓
     HTTP / REST
        ↓
   FastAPI Backend
        ↓
   SQLite Database
```

The browser-based frontend will use:

- HTML;
- basic CSS;
- vanilla JavaScript.

The FastAPI backend is responsible for:

- REST endpoints;
- input validation;
- business rules;
- database operations.

The frontend does not access the SQLite database directly.

Business rules such as preventing negative stock are handled by the backend.

For the detailed architecture, see:

[Architecture](architecture.md)

---

## 4. Development Method

The project uses **Scrum with selected XP practices**, adapted for individual development.

Scrum practices used in the project include:

- prioritized product backlog;
- sprint goals;
- sprint planning;
- incremental implementation;
- review;
- retrospective;
- backlog updates based on progress and feedback.

Selected XP practices include:

- automated testing;
- continuous integration;
- small incremental changes;
- frequent commits;
- simple design;
- refactoring when necessary.

Because the project is developed individually, planning, review, and retrospective activities are performed by the developer. Team roles or peer-review activities are not simulated.

For the detailed method rationale, see:

[Method Choice](method-choice.md)

---

## 5. Development Workflow

Development work follows a simple Git and GitHub workflow:

```text
Backlog / Issue
      ↓
Ready
      ↓
In Progress
      ↓
Development Branch
      ↓
Commit
      ↓
Pull Request
      ↓
CI and Review
      ↓
Merge to main
      ↓
Done
```

The `main` branch is kept stable.

Implementation work is normally performed on a separate branch and merged through a Pull Request.

Important project and technical decisions are recorded together with their reasons and consequences.

For the working rules and Definition of Done, see:

[Working Agreement and Definition of Done](working-agreement-and-dod.md)

For recorded project decisions, see:

[Decision Log](decision-backlog.md)

---

# Sprint 0

## 6. Sprint 0 Goal

The goal of Sprint 0 was to establish a clear product, process, and technical foundation before starting the three implementation sprints.

Sprint 0 focused on:

- defining the project;
- defining and prioritizing requirements;
- establishing quality expectations;
- selecting the development method;
- defining the architecture;
- establishing the Git and GitHub workflow;
- preparing the development environment;
- verifying testing and continuous integration.

Core inventory functionality was intentionally not implemented during Sprint 0.

---

## 7. Sprint 0 Product and Requirements Evidence

The product scope and target user were defined before implementation.

The product backlog was prioritized using P1, P2, and P3 priorities.

The highest-priority user workflows are:

1. Add a product.
2. View products and current stock.
3. Record stock increases.
4. Record stock decreases safely.

Stock movements are stored from the first stock operation so that historical information is preserved.

Detailed artifacts:

- [Project Definition](project-definition.md)
- [Product Backlog](product-backlog.md)
- [Acceptance Criteria](acceptance-criteria.md)
- [Quality Scenarios](quality-scenarios.md)

The documented quality scenarios include measurable expectations for:

- stock data integrity;
- API performance;
- data persistence.

---

## 8. Sprint 0 Risks and Terminology

A project glossary and risk list were created during Sprint 0.

Important identified risks include:

- limited previous REST API experience;
- limited Git and GitHub workflow experience;
- excessive workload caused by individual development;
- uncontrolled scope growth;
- frontend and REST API integration delays;
- testing and CI setup taking longer than expected.

The project reduces these risks by keeping the scope small, implementing features incrementally, and introducing testing and CI early.

See:

[Glossary and Risks](glossary-and-risks.md)

---

## 9. Sprint 0 Technical Setup

Sprint 0 established the initial backend structure using FastAPI.

The first endpoint implemented was:

```http
GET /health
```

Expected response:

```json
{
  "status": "ok"
}
```

An automated test verifies that:

- the endpoint is available;
- HTTP status `200` is returned;
- the expected JSON response is returned.

Tests can be executed locally with:

```bash
python -m pytest
```

The initial automated test completed successfully:

```text
1 passed
```

GitHub Actions was also configured to install the project dependencies and run the automated test suite automatically.

The first technical implementation was tracked through:

- [Issue #14 — Set up backend skeleton and health endpoint](https://github.com/gablovicco/project-inventory-manager/issues/14)
- [Pull Request #15 — Set up backend health check and CI](https://github.com/gablovicco/project-inventory-manager/pull/15)

The Pull Request was merged into `main` after the CI workflow completed successfully.

Clean installation, run, and test instructions are available in the repository:

[README](../README.md)

---

## 10. Sprint 0 Review

Sprint 0 established the required starting point for the implementation sprints.

The following were completed:

- product goal, target user, and scope;
- prioritized product backlog;
- acceptance criteria;
- measurable quality scenarios;
- development method and rationale;
- solo working agreement;
- Definition of Done;
- glossary and risk list;
- initial architecture;
- decision records;
- GitHub issue and project workflow;
- FastAPI development environment;
- initial REST endpoint;
- automated test;
- GitHub Actions CI workflow;
- setup and test instructions.

The project therefore enters Sprint 1 with both the development process and the basic technical environment already established.

See:

[Sprint 0 Review and Retrospective](sprint-0-review-retrospective.md)

---

## 11. Sprint 0 Retrospective

### What Went Well

- Keeping the initial scope small made the project manageable for individual development.
- Requirements and acceptance criteria were defined before implementation.
- The first REST endpoint provided a simple way to verify the backend environment.
- The GitHub issue, branch, commit, Pull Request, and CI workflow was practiced before feature development began.
- Automated testing and CI were introduced from the beginning.

### Difficulties and Lessons Learned

- Git and GitHub workflows were initially unfamiliar.
- The Python testing environment required some troubleshooting.
- Dependency and import issues demonstrated the importance of testing locally.
- Keeping the technical design simple is important because every part of the project must remain understandable and explainable.

### Sprint 1 Improvement Action

During Sprint 1, only **one complete P1 user workflow will be implemented at a time before starting another user story**.

The first feature should be completed end-to-end across:

```text
Browser Interface
        ↓
REST API
        ↓
Business Logic
        ↓
SQLite
        ↓
Automated Tests
```

This approach is intended to reduce unfinished work and keep each implementation step easy to test, review, and explain.

---

# Current Project Status

## 12. Status After Sprint 0

Sprint 0 is complete.

The project currently has:

- a clearly defined scope;
- a prioritized backlog;
- an established development method;
- a documented Definition of Done;
- a documented architecture;
- a working FastAPI backend;
- an automated test;
- a working GitHub Actions CI pipeline;
- documented setup instructions;
- a tested Git and Pull Request workflow.

Core inventory functionality will be developed during Sprint 1, Sprint 2, and Sprint 3.

---

# Implementation Sprints

## 13. Sprint 1

### Sprint Goal

The Sprint 1 goal is to implement the first complete inventory workflow by allowing the user to create a product, store it persistently, and see the stored product in the browser interface.

Sprint 1 primarily focuses on:

**US-01 — Add a Product**

The Sprint 0 retrospective action is followed by completing this workflow end-to-end before beginning stock-in or stock-out functionality.

### Selected User Story

US-01 requires the user to be able to:

- enter a product name;
- enter an initial stock quantity;
- define a minimum stock level;
- create a valid product;
- see the newly created product in the product list.

The product name is required.

The initial quantity and minimum stock level cannot be negative.

### Database Foundation

SQLite is used as the persistent database.

SQLModel was introduced during Sprint 1 to define database models and access SQLite while keeping the persistence layer small and understandable.

The initial Product model contains:

```text
Product
├── id
├── name
├── current_quantity
└── minimum_stock_level
```

The database is created locally as `inventory.db`.

The database file itself is excluded from Git because it contains local runtime data rather than project source code.

Database access is performed only through the FastAPI backend.

The technical decision to use SQLModel is recorded in the Decision Log.

### REST API Implementation

Sprint 1 introduced the following product endpoints:

```http
POST /products
GET /products
```

`POST /products` creates and stores a new product.

`GET /products` retrieves stored products from SQLite.

Separate models are used for API input, database storage and API output so that the responsibilities of each model remain clear.

The product creation endpoint returns:

```text
201 Created
```

for a valid product.

Invalid input is rejected by the API validation layer.

### Input Validation

The following validation rules have been implemented:

- the product name cannot be empty;
- whitespace-only product names are rejected;
- leading and trailing whitespace is removed from valid product names;
- the initial quantity cannot be negative;
- the minimum stock level cannot be negative.

For example:

```text
"Keyboard"     → accepted
"  Mouse  "    → stored as "Mouse"
"    "         → rejected
quantity = -5  → rejected
```

Manual API testing confirmed both successful and invalid requests.

### Browser-Based Frontend

A simple browser interface was created using:

- HTML;
- CSS;
- vanilla JavaScript.

The interface currently contains:

- a product-name input;
- an initial-quantity input;
- a minimum-stock-level input;
- an Add Product button;
- a product list.

JavaScript sends the form data to the FastAPI REST API as JSON.

After a successful product creation, the frontend retrieves the current product list and displays the stored products in the browser.

The current end-to-end flow is:

```text
Inventory Manager
        ↓
Browser Product Form
        ↓
JavaScript
        ↓
POST /products
        ↓
FastAPI
        ↓
Input Validation
        ↓
SQLModel
        ↓
SQLite
        ↓
GET /products
        ↓
JavaScript
        ↓
Browser Product List
```

This confirms that the browser frontend communicates with the backend through the REST API and does not access SQLite directly.

### Persistence

Products created through the API are stored in SQLite.

Stored products can later be retrieved through `GET /products` and displayed in the browser interface.

### Automated Testing

The automated test suite was extended during Sprint 1.

The tests currently verify:

- the existing health endpoint;
- successful product creation;
- rejection of negative initial quantities;
- rejection of empty product names;
- trimming of leading and trailing whitespace from product names;
- retrieval of stored products;
- successful loading of the browser home page.

The automated tests use a separate in-memory SQLite database so that testing does not modify the local application database.

The current local test result is:

```text
7 passed
```

A dependency deprecation warning is currently displayed during testing, but it does not cause the tests to fail.

### US-01 Acceptance Status

The functional acceptance criteria for US-01 have been implemented and verified:

- the user can enter a product name;
- the product name is required;
- the user can enter an initial stock quantity;
- the initial stock quantity cannot be negative;
- the user can define a minimum stock level;
- the minimum stock level cannot be negative;
- a valid product is stored successfully;
- the newly created product appears in the product list.

US-01 is functionally complete.

However, it will only be marked **Done** after the remaining applicable Definition of Done activities are completed:

- CI verification;
- self-review;
- Pull Request review;
- merge into `main`;
- project-board status update.

### Current Sprint 1 Status

The first Sprint 1 end-to-end workflow is implemented on the feature branch.

The current implementation includes:

- persistent SQLite product storage;
- SQLModel database access;
- product input validation;
- product creation REST API;
- product-list REST API;
- browser product creation interface;
- browser product list;
- isolated automated database tests;
- seven passing automated tests.

The next step is to complete the Git workflow through a Pull Request, verify CI, review the completed work and merge it into `main`.

---

## 14. Sprint 2

To be updated during Sprint 2.

---

## 15. Sprint 3

To be updated during Sprint 3.

---

## 16. Report Maintenance

This document is the project's living report.

It will continue to be updated during Sprint 1, Sprint 2 and Sprint 3 as the project evolves.

Existing artifacts, decisions and Git history will be preserved rather than replaced so that the development process remains traceable.
