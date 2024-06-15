import { Link } from "react-router-dom";
import "./navbar.css";

function Navbar() {
  return (
    <nav className="navbar">
      <Link to="/home">Home</Link>
      <Link to="/game">Available games</Link>
      <Link to="/offer">Games on offer</Link>
      <Link to="/upcoming">Upcoming</Link>
    </nav>
  );
}

export default Navbar;
