import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

function Offer() {
  const [offers1, setOffers1] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/offer")
      .then((response) => response.json())
      .then((data) => {
        if (data.offers) {
          setOffers1(data.offers);
        } else {
          console.error("Unexpected data structure:", data);
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  const handlePurchase = (offer_data) => {
    alert(`Purchase: ${offer_data.title}`);
  };

  return (
    <div>
      <Link to="/games" className="btn btn-back btn-light">
        Back
      </Link>
      <div className="cards-container">
        {offers1.map((card, index) => (
          <div className="card" key={card.id}>
            <img
              src={card.image_url}
              className="card-img-top"
              alt={`Card image ${index + 1}`}
            />
            <div className="card-body">
              <h5 className="heading">{card.title}</h5>
              <div className="card-details">
                <p>Category: {card.category}</p>
                <p>Initial price: {card.initial_price}</p>
                <p>Final price: {card.current_price}</p>
                <p>Rating: {card.rating}</p>
                <p>{card.release_date}</p>
              </div>
              <button
                onClick={() => handlePurchase(card)}
                className="btn btn-success"
              >
                Buy Now
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Offer;
