from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

# Initialize Flask application
app = Flask(__name__)

# Set up the configuration for the database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Secret key for JWT

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Database model for Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Home route
@app.route('/')
def home():
    return jsonify(message="Welcome to the API!")

# Register route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify(message="Missing username or password"), 400

    # Check if user already exists
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify(message="User already exists"), 400

    # Create new user
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message="User created successfully"), 201

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify(message="Missing username or password"), 400

    # Check if user exists
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if not user:
        return jsonify(message="Invalid username or password"), 401

    # Create JWT token
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

# Protected route (requires JWT token)
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="You have access to this protected route!")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
