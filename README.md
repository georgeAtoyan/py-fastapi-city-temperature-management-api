# City Temperature Management API

A REST API built with **FastAPI**, **SQLAlchemy**, and **SQLite** for managing cities and recording their temperatures.

## Features

- Create, retrieve, update, and delete cities.
- Record temperatures associated with existing cities.
- Retrieve temperature records and filter them by city.
- Validate request data using Pydantic.
- Support pagination for list endpoints, if enabled.

## Technologies

- Python 3.13+
- FastAPI
- SQLAlchemy with asynchronous database operations
- SQLite
- aiosqlite
- Pydantic
- Uvicorn

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd py-fastapi-city-temperature-management-api
```

Replace `<repository-url>` with your repository's URL.

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

If the project contains a `requirements.txt` file:

```bash
python -m pip install -r requirements.txt
```

Otherwise, install the required packages:

```bash
python -m pip install fastapi "uvicorn[standard]" sqlalchemy aiosqlite
```

### 4. Run the application

From the project root directory, run:

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

- API base URL: http://127.0.0.1:8000
- Interactive Swagger documentation: http://127.0.0.1:8000/docs
- ReDoc documentation: http://127.0.0.1:8000/redoc

Use Swagger UI to explore the endpoints and send requests.

### 5. Database initialization

The application uses SQLite and stores its data in `city_temperature.db`.

Database tables are created during application startup using SQLAlchemy metadata, provided the models have been imported and registered correctly.

If the database file does not exist, SQLite can create it when the application first connects. The application startup process creates the required tables.

## Design Choices

### FastAPI for the API layer

FastAPI provides request handling, dependency injection, input validation integration, and automatic API documentation.

### Pydantic schemas for validation

Pydantic schemas define the expected request and response structures. Separate schemas for creating, updating, and returning cities help distinguish client-provided data from database-generated fields.

### SQLAlchemy ORM for database operations

SQLAlchemy models represent database tables as Python classes. The ORM allows database records to be created and modified using Python objects instead of writing SQL statements for every operation.

### Asynchronous database access

The application uses SQLAlchemy's asynchronous engine and `AsyncSession` to perform database operations without blocking the event loop while waiting for database I/O.

### Separation of responsibilities

The application separates its main responsibilities into modules:

- `app/main.py` initializes the FastAPI application and registers routers.
- `routers/` defines API endpoints and handles HTTP-level behavior.
- `app/schemas.py` defines data validation and serialization.
- `app/models.py` defines database models and relationships.
- `app/database.py` configures the engine, session factory, and database dependency.
- `crud.py` contains database operations.

This organization improves readability, maintainability, and testability.

### SQLite for persistence

SQLite provides a lightweight database that is easy to configure for local development and learning without requiring a separate database server.

## Assumptions and Simplifications

- Each temperature record belongs to an existing city.
- The API validates that a referenced city exists before creating a temperature record.
- City names are required and must not be empty.
- Temperature values are accepted as numeric values; additional business rules, such as acceptable minimum and maximum temperatures, are not enforced unless implemented separately.
- Authentication and authorization are outside the scope of this project.
- SQLite is intended for local development and demonstration rather than as a recommendation for every production deployment.
- Database schema migrations are not included; tables are initialized using SQLAlchemy metadata.
- Error handling covers expected cases, such as requests referencing nonexistent cities. More comprehensive logging and centralized exception handling could be added later.