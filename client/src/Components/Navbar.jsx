// // Navbar.js
// import React from 'react';
// import { Link } from 'react-router-dom';

// const Navbar = () => {
//   return (
//     <header className='nav'>
//       <div>
//         <h1>FlashCard app</h1>
//         <ul>
//           <li>
//             <Link to="/">HOME</Link>
//           </li>
//           <li>
//             <Link to="/decks">DECKS</Link>
//           </li>
//           <li>
//             <Link to="/flashcards">FLASHCARDS</Link>
//           </li>
//           <li>
//             <Link to="/studysessions">STUDY SESSIONS</Link>
//           </li>
//         </ul>
//       </div>
//     </header>
//   );
// }

// export default Navbar;

import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <header>
      <div>
        <h1>FlashCard app</h1>
        <ul>
          <li>
            <Link to="/">HOME</Link>
          </li>
          <li>
            <Link to="/decks">DECKS</Link>
          </li>
          <li>
            <Link to="/flashcards">FLASHCARDS</Link>
          </li>
          <li>
            <Link to="/studysessions">STUDYSESSIONS</Link>
          </li>
        </ul>
      </div>
    </header>
  );
};

export default Navbar;
