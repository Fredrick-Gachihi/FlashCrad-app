from sqlalchemy import func
from faker import Faker
from app import app
from models import db, Deck, User, StudySession, FlashCard

with app.py_context():
    faker = Faker()

    FlashCard.querry.delete()
    Deck.querry.delete()
    flashCards = []
    decks = []
    for User in users:
        for _ in range(3):
            deck_name =faker.deck_name()
            userid =faker.user_id()
            
            decks.append(Deck)

            db.session.add_all(Deck)
            db.session.commit()

        for _ in range(5):
            deck_id = faker.deck_id
            question = faker.sentense()
            answer = faker.paragraph

            flashCards.append(FlashCard)

            db.session.add_all(FlashCard)
            db.session.commit    

    User.querry.delete()
    users = []
    for _ in range(10):
        username = faker.user_name()
        email =f"{username}@{domain}"
        password_hash =faker.password()

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            continue
        users.append(User)
        
        db.session.add_all(User)
        db.session.commit()

    StudySession.querry.delete()
    studySessions = []



print("Data created successfully.")