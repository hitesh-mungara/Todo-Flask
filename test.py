from app import app, db  # Import your Flask app and the db object
from sqlalchemy.exc import SQLAlchemyError

# Ensure that the app context is active
with app.app_context():
    try:
        db.create_all()  # Attempt to create the database tables
        print("Database created successfully!")
    except SQLAlchemyError as e:
        print(f"SQLAlchemy error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
