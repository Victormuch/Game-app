function Login() {
  return (
    <div className="d-flex justify-content-center align-items-center bg-dark vh-100">
      <div className="bg-secondary p-4 rounded w-50">
        <form>
          <h2 className="mb-4 text-center text-light">
            Welcome to Arcadin realm games
          </h2>
          <div className="mb-3">
            <label htmlFor="email" className="form-label text-light">
              Email
            </label>
            <input
              type="email"
              id="email"
              placeholder="Enter your Email"
              className="form-control"
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
              placeholder="Enter your Password"
              className="form-control"
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
            <button className="btn btn-outline-light btn-lg" type="button">
              Create Account
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Login;
