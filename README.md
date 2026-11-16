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

The project is currently in Sprint 1.

The first end-to-end inventory workflow allows the user to create products through a browser interface, store them persistently in SQLite through the FastAPI REST API, and view the stored products in the browser.

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

### View Products

```http
GET /products
```

Returns the products stored in the SQLite database.

FastAPI automatically generated API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Run the Tests

With the virtual environment activated, run:

```bash
python -m pytest
```

The current automated test suite verifies:

- the health endpoint;
- successful product creation;
- rejection of negative initial quantities;
- rejection of empty product names;
- product-name trimming;
- retrieval of stored products;
- successful loading of the browser interface.

The current local test result is:

```text
8 passed
```

The product API tests use an isolated in-memory SQLite database so that automated testing does not modify the local application database.

## Continuous Integration

The repository uses GitHub Actions.

The CI workflow automatically installs the project dependencies and runs the automated test suite when a Pull Request is opened and when changes are pushed to the `main` branch.

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

## Current Sprint

Sprint 1 focuses primarily on:

**US-01 — Add a Product**

The first end-to-end workflow is implemented on the feature branch and includes:

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

US-01 will be considered Done after the remaining Definition of Done activities are completed, including CI verification, self-review, Pull Request review and merge into `main`.
