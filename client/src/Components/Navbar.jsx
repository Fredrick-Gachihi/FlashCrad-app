import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav>
      <Link to="/Home">Home</Link>
      <Link to="/decks">Decks</Link>
      <Link to="/flashcards">FlashCards</Link>
      <Link to="/studysessions">StudySessions</Link>
    </nav>
  );
};

export default Navbar;
