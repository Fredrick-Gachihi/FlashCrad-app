import React, { useState } from 'react';

const Decks = ({ flashCards }) => {
  const [questions, setQuestions] = useState('');
  const [answers, setAnswers] = useState('');

  return (
    <div>
      <div>
        <label htmlFor="questions">Questions:</label>
        <input
          type="text"
          id="questions"
          value={questions}
          onChange={(e) => setQuestions(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="answers">Answers:</label>
        <input
          type="text"
          id="answers"
          value={answers}
          onChange={(e) => setAnswers(e.target.value)}
        />
      </div>
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

