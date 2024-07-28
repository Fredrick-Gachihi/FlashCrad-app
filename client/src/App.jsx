
import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Decks from './pages/Decks';
import './App.css';
import Navbar from './Components/Navbar';
import FlashCards from './pages/FlashCards';
import StudySessions from './pages/StudySesions';

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

  const addFlashCard = (newFlashCard) => {
    setFlashCards([...flashCards, { ...newFlashCard, id: flashCards.length + 1 }]);
  };

  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/decks" element={<Decks flashCards={flashCards} />} />
          <Route path="/flashcards" element={<FlashCards flashCards={flashCards} addFlashCard={addFlashCard} />} />
          <Route path="/studysessions" element={<StudySessions />} />
        </Routes>
      </div>
    </Router>
  );
}

const Home = () => <div>Home Page</div>;
// const StudySessions = () => <div>Study Sessions Page</div>;

export default App;
