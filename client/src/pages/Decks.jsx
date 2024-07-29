import React, { useState } from 'react';

const Decks = ({ flashCards }) => {
  return (
    <div>
      <h2>View the questions here.</h2>
      <div>
        <h3>Flashcards:</h3>
        <table>
          <thead>
            <tr>
              <th>Questions</th>
              <th>Answers</th>
            </tr>
          </thead>
          <tbody>
            {flashCards.map((flashCard) => (
              <tr key={flashCard.id}>
                <td>{flashCard.question}</td>
                <td>{flashCard.answer}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Decks;
