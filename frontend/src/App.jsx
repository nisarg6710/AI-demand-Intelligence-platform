import { BrowserRouter, Routes, Route } from "react-router-dom";

import Sidebar from "./components/Sidebar";
import Header from "./components/Header";

import Dashboard from "./pages/Dashboard";
import Forecasting from "./pages/Forecasting";
import Analytics from "./pages/Analytics";
import Chat from "./pages/Chat";
import Agents from "./pages/Agents";

function App() {
  return (
    <BrowserRouter>
      <div className="app">
        <Sidebar />

        <div className="main">
          <Header />

          <main className="content">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/forecasting" element={<Forecasting />} />
              <Route path="/analytics" element={<Analytics />} />
              <Route path="/chat" element={<Chat />} />
              <Route path="/agents" element={<Agents />} />
            </Routes>
          </main>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;