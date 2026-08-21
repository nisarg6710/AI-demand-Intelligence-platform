import { useEffect, useState } from "react";

import {
  BarChart3,
  TrendingUp,
  Send,
} from "lucide-react";

import ReactMarkdown from "react-markdown";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import {
  getAnalytics,
  getMonthlySales,
} from "../services/api";


function Analytics() {

  const [question, setQuestion] = useState(
    "Show me the monthly sales trend."
  );

  const [analyticsResult, setAnalyticsResult] = useState(null);

  const [monthlySales, setMonthlySales] = useState([]);

  const [loading, setLoading] = useState(false);

  const [chartLoading, setChartLoading] = useState(true);

  const [error, setError] = useState(null);


  // =========================
  // Load Monthly Sales
  // =========================

  useEffect(() => {

    const loadMonthlySales = async () => {

      try {

        setChartLoading(true);

        const result = await getMonthlySales();

        setMonthlySales(result.data || []);

      } catch (err) {

        console.error(
          "Monthly sales loading error:",
          err
        );

        setError(
          "Unable to load monthly sales data."
        );

      } finally {

        setChartLoading(false);

      }

    };

    loadMonthlySales();

  }, []);


  // =========================
  // Ask Analytics Agent
  // =========================

  const handleAnalyze = async () => {

    if (!question.trim()) {
      return;
    }

    try {

      setLoading(true);

      setError(null);

      const result = await getAnalytics(
        question
      );

      setAnalyticsResult(result);

    } catch (err) {

      console.error(
        "Analytics request failed:",
        err
      );

      setAnalyticsResult(null);

      setError(
        "Unable to analyze the question. Please try again."
      );

    } finally {

      setLoading(false);

    }

  };


  // =========================
  // Chart Data
  // =========================

  const chartData = monthlySales.map(
    (item) => ({
      period:
        `${item.year}-${String(item.month).padStart(2, "0")}`,

      sales: item.total_sales,
    })
  );


  return (

    <div className="analytics-page">

      {/* =========================
          Page Header
      ========================= */}

      <div className="page-header">

        <div>

          <h1>Analytics</h1>

          <p>
            Explore historical sales,
            trends and business performance.
          </p>

        </div>

        <div className="dashboard-status">

          <span className="status-dot"></span>

          Business Intelligence

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
          Analytics Question
      ========================= */}

      <div className="dashboard-card analytics-question-card">

        <div className="card-header">

          <div>

            <h2>
              Ask an Analytics Question
            </h2>

            <p>
              Use natural language to explore
              your retail data.
            </p>

          </div>

          <BarChart3 size={20} />

        </div>


        <div className="analytics-input-area">

          <textarea
            value={question}
            onChange={(e) =>
              setQuestion(e.target.value)
            }
            placeholder="Ask a business analytics question..."
            rows={4}
          />

          <button
            className="analyze-button"
            onClick={handleAnalyze}
            disabled={loading}
          >

            <Send size={16} />

            {loading
              ? "Analyzing..."
              : "Analyze"}

          </button>

        </div>

      </div>


      {/* =========================
          Monthly Sales
      ========================= */}

      <div className="dashboard-card analytics-chart-card">

        <div className="card-header">

          <div>

            <h2>
              Monthly Sales Trend
            </h2>

            <p>
              Historical monthly sales from
              the retail data warehouse.
            </p>

          </div>

          <TrendingUp size={20} />

        </div>


        <div className="analytics-chart">

          {chartLoading ? (

            <div className="loading-state">

              Loading monthly sales...

            </div>

          ) : chartData.length > 0 ? (

            <ResponsiveContainer
              width="100%"
              height={350}
            >

              <LineChart
                data={chartData}
                margin={{
                  top: 10,
                  right: 20,
                  left: 10,
                  bottom: 10,
                }}
              >

                <CartesianGrid
                  strokeDasharray="3 3"
                />

                <XAxis
                  dataKey="period"
                  tick={{
                    fontSize: 11,
                  }}
                  interval={5}
                />

                <YAxis
                  tick={{
                    fontSize: 11,
                  }}
                  tickFormatter={(value) =>
                    `$${(
                      value / 1000000
                    ).toFixed(1)}M`
                  }
                />

                <Tooltip
                  formatter={(value) =>
                    `$${Number(
                      value
                    ).toLocaleString()}`
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

              Monthly sales data unavailable.

            </div>

          )}

        </div>

      </div>


      {/* =========================
          AI Analytics Result
      ========================= */}

      <div className="dashboard-card analytics-result-card">

        <div className="card-header">

          <div>

            <h2>
              AI Analytics Insight
            </h2>

            <p>
              Business interpretation generated
              by the Analytics Agent.
            </p>

          </div>

          <BarChart3 size={20} />

        </div>


        <div className="analytics-result">

          {!analyticsResult && !loading && (

            <div className="empty-state">

              Ask an analytics question above
              to receive an AI-powered analysis.

            </div>

          )}


          {loading && (

            <div className="loading-state">

              Analyzing business data...

            </div>

          )}


          {analyticsResult?.response && (

            <div className="result-content">

              <ReactMarkdown>

                {analyticsResult.response}

              </ReactMarkdown>

            </div>

          )}

        </div>

      </div>

    </div>

  );

}


export default Analytics;