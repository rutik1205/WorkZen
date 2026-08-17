import "./footer.css"

const Footer = () => {
  return (
    <footer className="wz-footer">
      <div className="wz-footer__top wz-container">
        <div className="wz-footer__brand">
          <h2>WorkZen</h2>
          <p>Connect with talented freelancers and get your work done.</p>
        </div>

        <div className="wz-footer__col">
          <h3>For Clients</h3>
          <a href="/freelancers">Find Freelancers</a>
          <a href="/projects">Post a Project</a>
          <a href="/how-it-works">How It Works</a>
        </div>

        <div className="wz-footer__col">
          <h3>For Freelancers</h3>
          <a href="/jobs">Find Jobs</a>
          <a href="/profile">Create Profile</a>
          <a href="/dashboard">Dashboard</a>
        </div>

        <div className="wz-footer__col">
          <h3>Company</h3>
          <a href="/about">About Us</a>
          <a href="/contact">Contact</a>
          <a href="/privacy">Privacy Policy</a>
        </div>
      </div>

      <div className="wz-footer__bottom wz-container">
        <p>© 2026 WorkZen. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;