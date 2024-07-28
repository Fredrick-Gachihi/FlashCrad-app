import React, { useState, useEffect } from 'react';
import Decks from './pages/Decks'; 
import './App.css';

function App() {
  const [flashCards, setFlashCards] = useState([]);

  useEffect(() => {
    fetchFlashCards();
  }, []);

  const fetchFlashCards = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/flashcards');
      const data = await response.json();
      setFlashCards(data);
    } catch (error) {
      console.error('Error fetching flashcards:', error);
    }
  };

  return (
    <div className="App">
      <Decks flashCards={flashCards} />
    </div>
  );
}

export default App;
