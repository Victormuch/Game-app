import React, { useState, useEffect } from "react";
import Review from "../games/Review";


function Offer() {
  const [offers, setOffers] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/offer")
      .then((response) => response.json())
      .then((data) => {
        setOffers(data.offer);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  const handlePurchase = (offer) => {
    console.log("Purchase:", offer.title);
  };

  function handleRatingChange(index, newRating) {
    const updatedCardData = [...cardData];
    updatedCardData[index].rating = newRating;
    setCardData(updatedCardData);
  }
  return (
    <div className="body">
      <div className="cards-container">
        {offers.map((offer, index) => (
          <div className="card" key={index}>
            <img
              src={offer.image_url}
              className="card-img-top"
              alt={`Card image ${index + 1}`}
            />
            <div className="card-body">
              <h5 className="card-title">{offer.title}</h5>
              <div className="card-details">
                <p>Category: {offer.category}</p>
                <p>Price: {offer.current_price}</p>
                <p>Rating: {offer.rating}</p>
                <p>Release Date: {offer.release_date}</p>
              </div>
              <button
                onClick={() => handlePurchase(offer)}
                className="btn btn-success"
              >
                Buy Now
              </button>
              <Review
                rating={offer.rating}
                setRating={(newRating) => handleRatingChange(index, newRating)}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Offer;
