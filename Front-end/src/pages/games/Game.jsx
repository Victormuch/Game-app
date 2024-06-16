import React, { useState, useEffect } from "react";
import "./game.css";
import Review from "./Review";
import { Link } from "react-router-dom";

function Game() {
  const [cardData, setCardData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/games1")
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log("Fetched data:", data);
        setCardData(data.games1); 
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  function handlePurchase(card) {
    alert(`Purchased ${card.title}. Enjoy.`);
  }

  function handleRatingChange(index, newRating) {
    const updatedCardData = [...cardData];
    updatedCardData[index].rating = newRating;
    setCardData(updatedCardData);
  }
  return (
    <div>
      <Link to="/home" className="btn btn-back btn-light">
        Back
      </Link>
      <div className="cards-container">
        {cardData.map((card, index) => (
          <div className="card" key={index}>
            <img
              src={card.image_url}
              className="card-img-top"
              alt={`Card image ${index + 1}`}
            />
            <div className="card-body">
              <h5 className="heading">{card.title}</h5>
              <div className="card-details">
                <p>Category: {card.category}</p>
                <p>Price: {card.price}</p>
                <p>Rating: {card.rating}</p>
                <p>{card.release_date}</p>
              </div>
              <button
                onClick={() => handlePurchase(card)}
                className="btn btn-success"
              >
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
      <div className="next-page">
        <Link to="/offer" className="btn btn-back btn-light">
          Next Page
        </Link>
      </div>
    </div>
  );
}

export default Game;
