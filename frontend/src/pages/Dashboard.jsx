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
  getForecast,
  getMonthlySales,
  getSalesSummary,
  getTopStores,
  getCategoryPerformance,
} from "../services/api";

// import ReactMarkdown from "react-markdown";
import {
  LineChart,
  Line,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";


function Dashboard() {
  const [salesSummary, setSalesSummary] = useState(null);
  const [, setMonthlySales] = useState(null);
  const [monthlySalesData, setMonthlySalesData] = useState([]);
  const [forecast, setForecast] = useState(null);

  const [topStores, setTopStores] = useState([]);
  const [categoryPerformance, setCategoryPerformance] = useState([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadDashboard = async () => {
      setLoading(true);
      setError(null);

      const results = await Promise.allSettled([
        getSalesSummary(),
        getMonthlySales(),
        getForecast("What is the best forecasting model."),
        getTopStores(),
        getCategoryPerformance(),
      ]);

      const [
        summaryResult,
        monthlyResult,
        forecastResult,
        topStoresResult,
        categoryResult,
      ] = results;

      // -----------------------------
      // Sales Summary
      // -----------------------------
      if (summaryResult.status === "fulfilled") {
        setSalesSummary(summaryResult.value);
      } else {
        console.error(
          "Sales summary failed:",
          monthlyResult.reason,
        );

        setMonthlySales(null);
      }

      // -----------------------------
      // Monthly Sales
      // -----------------------------
      if (monthlyResult.status === "fulfilled") {
        setMonthlySales(monthlyResult.value);

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
      // Top Stores
      // -----------------------------
      if (topStoresResult.status === "fulfilled") {
        setTopStores(topStoresResult.value.data || []);
      } else {
        console.error(
          "Top stores failed:",
          topStoresResult.reason,
        );

        setTopStores([]);
      }   

      // -----------------------------
      // Category Performance
      // -----------------------------
      if (categoryResult.status === "fulfilled") {
        setCategoryPerformance(categoryResult.value.data || []);
      } else {
        console.error(
          "Category performance failed:",
          categoryResult.reason,
        );

        setCategoryPerformance([]);
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
          title="Total Sales"
          value={
            loading
              ? "..."
              : salesSummary?.data?.[0]?.total_sales != null
                ? `${(salesSummary.data[0].total_sales / 1000000).toFixed(1)}M`
                : "Unavailable"
          }
          description="Total sales value"
          icon={<TrendingUp size={20} />}
        />

        <MetricCard
          title="Sales Records"
          value={
            loading
              ? "..."
              : salesSummary?.data?.[0]?.total_records != null
                ? Number(
                    salesSummary.data[0].total_records
                  ).toLocaleString()
                : "Unavailable"
          }
          description="Records analyzed"
          icon={<ShoppingCart size={20} />}
        />

        <MetricCard
          title="Average Sale"
          value={
            loading
              ? "..."
              : salesSummary?.data?.[0]?.average_sales != null
                ? salesSummary.data[0].average_sales.toFixed(2)
                : "Unavailable"
          }
          description="Average sales value per record"
          icon={<Package size={20} />}
        />

        <MetricCard
          title="Stores"
          value="10"
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
      <div className="dashboard-grid">
        {/* Top Stores */}
        <div className="dashboard-card">
          <div className="card-header">
            <div>
              <h2>Top Performing Stores</h2>
              <p>Stores ranked by total sales value</p>
            </div>
            <Store size={20} />
          </div>

          <div className="chart-container">
            {loading ? (
              <div className="loading-state">
                Loading store performance...
              </div>
            ) : topStores.length > 0 ? (
              <ResponsiveContainer width="100%" height={320}>
                <BarChart
                  data={topStores}
                  margin={{
                    top: 10,
                    right: 20,
                    left: 10,
                    bottom: 10,
                  }}
                >
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="store_id" />
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
                  <Bar
                    dataKey="total_sales"
                    fill="#2563eb"
                    radius={[4, 4, 0, 0]}
                  />
                </BarChart>
              </ResponsiveContainer>
            ) : (
              <div className="loading-state">
                Store performance is temporarily unavailable.
              </div>
            )}
          </div>
        </div>

        {/* Category Performance */}
        <div className="dashboard-card">
          <div className="card-header">
            <div>
              <h2>Category Performance</h2>
              <p>Sales distribution across categories</p>
            </div>
            <Package size={20} />
          </div>

          <div className="chart-container">
            {loading ? (
              <div className="loading-state">
                Loading category performance...
              </div>
            ) : categoryPerformance.length > 0 ? (
              <ResponsiveContainer width="100%" height={320}>
                <BarChart
                  data={categoryPerformance}
                  margin={{
                    top: 10,
                    right: 20,
                    left: 10,
                    bottom: 10,
                  }}
                >
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="cat_id" />
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
                  <Bar
                    dataKey="total_sales"
                    fill="#2563eb"
                    radius={[4, 4, 0, 0]}
                  />
                </BarChart>
              </ResponsiveContainer>
            ) : (
              <div className="loading-state">
                Category performance is temporarily unavailable.
              </div>
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