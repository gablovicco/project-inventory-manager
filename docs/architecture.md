# Initial Architecture

This document describes the initial architecture of the Simple Inventory Management System.

The architecture is intentionally kept simple because the project is developed by one person and the current scope does not require a more complex distributed system.

The architecture may evolve during the implementation iterations if a real project requirement justifies a change.

---

## Architecture Overview

The system consists of three main parts:

1. Browser-based Frontend
2. FastAPI REST Backend
3. SQLite Database

```text
┌───────────────────────────────┐
│                               │
│     Browser-based Frontend    │
│                               │
│  - HTML structure             │
│  - Basic CSS                  │
│  - JavaScript interactions    │
│  - Product forms              │
│  - Product list               │
│  - Stock operations           │
│                               │
└───────────────┬───────────────┘
                │
                │ HTTP / REST
                ▼
┌───────────────────────────────┐
│                               │
│       FastAPI Backend         │
│                               │
│  - REST endpoints             │
│  - Input validation           │
│  - Business rules             │
│  - Database operations        │
│                               │
└───────────────┬───────────────┘
                │
                │ SQLite access
                ▼
┌───────────────────────────────┐
│                               │
│       SQLite Database         │
│                               │
│  - Products                   │
│  - Stock Movements            │
│                               │
└───────────────────────────────┘
```

---

## Browser-based Frontend

The user interface will be implemented using standard HTML, CSS and JavaScript.

Its responsibility is to provide a simple interface for the inventory manager.

The initial frontend will support the core workflow:

- adding a product;
- viewing products and current stock quantities;
- recording stock increases;
- recording stock decreases.

P2 and P3 functionality may later add:

- editing product information;
- identifying low-stock products;
- viewing stock movement history;
- searching or filtering products.

The frontend will not access the SQLite database directly.

Instead, JavaScript will communicate with the FastAPI backend using HTTP requests to the REST API.

No frontend framework such as React or Vue is planned for the initial version.

---

## REST API Backend

The backend will be implemented using FastAPI.

The REST API acts as the boundary between the frontend and the application logic.

Its responsibilities include:

- receiving HTTP requests from the frontend;
- validating incoming data;
- applying inventory business rules;
- reading and writing persistent data;
- returning appropriate responses to the frontend.

The initial API is expected to include operations similar to:

```text
GET  /products
POST /products

POST /products/{id}/stock-in
POST /products/{id}/stock-out
```

The exact API will be refined during implementation.

Additional endpoints will only be introduced when required by backlog items.

---

## Business Rules

Business rules will be handled by the backend rather than by the frontend.

Examples include:

- a product name cannot be empty;
- stock-in quantities must be greater than zero;
- stock-out quantities must be greater than zero;
- a stock-out operation must not make the current quantity negative;
- every successful stock increase or decrease must create a Stock Movement record.

Keeping these rules in the backend ensures that inventory rules are applied consistently regardless of how the REST API is accessed.

---

## Database

SQLite will provide local persistent storage.

The initial domain contains two main data concepts.

### Product

Represents an item whose inventory is tracked.

Initial information is expected to include:

- ID;
- name;
- current quantity;
- minimum stock level.

### Stock Movement

Represents a successful change in product stock.

Initial information is expected to include:

- ID;
- product ID;
- movement type (`IN` or `OUT`);
- quantity;
- date and time.

Stock movements will be stored from the beginning even though the user-facing movement history is currently a P2 feature.

This ensures that historical stock information is preserved from the first stock operation.

---

## Example Request Flow

A stock decrease will follow this general flow:

```text
Inventory Manager
       ↓
Browser Interface
       ↓
JavaScript HTTP Request
       ↓
FastAPI REST Endpoint
       ↓
Validate Request
       ↓
Check Current Stock
       ↓
Update Product
       ↓
Create Stock Movement
       ↓
Save Changes in SQLite
       ↓
Return API Response
       ↓
Update Browser Interface
```

For example:

1. The user selects a product.
2. The user requests a stock decrease of 3 units.
3. JavaScript sends the request to the REST API.
4. The backend validates the requested quantity.
5. The backend checks whether enough stock is available.
6. If the operation is valid, the current quantity is decreased.
7. A Stock Movement record is created.
8. The changes are stored in SQLite.
9. The API returns the result.
10. The browser interface displays the updated quantity.

If the requested decrease would result in negative stock, the backend rejects the operation and the inventory data remains unchanged.

---

## Architecture Principles

- Keep the system small and understandable.
- Use the REST API as the boundary between the frontend and application logic.
- Keep business rules in the backend.
- Prevent the frontend from directly accessing or modifying the database.
- Preserve stock movement data from the beginning.
- Avoid unnecessary frontend frameworks or architectural layers.
- Add new architectural components only when they solve a real problem.
- Prefer solutions that can be understood, tested and explained by the developer.
