import "./header.css"

const Header = () => {
  return (
    <header className="wz-header">
      <nav className="wz-nav wz-container">
        <div className="wz-nav__brand">
          <h2>WorkZen</h2>
        </div>

        <div className="wz-nav__links">
          <a href="/">Home</a>
          <a href="/freelancers">Find Freelancers</a>
          <a href="/projects">Projects</a>
          <a href="/about">About</a>
        </div>

        <div className="wz-nav__actions">
          <button className="wz-btn wz-btn--ghost">Log In</button>
          <button className="wz-btn wz-btn--primary">Sign Up</button>
        </div>
      </nav>
    </header>
  );
};

export default Header;