# Event Subscription


## Generated here

1. Backend with FastAPI: manages the routes and business logic.
2. Database: stores the form information, such as question and answer options and products.
3. Frontend with HTML/JavaScript: renders the form in the browser and performs calculations on the client side.


Project Structure

```
.
├── app
│   ├── main.py           # Main entry point for the FastAPI app
│   ├── models.py         # Database models and ORM classes
│   ├── schemas.py        # Pydantic schemas for request/response validation
│   ├── database.py       # Database connection setup
│   ├── routers           # Router modules for endpoints
│   │   ├── form.py       # Endpoint for handling form-related routes
│   │   └── products.py   # Endpoint for handling product-related routes
└── static
    └── form.html         # HTML form page for the front-end
└── requirements.txt      # Dependency requirements for the project
```

### Step 1: Backend with FastAPI

1. Database Configuration - We will use SQLite for simplicity.
2. Model Definition - Models for questions, answers and products.
3. Form and Product Routes - To send the answers and list products.


### Step 2: Frontend with HTML/JavaScript

### Step 3: requirements.txt file


## Running the Application

1. Install the dependencies with pip install -r requirements.txt.
2. Start the server with uvicorn app.main:app --reload.
3. Access the application at http://127.0.0.1:8000/static/form.html.

This framework provides a basic application where questions are loaded, products are listed with their prices, and a total is calculated based on the quantities selected.

