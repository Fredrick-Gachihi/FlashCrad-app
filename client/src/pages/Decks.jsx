import React, { useState } from 'react';

const Decks = ({ flashCards }) => {
  const [visibleAnswers, setVisibleAnswers] = useState({});

  const toggleAnswerVisibility = (id) => {
    setVisibleAnswers((prevVisibleAnswers) => ({
      ...prevVisibleAnswers,
      [id]: !prevVisibleAnswers[id],
    }));
  };

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
                <td>{visibleAnswers[flashCard.id] ? flashCard.answer : 'Click to show answer'}</td>
                <td>
                  <button onClick={() => toggleAnswerVisibility(flashCard.id)}>
                    {visibleAnswers[flashCard.id] ? 'Hide Answer' : 'Show Answer'}
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Decks;
