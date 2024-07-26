from sqlalchemy import func
from faker import Faker
from app import app
from models import db, Deck, User, StudySession, FlashCard

with app.py_context():
    faker = Faker()

    Deck.querry.delete()
    decks = []

    User.querry.delete()
    users = []


    StudySession.querry.delete()
    studySessions = []

    FlashCard.querry.delete()
    flashCards = []



print("Data created successfully.")