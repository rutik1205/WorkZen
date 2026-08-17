import "./home.css"

const categories = [
  { name: "Design & Creative", count: "1,240 projects" },
  { name: "Development & IT", count: "2,860 projects" },
  { name: "Writing & Content", count: "980 projects" },
  { name: "Marketing", count: "740 projects" },
  { name: "Video & Animation", count: "410 projects" },
  { name: "Admin & Support", count: "560 projects" },
];

const freelancers = [
  { name: "Aditi Rao", role: "Product Designer", rate: "₹1,800/hr", rating: "4.9" },
  { name: "Marcus Chen", role: "Full-Stack Developer", rate: "₹2,400/hr", rating: "5.0" },
  { name: "Priya Nair", role: "Content Strategist", rate: "₹1,200/hr", rating: "4.8" },
  { name: "Daniel Osei", role: "Motion Designer", rate: "₹1,600/hr", rating: "4.9" },
];

const Home = () => {
  return (
    <main>
      {/* Hero */}
      <section className="wz-hero">
        <div className="wz-container wz-hero__inner">
          <span className="wz-eyebrow">WorkZen</span>
          <h1>Get your project done by vetted freelancers</h1>
          <p className="wz-hero__sub">
            Post a project, review proposals, and hire someone who's right for
            the job — with payment held safely until the work is done.
          </p>
          <div className="wz-hero__actions">
            <button className="wz-btn wz-btn--primary wz-btn--lg">Post a Project</button>
            <a href="/jobs" className="wz-hero__secondary">Looking for work instead? →</a>
          </div>
        </div>
      </section>

      {/* Trust strip */}
      <section className="wz-trust">
        <div className="wz-container wz-trust__row">
          <div className="wz-trust__item">
            <span className="wz-eyebrow">Verified</span>
            <p>Every profile is identity-checked</p>
          </div>
          <div className="wz-trust__item">
            <span className="wz-eyebrow">Protected</span>
            <p>Payment held in escrow until you approve the work</p>
          </div>
          <div className="wz-trust__item">
            <span className="wz-eyebrow">Supported</span>
            <p>Dispute resolution on every project</p>
          </div>
        </div>
      </section>

      {/* Categories */}
      <section className="wz-section">
        <div className="wz-container">
          <h2>Browse by category</h2>
          <div className="wz-categories">
            {categories.map((cat) => (
              <a href="#" className="wz-category-card" key={cat.name}>
                <h4>{cat.name}</h4>
                <span className="wz-figure wz-text-soft">{cat.count}</span>
              </a>
            ))}
          </div>
        </div>
      </section>

      {/* How it works */}
      <section className="wz-section wz-section--tint">
        <div className="wz-container">
          <h2>How it works</h2>
          <div className="wz-how">
            <div className="wz-how__track">
              <span className="wz-eyebrow">As a Client</span>
              <ol className="wz-how__steps">
                <li><span className="wz-figure">01</span> Post your project and budget</li>
                <li><span className="wz-figure">02</span> Review proposals from freelancers</li>
                <li><span className="wz-figure">03</span> Hire and pay when work is approved</li>
              </ol>
            </div>
            <div className="wz-how__track">
              <span className="wz-eyebrow">As a Freelancer</span>
              <ol className="wz-how__steps">
                <li><span className="wz-figure">01</span> Create your profile and portfolio</li>
                <li><span className="wz-figure">02</span> Send proposals to open projects</li>
                <li><span className="wz-figure">03</span> Get paid once the client approves</li>
              </ol>
            </div>
          </div>
        </div>
      </section>

      {/* Featured freelancers */}
      <section className="wz-section">
        <div className="wz-container">
          <h2>Featured freelancers</h2>
          <div className="wz-freelancers">
            {freelancers.map((f) => (
              <div className="wz-freelancer-card" key={f.name}>
                <div className="wz-freelancer-card__avatar" />
                <h4>{f.name}</h4>
                <p className="wz-text-soft">{f.role}</p>
                <div className="wz-freelancer-card__meta">
                  <span className="wz-figure">{f.rate}</span>
                  <span className="wz-figure">★ {f.rating}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Closing CTA */}
      <section className="wz-cta">
        <div className="wz-container wz-cta__inner">
          <h2>Ready to get started?</h2>
          <button className="wz-btn wz-btn--primary wz-btn--lg">Post a Project</button>
        </div>
      </section>
    </main>
  );
};

export default Home;