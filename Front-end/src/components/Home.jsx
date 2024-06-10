import React from "react";
import { useLocation } from "react-router-dom";
import Navbar from "./Navbar";
import "./home.css";

function Home() {
  const searchParams = new URLSearchParams(useLocation().search);
  const username = searchParams.get("username");

  return (
    <div className="home-container">
      <Navbar />
      <div className="background-overlay"></div>
      <div className="home">
        <div className="content">
          <h2 className="welcome-text">Welcome {username}</h2>
          <p className="detailed-message">
            Welcome to Arcadin Realm, where dreams come true and adventures
            await at every turn. Embark on a journey through our extensive game
            library, discover hidden gems, and immerse yourself in thrilling
            quests and epic battles.
          </p>
          <button className="button">Let's get started</button>
        </div>
      </div>
    </div>
  );
}

export default Home;
