import { useEffect, useState } from "react";
import {
  TrendingUp,
  ShoppingCart,
  Package,
  Store,
  MessageSquare,
  BarChart3,
  ArrowRight,
} from "lucide-react";

import MetricCard from "../components/MetricCard";
import {
  getAnalytics,
  getForecast,
  getMonthlySales,
} from "../services/api";

// import ReactMarkdown from "react-markdown";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";


function Dashboard() {
  const [salesSummary, setSalesSummary] = useState(null);
  const [monthlySales, setMonthlySales] = useState(null);
  const [monthlySalesData, setMonthlySalesData] = useState([]);
  const [forecast, setForecast] = useState(null);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadDashboard = async () => {
      setLoading(true);
      setError(null);

      const results = await Promise.allSettled([
        getAnalytics("Give me a sales summary."),
        getMonthlySales(),
        getForecast("What is the best forecasting model."),
      ]);

      const [
        summaryResult,
        monthlyResult,
        forecastResult,
      ] = results;

      // -----------------------------
      // Sales Summary
      // -----------------------------
      if (summaryResult.status === "fulfilled") {
        setSalesSummary(summaryResult.value);

        const chartData = monthlyResult.value.data.map((item) => ({
          period: `${item.year}-${String(item.month).padStart(2, "0")}`,
          sales: item.total_sales,
        }));

        setMonthlySalesData(chartData);
      } else {
        console.error(
          "Monthly sales failed:",
          monthlyResult.reason,
        );

        setMonthlySales(null);
        setMonthlySalesData([]);
      }

      // -----------------------------
      // Monthly Sales
      // -----------------------------
      if (monthlyResult.status === "fulfilled") {
        setMonthlySales(monthlyResult.value);
      } else {
        console.error(
          "Monthly sales failed:",
          monthlyResult.reason,
        );

        setMonthlySales(null);
      }

      // -----------------------------
      // Forecast
      // -----------------------------
      if (forecastResult.status === "fulfilled") {
        setForecast(forecastResult.value);
      } else {
        console.error(
          "Forecast failed:",
          forecastResult.reason,
        );

        setForecast(null);
      }

      // -----------------------------
      // Overall Status
      // -----------------------------
      const failedRequests = results.filter(
        (result) => result.status === "rejected",
      );

      if (failedRequests.length > 0) {
        setError(
          "Some intelligence services are temporarily unavailable. Available data is still being displayed.",
        );
      }

      setLoading(false);
    };

    loadDashboard();
  }, []);

  return (
    <div className="dashboard">

      {/* =========================
          Page Header
      ========================= */}

      <div className="page-header">
        <div>
          <h1>Dashboard</h1>

          <p>
            Overview of your retail demand intelligence platform.
          </p>
        </div>

        <div className="dashboard-status">
          <span className="status-dot"></span>
          Live Intelligence
        </div>
      </div>

      {/* =========================
          Error
      ========================= */}

      {error && (
        <div className="error-banner">
          {error}
        </div>
      )}

      {/* =========================
          KPI Cards
      ========================= */}

      <div className="metrics-grid">

        <MetricCard
          title="Total Revenue"
          value={
            loading
              ? "..."
              : "$65.7M"
          }
          description="Historical revenue"
          icon={<TrendingUp size={20} />}
        />

        <MetricCard
          title="Total Sales"
          value={
            loading
              ? "..."
              : "58.3M"
          }
          description="Sales records analyzed"
          icon={<ShoppingCart size={20} />}
        />

        <MetricCard
          title="Active Products"
          value={
            loading
              ? "..."
              : "3,049"
          }
          description="Products in catalog"
          icon={<Package size={20} />}
        />

        <MetricCard
          title="Stores"
          value={
            loading
              ? "..."
              : "10"
          }
          description="Retail locations"
          icon={<Store size={20} />}
        />

      </div>

      {/* =========================
          Main Dashboard Grid
      ========================= */}

      <div className="dashboard-grid">

        {/* Monthly Sales */}

        <div className="dashboard-card sales-card">

          <div className="card-header">

            <div>
              <h2>Monthly Sales</h2>

              <p>
                Historical revenue trend
              </p>
            </div>

            <BarChart3 size={20} />

          </div>

          <div className="chart-container">

            {loading ? (

              <div className="loading-state">
                Loading analytics...
              </div>
            ) : monthlySalesData.length > 0 ? (

              <ResponsiveContainer width="100%" height={320}>

                <LineChart
                  data={monthlySalesData}
                  margin={{
                    top: 10,
                    right: 20,
                    left: 10,
                    bottom: 10,
                  }}
                >

                  <CartesianGrid strokeDasharray="3 3" />

                  <XAxis
                    dataKey="period"
                    tick={{ fontSize: 12 }}
                    interval={5}
                  />

                  <YAxis
                    tick={{ fontSize: 12 }}
                    tickFormatter={(value) =>
                      `$${(value / 1000000).toFixed(1)}M`
                    }
                  />

                  <Tooltip
                    formatter={(value) =>
                      `$${Number(value).toLocaleString()}`
                    }
                  />

                  <Line
                    type="monotone"
                    dataKey="sales"
                    stroke="#2563eb"
                    strokeWidth={2}
                    dot={false}
                  />

                </LineChart>

              </ResponsiveContainer>

            ) : (

              <div className="loading-state">
                Monthly sales data is temporarily unavailable.
              </div>

            )}

          </div>

        </div>

        {/* Forecast */}

        <div className="dashboard-card">

          <div className="card-header">

            <div>
              <h2>Forecast Intelligence</h2>

              <p>
                Current forecasting assessment
              </p>
            </div>

            <TrendingUp size={20} />

          </div>

          <div className="forecast-summary">

            {loading ? (
              <div className="loading-state">
                Loading forecast...
              </div>
            ) : (
              <>
                <div className="forecast-status">
                  Forecast Model
                </div>

                <div className="forecast-model">
                  {forecast?.response ? "Prophet" : "Unavailable"}
                </div>

                <div className="forecast-description">
                  {forecast?.response
                    ? "Forecast evaluation is available through the forecasting service."
                    : "Forecast service is temporarily unavailable. Please try again later."}
                </div>
              </>
            )}

          </div>

        </div>

      </div>

      {/* =========================
          Quick Actions
      ========================= */}

      <div className="dashboard-card quick-actions">

        <div className="card-header">

          <div>
            <h2>Quick Actions</h2>

            <p>
              Explore the intelligence platform
            </p>
          </div>

        </div>

        <div className="actions-grid">

          <a
            href="/chat"
            className="action-card"
          >
            <MessageSquare size={22} />

            <div>
              <h3>Ask AI</h3>

              <p>
                Ask a natural-language business question.
              </p>
            </div>

            <ArrowRight size={18} />

          </a>

          <a
            href="/analytics"
            className="action-card"
          >
            <BarChart3 size={22} />

            <div>
              <h3>Explore Analytics</h3>

              <p>
                Analyze historical sales and business trends.
              </p>
            </div>

            <ArrowRight size={18} />

          </a>

          <a
            href="/forecasting"
            className="action-card"
          >
            <TrendingUp size={22} />

            <div>
              <h3>View Forecasts</h3>

              <p>
                Explore forecasting models and predictions.
              </p>
            </div>

            <ArrowRight size={18} />

          </a>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;