import { useEffect, useState } from "react";
import {
  BarChart3,
  Store,
  Package,
  CalendarDays,
  RefreshCw,
} from "lucide-react";

import {
  getMonthlySales,
  getTopStores,
  getCategoryPerformance,
  getDepartmentPerformance,
  getTopProducts,
  getWeekdaySales,
} from "../services/api";

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

function Analytics() {
  const [monthlySales, setMonthlySales] = useState([]);
  const [topStores, setTopStores] = useState([]);
  const [categories, setCategories] = useState([]);
  const [departments, setDepartments] = useState([]);
  const [products, setProducts] = useState([]);
  const [weekdays, setWeekdays] = useState([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadAnalytics = async () => {
      setLoading(true);
      setError(null);

      const results = await Promise.allSettled([
        getMonthlySales(),
        getTopStores(),
        getCategoryPerformance(),
        getDepartmentPerformance(),
        getTopProducts(),
        getWeekdaySales(),
      ]);

      const [
        monthlyResult,
        storesResult,
        categoryResult,
        departmentResult,
        productResult,
        weekdayResult,
      ] = results;

      if (monthlyResult.status === "fulfilled") {
        setMonthlySales(monthlyResult.value.data || []);
      }

      if (storesResult.status === "fulfilled") {
        setTopStores(storesResult.value.data || []);
      }

      if (categoryResult.status === "fulfilled") {
        setCategories(categoryResult.value.data || []);
      }

      if (departmentResult.status === "fulfilled") {
        setDepartments(departmentResult.value.data || []);
      }

      if (productResult.status === "fulfilled") {
        setProducts(productResult.value.data || []);
      }

      if (weekdayResult.status === "fulfilled") {
        setWeekdays(weekdayResult.value.data || []);
      }

      if (results.some((result) => result.status === "rejected")) {
        setError(
          "Some analytics data is temporarily unavailable."
        );
      }

      setLoading(false);
    };

    loadAnalytics();
  }, []);

  const monthlyChartData = monthlySales.map((item) => ({
    period: `${item.year}-${String(item.month).padStart(2, "0")}`,
    sales: item.total_sales,
  }));

  return (
    <div className="analytics-page">

      <div className="page-header">
        <div>
          <h1>Analytics</h1>
          <p>
            Explore historical sales and business performance.
          </p>
        </div>

        <div className="dashboard-status">
          <span className="status-dot"></span>
          Live Analytics
        </div>
      </div>

      {error && (
        <div className="error-banner">
          {error}
        </div>
      )}

      {loading ? (
        <div className="dashboard-card">
          <div className="loading-state">
            <RefreshCw size={20} className="spin" />
            Loading analytics...
          </div>
        </div>
      ) : (
        <>
          {/* Monthly Sales */}

          <div className="dashboard-card">

            <div className="card-header">
              <div>
                <h2>Monthly Sales</h2>
                <p>Historical monthly sales trend</p>
              </div>

              <BarChart3 size={20} />
            </div>

            <div className="chart-container">

              <ResponsiveContainer width="100%" height={360}>
                <LineChart data={monthlyChartData}>

                  <CartesianGrid strokeDasharray="3 3" />

                  <XAxis
                    dataKey="period"
                    interval={5}
                  />

                  <YAxis
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

            </div>

          </div>

          {/* Store + Category */}

          <div className="dashboard-grid">

            <div className="dashboard-card">

              <div className="card-header">
                <div>
                  <h2>Store Performance</h2>
                  <p>Total sales by store</p>
                </div>

                <Store size={20} />
              </div>

              <div className="chart-container">

                <ResponsiveContainer width="100%" height={320}>
                  <BarChart data={topStores}>

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis dataKey="store_id" />

                    <YAxis
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
                    />

                  </BarChart>
                </ResponsiveContainer>

              </div>

            </div>

            <div className="dashboard-card">

              <div className="card-header">
                <div>
                  <h2>Category Performance</h2>
                  <p>Total sales by category</p>
                </div>

                <Package size={20} />
              </div>

              <div className="chart-container">

                <ResponsiveContainer width="100%" height={320}>
                  <BarChart data={categories}>

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis dataKey="cat_id" />

                    <YAxis
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
                    />

                  </BarChart>
                </ResponsiveContainer>

              </div>

            </div>

          </div>

          {/* Department + Weekday */}

          <div className="dashboard-grid">

            <div className="dashboard-card">

              <div className="card-header">
                <div>
                  <h2>Department Performance</h2>
                  <p>Total sales by department</p>
                </div>

                <BarChart3 size={20} />
              </div>

              <div className="chart-container">

                <ResponsiveContainer width="100%" height={320}>
                  <BarChart data={departments}>

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis dataKey="dept_id" />

                    <YAxis
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
                    />

                  </BarChart>
                </ResponsiveContainer>

              </div>

            </div>

            <div className="dashboard-card">

              <div className="card-header">
                <div>
                  <h2>Weekday Sales</h2>
                  <p>Sales distribution by weekday</p>
                </div>

                <CalendarDays size={20} />
              </div>

              <div className="chart-container">

                <ResponsiveContainer width="100%" height={320}>
                  <BarChart data={weekdays}>

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis dataKey="weekday" />

                    <YAxis
                      tickFormatter={(value) =>
                        `${(value / 1000000).toFixed(1)}M`
                      }
                    />

                    <Tooltip
                      formatter={(value) =>
                        Number(value).toLocaleString()
                      }
                    />

                    <Bar
                      dataKey="total_sales"
                      fill="#2563eb"
                    />

                  </BarChart>
                </ResponsiveContainer>

              </div>

            </div>

          </div>

          {/* Top Products */}

          <div className="dashboard-card">

            <div className="card-header">
              <div>
                <h2>Top Products</h2>
                <p>Highest-performing products by total sales</p>
              </div>

              <Package size={20} />
            </div>

            <div className="analytics-table">

              <table>
                <thead>
                  <tr>
                    <th>Rank</th>
                    <th>Product</th>
                    <th>Total Sales</th>
                  </tr>
                </thead>

                <tbody>
                  {products.map((product, index) => (
                    <tr key={product.item_id}>
                      <td>{index + 1}</td>
                      <td>{product.item_id}</td>
                      <td>
                        {Number(
                          product.total_sales
                        ).toLocaleString()}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>

            </div>

          </div>
        </>
      )}

    </div>
  );
}

export default Analytics;