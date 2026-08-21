function Header() {
  return (
    <header className="header">
      <div>
        <h1>AI Demand Intelligence Platform</h1>
        <p>Retail demand forecasting & business intelligence</p>
      </div>

      <div className="api-status">
        <span className="status-dot"></span>
        <span>API Online</span>
      </div>
    </header>
  );
}

export default Header;