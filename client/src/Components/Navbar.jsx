import React from 'react'
import { Link } from 'react-router-dom'

const Navbar = () => {
  return (
    <header>
      <div>
        <ul>
          <li>
            <Link to="/">HOME</Link>
          </li>
          <li>
            <Link to="/decks">DECKS</Link>
          </li>
          <li>
            <Link to="/flashcard">FLASHCARDS</Link>
          </li>
          <li>
            <Link to="/studysessions">STUDYSESSIONS</Link>
          </li>
        </ul>
      </div>
    </header>
  );
}

export default Navbar
