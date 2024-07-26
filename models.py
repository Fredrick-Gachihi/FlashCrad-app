from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
import bcrypt 
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///deck_portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class User(db.Model):
    __tablename__ = 'users'

    id = db.column(db.integer, primary_key= True)
    username = db.column(db.string(90), nullable =False, unique =True)
    email = db.column(db.string(90), nullable =False  False, unique True)
    password_hash = db.column(db.strimg(90), nullable = False)

    @validates('email')
    def validate_email(self, key, address):
        assert '@'in address
        return address
    
    @validates('username')
    def validate_username(self, key, username):
        assert len(username) <= 90, "Username characters should be less than ninety."
        return username

class Deck(db.Model):
    __tablename__ = 'decks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    deck_name = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    user = db.relationship('User', backref=db.backref('decks', lazy=True))

    

class StudySession(db.Model):
    __tablename__ = 'studySessions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.deck_id'), nullable=False)
    session_date = db.Column(db.Date, nullable=False)
    score = db.Column(db.Integer)

    user = db.relationship('User', backref=db.backref('studysessions', lazy=True))
    deck = db.relationship('Deck', backref=db.backref('studysessions', lazy=True))

class FlashCard(db.model):
    __tablename__ = 'flashCards'    

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.deck_id'), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    deck = db.relationship('Deck', backref=db.backref('flashcards', lazy=True))


@app.route('/users', method =['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password_hash=data['password_hash'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201
 
@app.route('/user', method =['GET'])
def get_deck():
    deck = Deck.query.all()
    return jsonify([deck.to_dict() for deck in decks])


if __name__ == '__main__':
    app.run(debug=True)   