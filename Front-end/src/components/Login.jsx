import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

function Login() {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const { username, email, password } = formData;
    if (username && email && password) {
     
      navigate(`/home?username=${encodeURIComponent(username)}`);
    } else {
      alert("Please fill in all the fields.");
    }
  };

  return (
    <div className="d-flex justify-content-center align-items-center bg-dark vh-100">
      <div className="bg-secondary p-4 rounded w-50">
        <form onSubmit={handleSubmit}>
          <h2 className="mb-4 text-center text-light">
            Welcome to Arcadin realm games
          </h2>
          <div className="mb-3">
            <label htmlFor="username" className="form-label text-light">
              Username
            </label>
            <input
              type="text"
              id="username"
              name="username"
              placeholder="Enter your Username"
              className="form-control"
              value={formData.username}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-3">
            <label htmlFor="email" className="form-label text-light">
              Email
            </label>
            <input
              type="email"
              id="email"
              name="email"
              placeholder="Enter your Email"
              className="form-control"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-3">
            <label htmlFor="password" className="form-label text-light">
              Password
            </label>
            <input
              type="password"
              id="password"
              name="password"
              placeholder="Enter your Password"
              className="form-control"
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-3 d-grid">
            <button className="btn btn-success btn-lg" type="submit">
              Log in
            </button>
          </div>
          <p className="mb-3 text-center text-light">
            By logging in, you agree to our terms and policies
          </p>
          <div className="d-grid">
            <Link
              to="/signup"
              className="btn btn-outline-light btn-lg"
              type="button"
            >
              Create Account
            </Link>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Login;
