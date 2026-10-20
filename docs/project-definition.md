# Project Definition

## Project Title

Simple Inventory Management System

## Project Context

This project is developed as a solo semester project for the Software Development Methodologies course.

The project is intentionally kept small enough to be completed by one developer through Sprint 0 and three implementation iterations, while still demonstrating requirements management, REST API development, database usage, automated testing, CI and an iterative development process.

## Problem

Small businesses often need a simple way to keep track of their products and current stock levels.

When stock information is managed manually, it may become difficult to know how many items are currently available, which products are running low, and how the stock quantity has changed over time.

The system will provide a simple way to store product information, record stock changes and view the current inventory status.

## Target User

The primary user is a small-business employee or inventory manager responsible for maintaining product and stock information.

For the initial version, the system assumes a single type of user. Authentication and user roles are not required.

## Product Goal

The goal of the project is to create a simple inventory management system that allows a user to manage products, track stock increases and decreases, view stock movement history and identify products that are running low.

The system should provide these operations through a simple browser-based interface supported by a REST API and persistent data storage.

## Initial Scope

The first version of the system will support:

- Adding a new product.
- Viewing the list of products.
- Editing product information.
- Recording stock increases.
- Recording stock decreases.
- Preventing stock quantities from becoming negative.
- Viewing the current stock quantity of each product.
- Viewing the history of stock movements.
- Defining a minimum stock level for a product.
- Identifying products whose quantity is below the defined minimum stock level.
- Searching or filtering products.
- Accessing the main inventory operations through a REST API.
- Storing application data persistently in a database.

## Out of Scope

The following features are not planned for the initial version:

- User registration or login.
- Multiple user roles and permissions.
- Supplier management.
- Purchase orders.
- Sales and checkout functionality.
- Invoice generation.
- Payment processing.
- Barcode scanning.
- Multiple warehouses.
- Mobile application.
- Email or SMS notifications.
- Cloud synchronization.
- Advanced reporting or analytics.

These features may be considered as future extensions but are not required for the semester project.

## Assumptions

- The system will initially be used by one inventory operator at a time.
- Products are managed in a single inventory location.
- Stock changes are entered manually by the user.
- Each product has a current quantity and a minimum stock level.
- A stock decrease must never result in a negative quantity.
- The project will use a deliberately limited scope so that the complete development process can be demonstrated within the available semester time.
