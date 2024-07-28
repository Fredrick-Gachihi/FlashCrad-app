
import React, { useState } from 'react';

const FlashCards = ({ flashCards = [], addFlashCard }) => {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleAddFlashCard = (e) => {
    e.preventDefault();
    if (question.trim() && answer.trim()) {
      addFlashCard({ question, answer });
      setQuestion('');
      setAnswer('');
    }
  };

  return (
    <div>
      <h2>Make your flashcard here.</h2>
      <form onSubmit={handleAddFlashCard}>
        <div>
          <label htmlFor="question">Question:</label>
          <input
            type="text"
            id="question"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="answer">Answer:</label>
          <input
            type="text"
            id="answer"
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            required
          />
        </div>
        <button type="submit">Add Flashcard</button>
      </form>
      <table>
        <thead>
          <tr>
            <th>Questions</th>
            <th>Answers</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {flashCards.length > 0 ? (
            flashCards.map((flashCard) => (
              <tr key={flashCard.id}>
                <td>{flashCard.question}</td>
                <td>{flashCard.answer}</td>
                <td className="buttons">
                  <button>Update</button>
                  <button>Delete</button>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="3">No flashcards available.</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default FlashCards;
