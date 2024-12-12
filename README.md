
# Flask API with JWT Authentication

This project is a simple Flask application that demonstrates how to create a RESTful API with JWT-based authentication. It includes user registration, login functionality, and a protected route.

## Features
- **User Authentication**: Register and log in with username and password.
- **JWT Security**: Access protected routes with JSON Web Tokens.
- **Database Integration**: SQLite for data persistence.
- **Modular Structure**: Separate models for scalability.

## Installation
### Prerequisites
- Python 3.7+
- `pip` (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python -c "from app import db; db.create_all()"
   ```

5. Run the application:
   ```bash
   python app.py
   ```

## API Endpoints
### Public Endpoints
- **`POST /register`**: Register a new user.  
  **Payload**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
  **Response**:
  ```json
  {
    "message": "User created successfully"
  }
  ```

- **`POST /login`**: Log in and receive a JWT token.  
  **Payload**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
  **Response**:
  ```json
  {
    "access_token": "string"
  }
  ```

### Protected Endpoint
- **`GET /protected`**: Access protected content (requires JWT token).  
  **Headers**:
  ```json
  {
    "Authorization": "Bearer <your_token>"
  }
  ```
  **Response**:
  ```json
  {
    "message": "You have access to this protected route!"
  }
  ```

## Project Structure
```
├── app.py              # Main application file
├── models.py           # Database models
├── requirements.txt    # List of dependencies
├── README.md           # Documentation (this file)
└── users.db            # SQLite database (auto-created)
```

## Requirements
Add this to `requirements.txt`:
```plaintext
Flask
Flask-SQLAlchemy
Flask-JWT-Extended
```


