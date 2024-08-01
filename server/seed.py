from sqlalchemy import func
from faker import Faker
from app import app
from models import db, Deck, User, StudySession, FlashCard
import bcrypt

with app.app_context():
    faker = Faker()

    FlashCard.query.delete()
    StudySession.query.delete()
    Deck.query.delete()
    User.query.delete()
    db.session.commit()

    users = []
    for _ in range(10):
        username = faker.user_name()
        email = faker.unique.email()
        password_hash = bcrypt.hashpw(faker.password().encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            continue

        user = User(username=username, email=email, password_hash=password_hash)
        users.append(user)
        db.session.add(user)
    db.session.commit()

    decks = []
    flashcards = []
    for user in users:
        for _ in range(3):
            deck_name = faker.word()
            deck = Deck(user_id=user.id, deck_name=deck_name)
            decks.append(deck)
            db.session.add(deck)

        db.session.commit()

        for deck in decks:
            for _ in range(5):
                question = faker.sentence()
                answer = faker.paragraph()
                flashcard = FlashCard(deck_id=deck.id, question=question, answer=answer)
                flashcards.append(flashcard)
                db.session.add(flashcard)

    db.session.commit()

    study_sessions = []
    for user in users:
        for deck in decks:
            session_date = faker.date_this_year()
            score = faker.random_int(min=0, max=100)
            study_session = StudySession(user_id=user.id, deck_id=deck.id, session_date=session_date, score=score)
            study_sessions.append(study_session)
            db.session.add(study_session)

    db.session.commit()

print("Data created successfully.")
