from sqlalchemy import func
from faker import Faker
from app import app
from models import db, Deck, User, StudySession, FlashCard

with app.py_context():
    faker = Faker()

    


print("Data created successfully.")