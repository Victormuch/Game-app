function Review({ rating, setRating }) {
  return (
    <div>
      {[1, 2, 3, 4, 5].map((star, index) => {
        return (
          <span
            key={index}
            className="star"
            style={{
              cursor: "pointer",
              color: rating >= star ? "gold" : "grey",
              fontSize: "35px",
            }}
            onClick={() => {
              setRating(star);
            }}
          >
            ★
          </span>
        );
      })}
    </div>
  );
}

export default Review;
