import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

function Upcoming() {
  const [upcoming, setUpcoming] = useState([]); 


useEffect(() => {
  fetch("http://127.0.0.1:8000/coming1")
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      console.log("Fetched data:", data);
      setUpcoming(data.coming1);
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}, []);

  return (
    <div>
      <Link to="/offer" className="btn btn-back btn-light">
        Back
      </Link>
      <div className="cards-container">
        {upcoming.map((game) => (
          <div key={game.id} className="card">
            <img src={game.image_url} alt={game.title} />
            <div className="card-body">
              <h3>{game.title}</h3>
              <p>Release Date: {game.release_date}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Upcoming;
