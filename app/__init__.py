from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Import the routes (ensure this comes after app initialization)
from app import routes