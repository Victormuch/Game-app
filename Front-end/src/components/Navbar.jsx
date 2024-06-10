import React from "react";
import { Link } from "react-router-dom";
import "./navbar.css"
function Navbar() {
  return (
    <nav className="navbar">
      <Link to="/home">Home</Link>
      <Link to="/game">Available games</Link>
      <Link to="/add">Add game</Link>
      <Link to="/add-review">Add Review</Link>
    </nav>
  );
}

export default Navbar;
