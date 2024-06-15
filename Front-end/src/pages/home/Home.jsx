import React from "react";
import { Link, useLocation } from "react-router-dom";
import "./home.css";
import Navbar from "../../components/Navbar";

function Home() {
  const searchParams = new URLSearchParams(useLocation().search);
  const username = searchParams.get("username");

  return (
    <div>
      <Navbar />
      <div className="home-container">
        <div className="home">
          <div className="content">
            <h2 className="welcome-text">Welcome {username}</h2>
            <p className="detailed-message">
              Welcome to Arcadin Realm, where dreams come true and adventures
              await at every turn. Embark on a journey through our extensive
              game library, discover hidden gems, and immerse yourself in
              thrilling quests and epic battles.
            </p>
            <Link to= "/game"class="cta">
              <span>Let's get started</span>
              <svg width="15px" height="10px" viewBox="0 0 13 10">
                <path d="M1,5 L11,5"></path>
                <polyline points="8 1 12 5 8 9"></polyline>
              </svg>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
