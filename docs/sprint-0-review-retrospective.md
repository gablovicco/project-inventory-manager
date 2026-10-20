# Sprint 0 Review and Retrospective

## Sprint 0 Goal

The goal of Sprint 0 was to establish a clear and manageable foundation for the Inventory Manager project before starting the implementation sprints.

This included defining the product scope, preparing the backlog and quality expectations, selecting the development method and architecture, establishing the development workflow, and verifying that the basic technical environment works.

## Sprint 0 Review

During Sprint 0, the following project foundations were established:

- the product goal, target user, scope, assumptions and exclusions were defined;
- the product backlog was created and prioritized;
- acceptance criteria were defined for the user stories;
- measurable quality scenarios were documented;
- Scrum with selected XP practices was chosen and adapted for individual development;
- a solo working agreement and Definition of Done were established;
- project risks and glossary terms were documented;
- the initial architecture was defined as a browser-based frontend communicating with a FastAPI REST backend and SQLite database;
- important technical and project decisions were recorded;
- a GitHub repository and project board were established;
- an issue, branch, commit and Pull Request workflow was practiced;
- a minimal FastAPI backend was created;
- a `GET /health` endpoint was implemented;
- an automated test for the health endpoint was added;
- GitHub Actions continuous integration was configured;
- the CI workflow successfully executed the automated test;
- setup, run and test instructions were added to the README.

The first technical setup work was completed through issue #14 and Pull Request #15.

At the end of Sprint 0, the project has a working development environment and a tested REST API foundation. The main inventory functionality has intentionally not been implemented yet because it belongs to the implementation sprints.

## Retrospective

### What Went Well

- Keeping the initial scope small made the project easier to understand and manage as an individual project.
- The project requirements were translated into prioritized backlog items and explicit acceptance criteria before implementation started.
- The first REST endpoint provided a simple way to verify that the backend environment was working.
- The GitHub issue, branch, Pull Request and CI workflow was successfully practiced before implementing inventory features.
- Automated testing and CI were introduced at the beginning of the project rather than being postponed until later.

### Difficulties and Lessons Learned

- Git and GitHub workflows were initially unfamiliar and required learning the purpose of branches, commits, Pull Requests and CI.
- Setting up the Python testing environment required troubleshooting import and dependency-related issues.
- The first technical setup showed the importance of testing changes locally before relying on CI.
- Keeping implementation simple is important because every part of the project must remain understandable and explainable.

## Sprint 1 Improvement Action

During Sprint 1, only one complete P1 user workflow will be implemented at a time before starting another user story.

The first implementation should cover a small end-to-end flow from the browser interface through the REST API to persistent storage and automated tests.

This is intended to reduce unfinished work and make each implementation step easier to test, review and explain.
