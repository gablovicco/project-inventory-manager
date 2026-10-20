# Glossary and Risk List

This document defines important domain terms used in the project and records the main risks identified during Sprint 0.

---

# Glossary

## Product

An item whose inventory quantity is tracked by the system.

## Stock

The current quantity of a product available in the inventory.

## Stock In

An operation that increases the current stock quantity of a product.

Example: receiving 10 new units of a product.

## Stock Out

An operation that decreases the current stock quantity of a product.

Example: removing 3 units because they were sold or otherwise left the inventory.

## Stock Movement

A recorded change in the stock quantity of a product.

Each stock movement represents either a stock increase or stock decrease and stores information about the quantity changed and when the operation occurred.

## Current Quantity

The number of units of a product currently available in the inventory.

## Minimum Stock Level

A configurable quantity used to determine when a product is considered low in stock.

## Low Stock

A product state where the current quantity is below its defined minimum stock level.

## Inventory Manager

The primary user of the system who manages products and stock information.

## REST API

The interface used by the browser-based frontend to communicate with the backend.

The API will expose operations for retrieving and modifying inventory data using HTTP requests.

---

# Risk List

| ID | Risk | Probability | Impact | Planned Response |
|---|---|---|---|---|
| R-01 | REST API development is new to the developer. | Medium | High | Begin with a very small API endpoint during Sprint 0 before implementing inventory features. Add API functionality incrementally. |
| R-02 | Git and GitHub workflow experience is limited. | Medium | High | Use a simple and consistent workflow based on issues, feature branches, commits, pull requests and CI. Practice the workflow with a small Sprint 0 task before Sprint 1. |
| R-03 | The project is developed by one person, creating a risk of excessive workload. | High | High | Keep the P1 backlog intentionally small. Complete required functionality before starting P2 or P3 work. |
| R-04 | The project scope may grow during development. | Medium | High | New ideas will normally be added to the backlog rather than immediately implemented. Out-of-scope features will remain excluded unless there is a clear reason to change the scope. |
| R-05 | Problems integrating the browser-based frontend with the REST API may delay development.| Medium | Medium | First verify communication with a small endpoint before building full user workflows. Keep the client-server interaction simple. |
| R-06 | Automated testing or CI configuration may take longer than expected. | Medium | Medium | Configure one simple automated test and CI workflow during Sprint 0, then extend the same setup during later sprints. |

---

# Risk Management Approach

The risk list will be reviewed during each sprint.

If a risk becomes a real problem, its effect on the sprint or backlog will be recorded rather than hidden.

The project will prefer simpler solutions when they satisfy the same requirement and reduce delivery risk.
