import React, { useState, useEffect } from "react";
import "./game.css";
import { Navbar } from "react-bootstrap";
import Review from "./Review";

function Game() {
  const [cardData, setCardData] = useState([]);

  useEffect(() => {
    // Fetch data from FastAPI endpoint
    fetch("http://127.0.0.1:8000/games") // Corrected endpoint
      .then((response) => response.json())
      .then((data) => {
        setCardData(data.games); // Corrected data key
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  function handlePurchase() {
    alert("Purchased! Enjoy");
  }

  // Function to handle rating change
  function handleRatingChange(index, newRating) {
    const updatedCardData = [...cardData];
    updatedCardData[index].rating = newRating;
    setCardData(updatedCardData);
  }

  return (
    <div>
      <Navbar />
      <div className="cards-container">
        {cardData.map((card, index) => (
          <div className="card" key={index}>
            <img
              src={card.image_url} // Corrected key
              className="card-img-top"
              alt={`Card image ${index + 1}`}
            />
            <div className="card-body">
              <h5 className="heading">{card.title}</h5>
              <div className="card-details">
                <p>Category: {card.category}</p>
                <p>Price: {card.price}</p>
                <p>Rating: {card.rating}</p>
                <p>{card.release_date}</p> // Corrected key
              </div>
              <button onClick={handlePurchase} className="btn btn-success">
                Buy Now
              </button>
              <Review
                rating={card.rating}
                setRating={(newRating) => handleRatingChange(index, newRating)}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Game;
