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
