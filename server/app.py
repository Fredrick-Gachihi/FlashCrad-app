#!/usr/bin/env python3
import os
from flask import Flask, jsonify, request
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db, Deck, User, StudySession, FlashCard
from datetime import datetime

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "your_jwt_secret_key")

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

@app.route("/")
def index():
    return "<h1>Welcome to the Deck Portal API.</h1>"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity={'id': user.id, 'username': user.username})
        return jsonify({'token': access_token}), 200
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@app.route('/decks', methods=['POST'])
def create_deck():
    data = request.get_json()
    new_deck = Deck(user_id=data['user_id'], deck_name=data['deck_name'])
    db.session.add(new_deck)
    db.session.commit()
    return jsonify({"message": "Deck created"}), 201

@app.route('/decks', methods=['GET'])
def get_decks():
    decks = Deck.query.all()
    return jsonify([deck.to_dict(rules=['-flashcards']) for deck in decks]), 200

@app.route('/decks/<int:id>', methods=['GET', 'DELETE'])
def get_delete_deck_by_id(id):
    deck = Deck.query.filter(Deck.deck_id == id).first()

    if request.method == 'GET':
        if not deck:
            return {'error': 'Deck not found'}, 404
        return jsonify(deck.to_dict()), 200

    elif request.method == 'DELETE':
        if not deck:
            return {'error': 'Deck not found'}, 404
        db.session.delete(deck)
        db.session.commit()
        return {}, 204

@app.route('/flashcards', methods=['POST'])
def create_flashcard():
    data = request.get_json()
    new_flashcard = FlashCard(deck_id=data['deck_id'], question=data['question'], answer=data['answer'])
    db.session.add(new_flashcard)
    db.session.commit()
    return jsonify({"message": "Flashcard created"}), 201

@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    flashcards = FlashCard.query.all()
    return jsonify([flashcard.to_dict() for flashcard in flashcards]), 200


@app.route('/flashcards/<int:id>', methods=['PUT'])
def update_flashcard(id):
    data = request.get_json()
    flashcard = FlashCard.query.filter(FlashCard.flashcard_id == id).first()
    if not flashcard:
        return {'error': 'Flashcard not found'}, 404

    flashcard.question = data.get('question', flashcard.question)
    flashcard.answer = data.get('answer', flashcard.answer)
    flashcard.deck_id = data.get('deck_id', flashcard.deck_id)
    
    db.session.commit()
    return jsonify(flashcard.to_dict()), 200    


@app.route('/flashcards/<int:id>', methods=['GET', 'DELETE'])
def get_delete_flashcard_by_id(id):
    flashcard = FlashCard.query.filter(FlashCard.flashcard_id == id).first()

    if request.method == 'GET':
        if not flashcard:
            return {'error': 'Flashcard not found'}, 404
        return jsonify(flashcard.to_dict()), 200

    elif request.method == 'DELETE':
        if not flashcard:
            return {'error': 'Flashcard not found'}, 404
        db.session.delete(flashcard)
        db.session.commit()
        return {}, 204

@app.route('/studysessions', methods=['POST'])
def create_studysession():
    data = request.get_json()
    new_study_session = StudySession(
        user_id=data['user_id'],
        deck_id=data['deck_id'],
        session_date=datetime.strptime(data['session_date'], '%Y-%m-%d'),
        score=data.get('score')
    )
    db.session.add(new_study_session)
    db.session.commit()
    return jsonify({"message": "Study session created"}), 201

@app.route('/studysessions', methods=['GET'])
def get_studysessions():
    studysessions = StudySession.query.all()
    return jsonify([session.to_dict() for session in studysessions]), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
