import React, { useState, useEffect } from 'react';
import FlashCards from './pages/FlashCards';
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
      <FlashCards flashCards={flashCards} />
    </div>
  );
}

export default App;
