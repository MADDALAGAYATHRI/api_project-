Flask API with JWT Authentication
This project is a simple Flask application that demonstrates how to create a RESTful API with JWT-based authentication. It includes user registration, login functionality, and a protected route.

Features
User Authentication: Register and log in with username and password.
JWT Security: Access protected routes with JSON Web Tokens.
Database Integration: SQLite for data persistence.
Modular Structure: Separate models for scalability.
Installation
Prerequisites
Python 3.7+
pip (Python package manager)
Steps
Clone the repository:

git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install the required packages:

pip install -r requirements.txt
Set up the database:

python -c "from app import db; db.create_all()"
Run the application:

python app.py
API Endpoints
Public Endpoints
POST /register: Register a new user.
Payload:

{
  "username": "string",
  "password": "string"
}
Response:

{
  "message": "User created successfully"
}
POST /login: Log in and receive a JWT token.
Payload:

{
  "username": "string",
  "password": "string"
}
Response:

{
  "access_token": "string"
}
Protected Endpoint
GET /protected: Access protected content (requires JWT token).
Headers:
{
  "Authorization": "Bearer <your_token>"
}
Response:
{
  "message": "You have access to this protected route!"
}
Project Structure
├── app.py              # Main application file
├── models.py           # Database models
├── requirements.txt    # List of dependencies
├── README.md           # Documentation (this file)
└── users.db            # SQLite database (auto-created)
Requirements
Add this to requirements.txt:

Flask
Flask-SQLAlchemy
Flask-JWT-Extended