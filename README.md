# Project Inventory Manager

A simple inventory management system developed for the Software Development Methodologies semester project.

The project is developed as a solo project and follows an iterative development process using Scrum with selected XP practices.

## Current Technology Stack

- Python
- FastAPI
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
   SQLite Database
```

The project is currently in Sprint 0. The initial technical setup includes a minimal FastAPI backend and an automated health-check test.

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

## Run the Backend

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

Health endpoint:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "ok"
}
```

FastAPI automatically generated API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Run the Tests

With the virtual environment activated, run:

```bash
python -m pytest
```

The current Sprint 0 test verifies that the health endpoint:

- is available;
- returns HTTP status `200`;
- returns `{"status": "ok"}`.

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
- decision log.