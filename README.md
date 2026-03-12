# FastAPI Car Sharing API

A backend REST API for managing a car sharing service built with **FastAPI**, **SQLModel**, and **SQLite**.

This project demonstrates how to build a modern Python backend service with database integration, dependency injection, and RESTful endpoints.

---

# Features

- REST API built with FastAPI
- SQLite database integration
- SQLModel ORM for database models
- CRUD operations for car management
- Filter cars by size and number of doors
- Dependency-based database sessions
- Automatic API documentation with Swagger

---

# System Architecture

```
Client Request
      │
      ▼
FastAPI Application
      │
      ▼
SQLModel ORM
      │
      ▼
SQLite Database
```

---

# API Endpoints

## Get Cars

Retrieve available cars with optional filters.

```
GET /api/cars
```

Optional query parameters:

- `size`
- `doors`

Example:

```
GET /api/cars?size=medium&doors=4
```

---

## Add Car

Add a new car to the system.

```
POST /api/cars
```

Example request body:

```json
{
  "fuel": "petrol",
  "transmission": "automatic",
  "size": "medium",
  "doors": 4
}
```

---

## Update Car

Update an existing car.

```
PUT /api/cars?id=1
```

Example request body:

```json
{
  "fuel": "diesel",
  "transmission": "manual",
  "size": "large",
  "doors": 4
}
```

---

## Delete Car

Delete a car by ID.

```
DELETE /api/delete-cars/{id}
```

Example:

```
DELETE /api/delete-cars/1
```

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| FastAPI | Web framework |
| SQLModel | ORM |
| SQLite | Database |
| SQLAlchemy | Database engine |

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/fastapi-car-sharing-api.git
cd fastapi-car-sharing-api
```

Install dependencies:

```
pip install fastapi uvicorn sqlmodel sqlalchemy
```

---

# Running the Application

Start the FastAPI server:

```
uvicorn Car_Service_FastAPI:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# Skills Demonstrated

This project demonstrates:

- FastAPI REST API development
- SQLModel ORM usage
- SQLite database integration
- Backend service design
- Dependency injection in FastAPI
- API documentation with Swagger

---

# Future Improvements

- Authentication and authorization
- Pagination for car listings
- Docker containerization
- Integration with cloud databases
- Vehicle availability tracking
