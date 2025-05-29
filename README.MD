# Backend Developer Test Lucid

A RESTful API for user authentication and post management, built with FastAPI, SQLAlchemy, and Pydantic, following MVC architecture.

## Features

- JWT Authentication (Signup/Login)
- Post Management (Create, Read, Delete)
- In-memory caching
- Request validation & size limits
- Dependency injection


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/VeronikaHh/BackendDeveloperTestLucid.git
   cd BackendDeveloperTestLucid

2. Set up environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate    # Windows

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Add and fill .env file (structure in .env.sample)

## Running application

    ```bash
    uvicorn app.main:app --reload

## Potential Enhancements

- Using alembic to autogenerate migrations
- Add containerization with Docker
- Upgrade caching using fastapi_cache and redis for example
- Create custom exceptions
- Add unit tests with pytest for example
- Add endpoint documentation
- Add linters and testing (as a part of CI/CD)