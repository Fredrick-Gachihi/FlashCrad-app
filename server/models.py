from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from flask_migrate import Migrate
import bcrypt 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///deck_portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(90), nullable=False, unique=True)
    email = db.Column(db.String(90), nullable=False, unique=True)
    password_hash = db.Column(db.String(90), nullable=False)

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address

    @validates('username')
    def validate_username(self, key, username):
        assert len(username) <= 90, "Username characters should be less than ninety."
        return username

class Deck(db.Model):
    __tablename__ = 'decks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    deck_name = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    user = db.relationship('User', backref=db.backref('decks', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'deck_name': self.deck_name,
            'created_at': self.created_at
        }

class StudySession(db.Model):
    __tablename__ = 'studySessions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'), nullable=False)
    session_date = db.Column(db.Date, nullable=False)
    score = db.Column(db.Integer)

    user = db.relationship('User', backref=db.backref('studysessions', lazy=True))
    deck = db.relationship('Deck', backref=db.backref('studysessions', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'deck_id': self.deck_id,
            'session_date': self.session_date,
            'score': self.score
        }

class FlashCard(db.Model):
    __tablename__ = 'flashCards'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    deck = db.relationship('Deck', backref=db.backref('flashcards', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'deck_id': self.deck_id,
            'question': self.question,
            'answer': self.answer,
            'created_at': self.created_at
        }

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password.decode('utf-8'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@app.route('/decks', methods=['GET'])
def get_deck():
    decks = Deck.query.all()
    return jsonify([deck.to_dict() for deck in decks]), 200

if __name__ == '__main__':
    app.run(debug=True, port= 50000)

