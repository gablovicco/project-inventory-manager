# Sprint 1 Review and Retrospective

## Sprint 1 Goal

The Sprint 1 goal was to implement the first complete inventory workflow by allowing the user to create a product, store it persistently, and see the stored product in the browser interface.

The main selected backlog item was:

**US-01 — Add a Product**

The Sprint 0 retrospective action was also followed by focusing on one complete P1 workflow before starting another major user story.

## Sprint 1 Review

Sprint 1 produced the first working end-to-end inventory feature.

The user can now create a product through the browser interface by entering:

- a product name;
- an initial stock quantity;
- a minimum stock level.

The browser communicates with the FastAPI backend through the REST API.

The backend validates the input, stores valid products persistently in SQLite using SQLModel, and allows the stored products to be retrieved and displayed in the browser.

The following REST endpoints were implemented:

`POST /products`

`GET /products`

Input validation now ensures that:

- the product name is required;
- whitespace-only product names are rejected;
- leading and trailing whitespace is removed;
- the initial stock quantity cannot be negative;
- the minimum stock level cannot be negative.

The US-01 acceptance criteria were successfully demonstrated.

A valid product is stored successfully and appears in the product list after creation.

The automated test suite was expanded to eight tests covering:

- the health endpoint;
- successful product creation;
- rejection of negative initial quantities;
- rejection of negative minimum stock levels;
- rejection of empty product names;
- product-name trimming;
- retrieval of stored products;
- successful loading of the browser interface.

The final local test result after merging Sprint 1 into `main` was:

`8 passed`

GitHub Actions CI also completed successfully for Pull Request #18.

Sprint 1 implementation was completed through:

- Issue #1 — US-01 Add a Product;
- Pull Request #18 — Implement product creation workflow.

Pull Request #18 was merged into `main` on 16 November 2026, and Issue #1 was closed.

## Completed and Incomplete Work

US-01 — Add a Product was completed during Sprint 1.

The minimum product-list functionality required to demonstrate the newly created product was also implemented.

US-02 is not automatically considered complete because its full acceptance criteria must still be evaluated separately.

Stock increases, stock decreases, stock movement history, low-stock behavior, product editing and search were not implemented during Sprint 1 and remain future backlog work.

## Backlog Changes

The Product Backlog was reviewed at the end of Sprint 1.

The following status changes were made:

- US-01 — Add a Product moved to Done after its acceptance criteria were verified, CI passed, Pull Request #18 was merged into `main`, and Issue #1 was closed.
- US-02 — View Products and Current Stock remains open and P1. Some product-list functionality was implemented to support US-01, but US-02 has not been marked Done because its complete acceptance criteria have not yet been evaluated.
- US-04 — Record Stock Increase remains open and P1.
- US-05 — Record Stock Decrease remains open and P1.
- US-03, US-06 and US-07 remain P2.
- US-08 remains P3.

No backlog priorities were changed during Sprint 1.

The Sprint 1 implementation experience did not require expanding the product scope. The project will continue to prioritize the remaining P1 inventory workflows before starting lower-priority functionality.

## Product Capability After Sprint 1

At the end of Sprint 1, the product can:

- open a browser-based inventory interface;
- create a product with a name, initial quantity and minimum stock level;
- validate product input in the backend;
- reject invalid negative quantities;
- store valid products persistently in SQLite;
- retrieve stored products through the REST API;
- display stored products in the browser.

The application therefore provides its first complete end-to-end inventory workflow.

## Remaining Uncertainty

The stock-changing workflow has not yet been implemented.

The following behavior therefore remains to be implemented and verified in later sprints:

- increasing product stock;
- decreasing product stock;
- preventing a stock decrease from producing a negative quantity;
- creating Stock Movement records;
- verifying that the displayed quantity reflects completed stock operations;
- displaying stock movement history;
- low-stock behavior.

US-02 also remains open because its complete acceptance criteria have not yet been evaluated independently.

## Retrospective

### What Went Well

The Sprint 0 improvement action worked well. Focusing on one complete P1 workflow made it possible to finish the product-creation feature across the browser interface, REST API, database and automated tests instead of starting several unfinished features.

Introducing SQLModel provided a simple persistence layer that works naturally with FastAPI and SQLite.

Automated tests helped identify missing validation coverage before the Pull Request was merged.

The GitHub Actions workflow successfully verified the implementation before it was merged into `main`.

### Difficulties and Lessons Learned

A significant process problem occurred on 16 November 2026 while the feature branch was being updated.

Code changes were being made locally in PyCharm while documentation changes were also being committed directly through the GitHub web interface to the same branch.

This caused the local and remote branch histories to diverge and resulted in repeated push rejections requiring remote changes to be merged before additional local commits could be pushed.

The issue did not cause implementation work to be lost, but it added unnecessary Git workflow complexity.

Another lesson was that a passing test count alone is not sufficient evidence of correct test coverage. During review, one test temporarily lacked its expected status-code assertion. The assertion was restored before the Pull Request was merged, and the complete test suite was run again successfully.

A dependency deprecation warning is still displayed during testing. It does not currently cause test failures, but it remains a technical item that may need attention later.

## Sprint 2 Improvement Action

During Sprint 2, implementation changes will be made locally in PyCharm and pushed to GitHub through the normal Git workflow.

Documentation changes on the same active branch will be grouped after the implementation work whenever practical.

If editing switches between GitHub web and the local repository, the latest remote changes will be pulled before continuing local work.

This should reduce unnecessary branch divergence and make the Git workflow more predictable during Sprint 2.
