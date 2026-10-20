# Acceptance Criteria

This document defines the acceptance criteria for the user stories in the initial Product Backlog.

The criteria are used to determine whether a user story has been implemented successfully and can be considered complete together with the project's Definition of Done.

---

## US-01 — Add a Product

**Priority:** P1 — Must Have

**User Story:**  
As an inventory manager, I want to add a product so that I can start tracking its inventory.

### Acceptance Criteria

- The user can enter a product name.
- A product name is required.
- The user can enter an initial stock quantity.
- The initial stock quantity cannot be negative.
- The user can define a minimum stock level.
- The minimum stock level cannot be negative.
- A valid product is stored successfully.
- The newly created product appears in the product list.

---

## US-02 — View Products and Current Stock

**Priority:** P1 — Must Have

**User Story:**  
As an inventory manager, I want to view the product list and current stock quantities so that I can see the current state of the inventory.

### Acceptance Criteria

- The user can open the product list.
- Each product displays its name and current stock quantity.
- Products stored in the database are shown in the list.
- The displayed quantity reflects the latest completed stock operation.
- If no products exist, the application shows an empty state without an error.

---

## US-03 — Edit Product Information

**Priority:** P2 — Should Have

**User Story:**  
As an inventory manager, I want to edit product information so that incorrect or outdated information can be corrected.

### Acceptance Criteria

- The user can select an existing product for editing.
- The user can change the product name.
- The user can change the minimum stock level.
- The product name cannot be empty.
- The minimum stock level cannot be negative.
- Valid changes are saved successfully.
- The updated product information is visible in the product list.

---

## US-04 — Record Stock Increase

**Priority:** P1 — Must Have

**User Story:**  
As an inventory manager, I want to record stock increases so that newly received items are reflected in the current inventory and the stock change is recorded.

### Acceptance Criteria

- The user can select an existing product.
- The user can enter a quantity to add.
- The stock-in quantity must be greater than zero.
- The product's current stock quantity increases by the entered amount.
- A stock movement record is created for the operation.
- The stock movement stores the related product, quantity, movement type and date/time.
- The updated stock quantity is visible after the operation is completed.

---

## US-05 — Record Stock Decrease

**Priority:** P1 — Must Have

**User Story:**  
As an inventory manager, I want to record stock decreases so that outgoing items are reflected correctly and the stock change is recorded.

### Acceptance Criteria

- The user can select an existing product.
- The user can enter a quantity to remove.
- The stock-out quantity must be greater than zero.
- The operation is rejected if it would make the current stock quantity negative.
- A valid stock-out operation decreases the current stock quantity by the entered amount.
- A stock movement record is created for every successful stock-out operation.
- The stock movement stores the related product, quantity, movement type and date/time.
- The updated stock quantity is visible after the operation is completed.

---

## US-06 — Identify Low-Stock Products

**Priority:** P2 — Should Have

**User Story:**  
As an inventory manager, I want to see products that are below their minimum stock level so that I can identify products that may need replenishment.

### Acceptance Criteria

- Each product can have a minimum stock level.
- A product is considered low in stock when its current quantity is below its minimum stock level.
- The user can view which products are currently low in stock.
- The low-stock status is updated after a stock increase or stock decrease.
- Products that are not below their minimum stock level are not shown as low stock.

---

## US-07 — View Stock Movement History

**Priority:** P2 — Should Have

**User Story:**  
As an inventory manager, I want to view stock movement history so that I can understand how a product's quantity has changed over time.

### Acceptance Criteria

- The user can view recorded stock movements.
- Each stock movement shows the related product.
- Each stock movement shows whether it was a stock increase or stock decrease.
- Each stock movement shows the quantity changed.
- Each stock movement shows the date and time of the operation.
- Existing stock movement records remain available after the application is restarted.

---

## US-08 — Search or Filter Products

**Priority:** P3 — Could Have

**User Story:**  
As an inventory manager, I want to search or filter products so that I can find products more easily when the inventory becomes larger.

### Acceptance Criteria

- The user can enter a product name or part of a product name.
- Products matching the search input are displayed.
- Products that do not match the search input are excluded from the displayed results.
- Clearing the search shows the full product list again.

---

## Relationship to Definition of Done

Meeting the acceptance criteria alone does not automatically make a backlog item Done.

A completed item must also satisfy the applicable conditions in the project's [Definition of Done](working-agreement-and-dod.md), including testing, CI, review, documentation and merge requirements.
