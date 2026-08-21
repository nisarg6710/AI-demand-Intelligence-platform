import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  TrendingUp,
  BarChart3,
  MessageSquare,
  Bot,
} from "lucide-react";

const navigation = [
  {
    name: "Dashboard",
    path: "/",
    icon: LayoutDashboard,
  },
  {
    name: "Forecasting",
    path: "/forecasting",
    icon: TrendingUp,
  },
  {
    name: "Analytics",
    path: "/analytics",
    icon: BarChart3,
  },
  {
    name: "Chat",
    path: "/chat",
    icon: MessageSquare,
  },
  {
    name: "Agents",
    path: "/agents",
    icon: Bot,
  },
];

function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <div className="brand-icon">📊</div>

        <div>
          <h2>Demand Intelligence</h2>
          <span>AI Platform</span>
        </div>
      </div>

      <nav className="sidebar-nav">
        {navigation.map((item) => {
          const Icon = item.icon;

          return (
            <NavLink
              key={item.path}
              to={item.path}
              end={item.path === "/"}
              className={({ isActive }) =>
                `nav-item ${isActive ? "active" : ""}`
              }
            >
              <Icon size={19} />
              <span>{item.name}</span>
            </NavLink>
          );
        })}
      </nav>

      <div className="sidebar-footer">
        <span>AI Demand Intelligence</span>
        <small>v10.0.0</small>
      </div>
    </aside>
  );
}

export default Sidebar;