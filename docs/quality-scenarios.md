# Quality Scenarios

This document defines measurable quality expectations for the Simple Inventory Management System.

These scenarios are intentionally limited to qualities that are relevant to the project and can be verified during development.

---

## QS-01 — Prevent Invalid Stock Levels

**Quality Attribute:** Reliability / Data Integrity

### Scenario

When an inventory manager attempts to remove more units than are currently available for a product, the system must reject the operation.

### Measure

- The stock quantity must never become negative.
- The rejected operation must not change the current stock quantity.
- No successful stock movement record should be created for the rejected operation.

### Verification

This behavior will be verified using automated tests for the stock-decrease business logic and REST API.

---

## QS-02 — Product List Response Time

**Quality Attribute:** Performance

### Scenario

When the inventory contains up to 1,000 products, the user should be able to retrieve the product list without a noticeable delay.

### Measure

The REST API should return the product list within 1 second on the development machine for a dataset containing up to 1,000 products.

### Verification

A performance check will be performed using a test dataset containing up to 1,000 products.

---

## QS-03 — Persistent Inventory Data

**Quality Attribute:** Reliability / Persistence

### Scenario

When the application is closed and started again, previously stored inventory information must still be available.

### Measure

After restarting the application:

- previously created products must still exist;
- current stock quantities must remain unchanged;
- previously recorded stock movements must remain available.

### Verification

This will be verified by storing test data, restarting the application and confirming that the data can still be retrieved from the database.
