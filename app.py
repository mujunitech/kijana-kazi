from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kijana_kazi.db'
app.config['SECRET_KEY'] = 'your-secret-key-123'

# Initialize database
db = SQLAlchemy(app)

# Define models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Initialize database within app context
with app.app_context():
    db.create_all()

# Routes go here
@app.route('/')
def home():
    return "Welcome to Kijana Kazi!"

if __name__ == '__main__':
    app.run(debug=True)
