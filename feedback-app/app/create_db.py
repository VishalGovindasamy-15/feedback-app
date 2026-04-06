from app import app
from db import db

print("Creating database...")

with app.app_context():
    db.create_all()

print("Database created successfully!")