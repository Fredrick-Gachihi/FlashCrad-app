
import React from 'react';

const FlashCards = ({ flashCards = [] }) => {
  return (
    <div>
      <h2>Make your flashcard here.</h2>
      <table>
        <thead>
          <tr>
            <th>Questions</th>
            <th>Answers</th>
          </tr>
        </thead>
        <tbody>
          {flashCards.length > 0 ? (
            flashCards.map((flashCard) => (
              <tr key={flashCard.id}>
                <td>{flashCard.question}</td>
                <td>{flashCard.answer}</td>
                <td>
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
