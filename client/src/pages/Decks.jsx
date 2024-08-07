import React, { useState } from 'react';
import axios from 'axios';
import '../App.css';

const Decks = ({ flashCards }) => {
  const [visibleAnswers, setVisibleAnswers] = useState({});
  const [currentIndex, setCurrentIndex] = useState(0);

  const toggleAnswerVisibility = (id) => {
    setVisibleAnswers((prevVisibleAnswers) => ({
      ...prevVisibleAnswers,
      [id]: !prevVisibleAnswers[id],
    }));
  };

  const sendFlashCardsToDatabase = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/flashcards', flashCards);
      console.log(response.data);
    } catch (error) {
      console.error('Error sending flashcards to database:', error);
    }
  };

  const handleNext = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % flashCards.length);
  };

  const handlePrev = () => {
    setCurrentIndex((prevIndex) => (prevIndex - 1 + flashCards.length) % flashCards.length);
  };

  return (
    <div className="container">
      <h2 className="heading">View the questions here.</h2>
      {flashCards.length > 0 && (
        <div>
          <h3 className="subheading">Flashcard {currentIndex + 1} of {flashCards.length}</h3>
          <p className="question">Question: {flashCards[currentIndex].question}</p>
          <p className="answer">
            Answer: {visibleAnswers[flashCards[currentIndex].id] ? flashCards[currentIndex].answer : 'Click to show answer'}
          </p>
          <button 
            className="button" 
            onClick={() => toggleAnswerVisibility(flashCards[currentIndex].id)}>
            {visibleAnswers[flashCards[currentIndex].id] ? 'Hide Answer' : 'Show Answer'}
          </button>
          <div className="navigation-buttons">
            <button 
              onClick={handlePrev} 
              disabled={flashCards.length <= 1}>
              Previous
            </button>
            <button 
              onClick={handleNext} 
              disabled={flashCards.length <= 1}>
              Next
            </button>
          </div>
        </div>
      )}
      {flashCards.length === 0 && <p>No flashcards available.</p>}
      {/* <button onClick={sendFlashCardsToDatabase}>Send Flashcards to Database</button> */}
    </div>
  );
};

export default Decks;
