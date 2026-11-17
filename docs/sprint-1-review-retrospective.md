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

## Peer Review Feedback

An external peer review was performed after the Sprint 1 increment was completed.

The reviewer inspected the code, automated tests, documentation and Git history and also ran the application locally.

All eight automated tests passed successfully in the reviewer's environment.

The reviewer positively noted:

- the detailed project documentation;
- preservation of superseded decisions in the Decision Log, such as the transition from PySide6 to the browser-based interface;
- honest documentation of development problems in the retrospectives;
- simple and readable implementation code;
- use of an isolated in-memory database for automated tests so that the local `inventory.db` file is not modified.

The review also identified several possible improvements.

### Robustness and Validation

Very large numeric quantity values can exceed the integer range supported by SQLite and may cause a server error.

A future improvement would be to define reasonable maximum values for quantity fields.

The reviewer also observed that input validation could be stricter. Some values can be converted automatically by the validation layer, product names currently have no maximum length, and duplicate or case-variant product names are currently allowed.

These behaviors are not currently defined by the Sprint 1 acceptance criteria, but they may be considered as future validation improvements.

### Application Paths

The application currently uses relative paths such as `app/static` and `inventory.db`.

This means the documented startup procedure should be executed from the project root directory.

Using paths based on the application file location could make the application more robust if it is started from another working directory.

### Dependency Reproducibility

The dependencies in `requirements.txt` are currently not pinned to specific versions.

The current CI workflow installs the latest compatible versions available at execution time.

Pinning or locking dependency versions may improve reproducibility in later development.

### User Interface Feedback

The browser interface currently displays a general error message when product creation fails:

`Could not add product.`

More specific validation feedback could improve usability.

The product list also currently has no explicit empty-state message when no products exist.

### Persistence Verification

Product persistence is implemented using SQLite, but there is not yet an automated test that explicitly restarts or recreates the application and verifies that previously stored data remains available.

This could provide stronger verification for the persistence quality scenario in a later sprint.

### Review Outcome

The peer review did not identify a problem that prevents the Sprint 1 goal from being considered complete.

The main product-creation workflow works as intended, and all eight automated tests passed in the reviewer's environment.

The identified findings are mainly robustness, validation, reproducibility and usability improvements that can be evaluated during Sprint 2 planning and later development.

No backlog priority was changed immediately as a result of the peer review.

## Retrospective

### What Went Well

The Sprint 0 improvement action worked well. Focusing on one complete P1 workflow made it possible to finish the product-creation feature across the browser interface, REST API, database and automated tests instead of starting several unfinished features.

Introducing SQLModel provided a simple persistence layer that works naturally with FastAPI and SQLite.

Automated tests helped identify missing validation coverage before the Pull Request was merged.

The GitHub Actions workflow successfully verified the implementation before it was merged into `main`.

The external peer review also provided useful feedback about robustness, validation, dependency reproducibility, usability and persistence verification without identifying a blocker in the completed Sprint 1 workflow.

### Difficulties and Lessons Learned

A significant process problem occurred on 16 November 2026 while the feature branch was being updated.

Code changes were being made locally in PyCharm while documentation changes were also being committed directly through the GitHub web interface to the same branch.

This caused the local and remote branch histories to diverge and resulted in repeated push rejections requiring remote changes to be merged before additional local commits could be pushed.

The issue did not cause implementation work to be lost, but it added unnecessary Git workflow complexity.

Another lesson was that a passing test count alone is not sufficient evidence of correct test coverage. During review, one test temporarily lacked its expected status-code assertion. The assertion was restored before the Pull Request was merged, and the complete test suite was run again successfully.

A dependency deprecation warning is still displayed during testing. It does not currently cause test failures, but it remains a technical item that may need attention later.

The peer review also showed that passing the defined Sprint 1 acceptance criteria does not mean that all possible edge cases are already covered. Robustness limits and stricter validation can be improved incrementally without expanding the completed Sprint 1 scope retrospectively.

## Sprint 2 Improvement Action

During Sprint 2, implementation changes will be made locally in PyCharm and pushed to GitHub through the normal Git workflow.

Documentation changes on the same active branch will be grouped after the implementation work whenever practical.

If editing switches between GitHub web and the local repository, the latest remote changes will be pulled before continuing local work.

This should reduce unnecessary branch divergence and make the Git workflow more predictable during Sprint 2.

The peer review findings will also be considered during Sprint 2 planning. Improvements will be prioritized only where they support the remaining P1 workflows or address a clear reliability problem, so that robustness work does not create unnecessary scope growth.
