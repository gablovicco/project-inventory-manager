# Project Inventory Manager

A simple inventory management system developed for the Software Development Methodologies semester project.

The project is developed as a solo project and follows an iterative development process using Scrum with selected XP practices.

## Current Technology Stack

- Python
- FastAPI
- SQLModel
- SQLite
- HTML, CSS and JavaScript
- pytest
- GitHub Actions

## Current Architecture

```text
Browser-based Frontend
        ↓
     HTTP / REST
        ↓
   FastAPI Backend
        ↓
      SQLModel
        ↓
   SQLite Database
```

Sprint 1 is complete.

The first end-to-end inventory workflow is complete. The application allows the user to create products through a browser interface, store them persistently in SQLite through the FastAPI REST API, and view the stored products in the browser.

## Requirements

- Python 3.13
- Git

## Setup

Clone the repository:

```bash
git clone https://github.com/gablovicco/project-inventory-manager.git
```

Enter the project directory:

```bash
cd project-inventory-manager
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment on macOS or Linux:

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

## Browser Interface

After starting the application, open:

```text
http://127.0.0.1:8000/
```

The current browser interface supports:

- adding a product;
- entering an initial stock quantity;
- defining a minimum stock level;
- viewing stored products.

## API Endpoints

### Health Check

```http
GET /health
```

Expected response:

```json
{
  "status": "ok"
}
```

### Create Product

```http
POST /products
```

Creates and stores a new product.

For a valid product, the endpoint returns:

```text
201 Created
```

The API rejects invalid product data such as:

- an empty or whitespace-only product name;
- a negative initial stock quantity;
- a negative minimum stock level.

Leading and trailing whitespace is removed from valid product names.

### View Products

```http
GET /products
```

Returns the products stored in the SQLite database.

FastAPI automatically generated API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Persistence

Products are stored in a local SQLite database.

SQLModel is used to define the database models and access SQLite.

The browser frontend does not access the database directly. All database operations are performed through the FastAPI backend.

The local database file is:

```text
inventory.db
```

This file is excluded from Git because it contains local runtime data.

## Run the Tests

With the virtual environment activated, run:

```bash
python -m pytest
```

The current automated test suite verifies:

- the health endpoint;
- successful product creation;
- rejection of negative initial quantities;
- rejection of negative minimum stock levels;
- rejection of empty product names;
- product-name trimming;
- retrieval of stored products;
- successful loading of the browser interface.

The final Sprint 1 local test result is:

```text
8 passed
```

The product API tests use an isolated in-memory SQLite database so that automated testing does not modify the local application database.

A dependency deprecation warning is currently displayed during testing, but it does not cause the test suite to fail.

## Continuous Integration

The repository uses GitHub Actions.

The CI workflow automatically installs the project dependencies and runs the automated test suite when a Pull Request is opened and when changes are pushed to the `main` branch.

Pull Request #18 passed CI with:

```text
8 passed, 1 warning
```

before being merged into `main`.

## Project Documentation

Project documentation is stored in the `docs/` directory and includes:

- project definition and scope;
- product backlog;
- acceptance criteria;
- quality scenarios;
- development method;
- working agreement and Definition of Done;
- glossary and risks;
- architecture;
- decision log;
- sprint plans;
- sprint reviews and retrospectives;
- living report.

Important Sprint 1 documents include:

- `docs/sprint-1-plan.md`
- `docs/sprint-1-review-retrospective.md`
- `docs/living-report.md`

## Sprint 1 Status

Sprint 1 is complete.

The main Sprint 1 backlog item was:

**US-01 — Add a Product**

The completed end-to-end workflow is:

```text
Browser Interface
        ↓
REST API
        ↓
Input Validation
        ↓
SQLModel
        ↓
SQLite
        ↓
Automated Tests
```

The Sprint 1 increment includes:

- persistent product storage;
- SQLModel database access;
- product input validation;
- `POST /products`;
- `GET /products`;
- browser-based product creation;
- product-list display;
- isolated automated database tests;
- eight passing automated tests;
- successful GitHub Actions CI verification.

US-01 is Done.

The implementation was tracked through:

- Issue #1 — US-01 Add a Product
- Pull Request #18 — Implement product creation workflow

Pull Request #18 was merged into `main` on 16 November 2026.

## Remaining Product Work

The following major inventory capabilities remain for later backlog work:

- stock increases;
- stock decreases;
- stock movement history;
- low-stock behavior;
- product editing;
- search and filtering.

The minimum product-list functionality required for Sprint 1 was implemented, but US-02 remains open and will be evaluated separately against its full acceptance criteria.
