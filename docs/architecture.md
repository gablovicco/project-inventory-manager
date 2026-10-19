# Initial Architecture

This document describes the initial architecture of the Simple Inventory Management System.

The architecture is intentionally kept simple because the project is developed by one person and the current scope does not require a more complex distributed system.

The architecture may evolve during the implementation iterations if a real project requirement justifies a change.

---

## Architecture Overview

The system consists of three main parts:

1. PySide6 Desktop Client
2. FastAPI REST Backend
3. SQLite Database

```text
┌───────────────────────────────┐
│                               │
│     PySide6 Desktop Client    │
│                               │
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
