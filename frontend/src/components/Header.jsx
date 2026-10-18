import { IS_PUBLIC_DEMO } from "../services/api";

function Header() {
  return (
    <header className="header">
      <div>
        <h1>AI Demand Intelligence Platform</h1>
        <p>Retail demand forecasting & business intelligence</p>
      </div>

      <div className="api-status">
        <span className="status-dot"></span>
        <span>{IS_PUBLIC_DEMO ? "Public Demo" : "API Online"}</span>
      </div>
    </header>
  );
}

export default Header;
