# Product Backlog

This document contains the initial prioritized backlog for the Simple Inventory Management System.

The backlog is expected to change during the project as implementation progresses and feedback is received. Changes will be preserved rather than replacing the history of the project.

## Priority Levels

- **P1 — Must Have:** Required for the minimum useful inventory workflow.
- **P2 — Should Have:** Important functionality that improves the usefulness of the product but is not required for the first working version.
- **P3 — Could Have:** Optional functionality that may be implemented if the core product is complete and time allows.

---

## Initial Product Backlog

| ID | Priority | User Story | Reason for Priority |
|---|---|---|---|
| US-01 | P1 | As an inventory manager, I want to add a product so that I can start tracking its inventory. | Products are the basic data required for all inventory operations. |
| US-02 | P1 | As an inventory manager, I want to view the product list and current stock quantities so that I can see the current state of the inventory. | The user must be able to see the inventory after products and stock changes are recorded. |
| US-03 | P2 | As an inventory manager, I want to edit product information so that incorrect or outdated information can be corrected. | Useful for normal use, but the minimum inventory workflow can function without editing in the first version. |
| US-04 | P1 | As an inventory manager, I want to record stock increases so that newly received items are reflected in the current inventory and the stock change is recorded. | Stock-in is one of the core inventory operations. |
| US-05 | P1 | As an inventory manager, I want to record stock decreases so that outgoing items are reflected correctly and the stock change is recorded. | Stock-out is a core inventory operation and must prevent the stock quantity from becoming negative. |
| US-06 | P2 | As an inventory manager, I want to see products that are below their minimum stock level so that I can identify products that may need replenishment. | Improves inventory monitoring but is not required for the first end-to-end workflow. |
| US-07 | P2 | As an inventory manager, I want to view stock movement history so that I can understand how a product's quantity has changed over time. | Stock movements are recorded as part of the P1 stock operations, but the user-facing history view can be added later. |
| US-08 | P3 | As an inventory manager, I want to search or filter products so that I can find products more easily when the inventory becomes larger. | Improves usability but is optional for the semester project. |

---

## Technical Enablers

Some work is necessary to support the product stories but does not directly represent a user-facing feature.

| ID | Priority | Technical Enabler | Reason |
|---|---|---|---|
| TE-01 | P1 | Provide the core inventory operations through a REST API. | REST/API usage is a course requirement and will provide communication between the browser-based frontend and backend. |
| TE-02 | P1 | Store product and stock movement data in a persistent database. | Inventory information must remain available after the application is closed, and stock changes must be preserved. |
| TE-03 | P1 | Create automated tests for important business rules and API behavior. | Required to verify correctness and provide test evidence. |
| TE-04 | P1 | Configure a basic CI workflow that automatically runs the automated tests. | Required to provide repeatable CI evidence during development. |

---

## Initial Prioritization Rationale

Because the project is developed by a single developer, the P1 backlog is intentionally limited to the smallest useful end-to-end inventory workflow.

The minimum useful workflow is:

1. Add a product.
2. View products and their current quantities.
3. Record stock increases.
4. Record stock decreases safely.
5. Store every stock change for traceability.

These features are enough to demonstrate a working inventory management system.

Stock movements must be recorded from the beginning because historical data cannot be reconstructed reliably later if only the current stock quantity is stored.

However, viewing that history through the user interface is treated as a P2 feature. This keeps the first implementation smaller while preserving the necessary data from the start.

Editing product information and identifying low-stock products are also P2 because they improve the usefulness of the application but are not required for the minimum working inventory workflow.

Search and filtering are P3 because they are usability improvements and can be omitted if the higher-priority functionality requires more development time.

The backlog will be reviewed after each iteration and may be reordered if implementation experience or feedback changes the priorities.
