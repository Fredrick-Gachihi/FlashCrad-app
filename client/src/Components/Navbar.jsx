import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav>
      <h1>FlashCard app.</h1>
      <Link to="/Home">Home</Link>
      <Link to="/decks">Decks</Link>
      <Link to="/flashcards">FlashCards</Link>
      <Link to="/studysessions">StudySessions</Link>
    </nav>
  );
};

export default Navbar;


// import React from 'react';
// import { Link } from 'react-router-dom';

// const Navbar = ({ onLogout }) => {
//   return (
//     <nav>
//       <ul>
//         <li><Link to="/decks">Decks</Link></li>
//         <li><Link to="/flashcards">Flashcards</Link></li>
//         <li><Link to="/studysessions">Study Sessions</Link></li>
//         <li><button onClick={onLogout}>Logout</button></li>
//       </ul>
//     </nav>
//   );
// };

// export default Navbar;
