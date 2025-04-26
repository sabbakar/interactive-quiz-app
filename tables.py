from flask_app import db, app
from models import User  # Your model

# This will create the tables in the database based on your models
with app.app_context():
    db.create_all()
