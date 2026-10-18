import { useEffect, useState } from "react";
import {
  Bar,
  BarChart,
  CartesianGrid,
  Legend,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import {
  BarChart3,
  Brain,
  RefreshCw,
  Send,
  TrendingUp,
} from "lucide-react";
import ReactMarkdown from "react-markdown";

import {
  getForecast,
  getHistoricalHoldout,
  getModelComparison,
  IS_PUBLIC_DEMO,
} from "../services/api";

const number = (value) => Number(value).toLocaleString(undefined, {
  maximumFractionDigits: 2,
});

function Forecasting() {
  const [question, setQuestion] = useState("What is the best forecasting model?");
  const [result, setResult] = useState(null);
  const [interactionLoading, setInteractionLoading] = useState(false);
  const [interactionError, setInteractionError] = useState(null);
  const [comparison, setComparison] = useState(null);
  const [holdout, setHoldout] = useState(null);
  const [dataLoading, setDataLoading] = useState(IS_PUBLIC_DEMO);
  const [dataError, setDataError] = useState(null);

  const exampleQuestions = [
    "What is the best forecasting model?",
    "Compare the forecasting models.",
    "What is the future demand forecast for the next 12 months?",
    "Which months have the highest forecasted demand?",
  ];

  useEffect(() => {
    if (!IS_PUBLIC_DEMO) {
      return undefined;
    }
    let active = true;
    Promise.allSettled([getModelComparison(), getHistoricalHoldout()]).then((results) => {
      if (!active) return;
      const [comparisonResult, holdoutResult] = results;
      if (comparisonResult.status === "fulfilled") {
        setComparison(comparisonResult.value);
      }
      if (holdoutResult.status === "fulfilled") {
        setHoldout(holdoutResult.value);
      }
      if (results.some((item) => item.status === "rejected")) {
        setDataError("Some recorded forecasting data could not be loaded. The demo service may be waking after idle time; please retry shortly.");
      }
      setDataLoading(false);
    });
    return () => { active = false; };
  }, []);

  const runDemoInteraction = async (forecastQuestion = question) => {
    if (!forecastQuestion.trim() || interactionLoading) return;
    setInteractionLoading(true);
    setInteractionError(null);
    try {
      setResult(await getForecast(forecastQuestion));
    } catch (err) {
      console.error("Demo forecast interaction failed:", err);
      setInteractionError(IS_PUBLIC_DEMO
        ? "The demo service did not respond. It may be starting after idle time; please retry shortly."
        : "Unable to retrieve forecasting intelligence. Please try again.");
      setResult(null);
    } finally {
      setInteractionLoading(false);
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    runDemoInteraction();
  };

  const handleExample = (example) => {
    setQuestion(example);
    runDemoInteraction(example);
  };

  const comparisonRows = comparison?.data || [];
  const holdoutRows = holdout?.data || [];

  return (
    <div className="forecasting-page">
      <div className="page-header">
        <div>
          <h1>Forecasting</h1>
          <p>{IS_PUBLIC_DEMO ? "Review recorded model benchmarks and a historical holdout evaluation." : "Explore the local forecasting service and ask questions about models and demand."}</p>
        </div>
        <div className="dashboard-status">
          <span className="status-dot"></span>
          {IS_PUBLIC_DEMO ? "Recorded Results" : "Forecast Intelligence"}
        </div>
      </div>

      {IS_PUBLIC_DEMO && <div className="dashboard-card">
        <div className="card-header">
          <div>
            <h2>Recorded Model Comparison</h2>
            <p>Existing classical model benchmark from {comparison?.source || "the repository benchmark artifact"}.</p>
          </div>
          <BarChart3 size={20} />
        </div>
        {dataLoading && !comparison ? (
          <div className="loading-state"><RefreshCw size={20} className="spin" /> Loading recorded benchmarks...</div>
        ) : comparisonRows.length ? (
          <>
            <div className="dashboard-grid">
              <div>
                <h3>Recorded error metrics</h3>
                <div className="chart-container">
                  <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={comparisonRows}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="model" />
                      <YAxis />
                      <Tooltip formatter={(value) => number(value)} />
                      <Legend />
                      <Bar dataKey="mae" name="MAE" fill="#2563eb" />
                      <Bar dataKey="rmse" name="RMSE" fill="#7c3aed" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>
              </div>
              <div>
                <h3>Recorded runtime</h3>
                <div className="chart-container">
                  <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={comparisonRows}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="model" />
                      <YAxis />
                      <Tooltip formatter={(value) => `${number(value)} s`} />
                      <Legend />
                      <Bar dataKey="train_time_s" name="Training (s)" fill="#0891b2" />
                      <Bar dataKey="predict_time_s" name="Prediction (s)" fill="#16a34a" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>
              </div>
            </div>
            <div className="table-container">
              <table>
                <thead><tr><th>Model</th><th>MAE</th><th>RMSE</th><th>MAPE</th><th>Train (s)</th><th>Predict (s)</th></tr></thead>
                <tbody>
                  {comparisonRows.map((row) => (
                    <tr key={row.model}>
                      <td>{row.model}</td><td>{number(row.mae)}</td><td>{number(row.rmse)}</td>
                      <td>{number(row.mape)}%</td><td>{Number(row.train_time_s).toFixed(6)}</td><td>{Number(row.predict_time_s).toFixed(6)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <p className="forecast-description">
              These are previously recorded benchmark results, not a live benchmark. MAPE values are unusually high and can be unreliable when actual values are zero or small; do not use MAPE alone to select a model.
            </p>
          </>
        ) : (
          <div className="empty-state">Recorded model comparison data is unavailable.</div>
        )}
      </div>}

      {IS_PUBLIC_DEMO && <div className="dashboard-card">
        <div className="card-header">
          <div>
            <h2>Historical holdout evaluation — not a future forecast</h2>
            <p>{holdout?.model_name || "ARIMAModel"} · {holdout?.date_range?.start || ""} to {holdout?.date_range?.end || ""} · daily aggregate item units</p>
          </div>
          <TrendingUp size={20} />
        </div>
        {dataLoading && !holdout ? (
          <div className="loading-state"><RefreshCw size={20} className="spin" /> Loading historical holdout...</div>
        ) : holdoutRows.length ? (
          <div className="chart-container">
            <ResponsiveContainer width="100%" height={360}>
              <LineChart data={holdoutRows}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="forecast_date" interval={Math.max(1, Math.floor(holdoutRows.length / 12))} />
                <YAxis />
                <Tooltip labelFormatter={(label) => `Date: ${label}`} formatter={(value) => `${number(value)} units`} />
                <Legend />
                <Line type="monotone" dataKey="actual" name="Actual" stroke="#2563eb" dot={false} />
                <Line type="monotone" dataKey="prediction" name="ARIMA prediction" stroke="#ea580c" dot={false} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        ) : (
          <div className="empty-state">Historical holdout data is unavailable.</div>
        )}
      </div>}

      {IS_PUBLIC_DEMO && dataError && <div className="error-banner">{dataError}</div>}

      <div className="dashboard-card forecast-query-card">
        <div className="card-header">
          <div>
            <h2>{IS_PUBLIC_DEMO ? "Forecasting Demo Interaction" : "Forecast Query"}</h2>
            <p>{IS_PUBLIC_DEMO
              ? "This form returns a fixed explanatory demo response. It does not run a model, query MySQL, or call Gemini."
              : "Ask questions about forecasting models and future demand in the local production application."}</p>
          </div>
          <Brain size={20} />
        </div>
        <form onSubmit={handleSubmit} className="forecast-form">
          <textarea value={question} onChange={(event) => setQuestion(event.target.value)} placeholder={IS_PUBLIC_DEMO ? "Enter a demo question..." : "Ask a forecasting question..."} rows={4} className="forecast-input" />
          <button type="submit" className="primary-button" disabled={interactionLoading}>
            {interactionLoading ? <><RefreshCw size={18} className="spin" /> {IS_PUBLIC_DEMO ? "Waiting for service..." : "Analyzing..."}</> : <><Send size={18} /> {IS_PUBLIC_DEMO ? "Show Demo Response" : "Run Forecast"}</>}
          </button>
        </form>
        <div className="example-questions">
          <span className="example-label">Example questions</span>
          <div className="example-question-list">
            {exampleQuestions.map((example) => (
              <button key={example} type="button" className="example-question" onClick={() => handleExample(example)} disabled={interactionLoading}>{example}</button>
            ))}
          </div>
        </div>
        {interactionError && <div className="error-banner">{interactionError}</div>}
        {interactionLoading ? (
          <div className="loading-state">{IS_PUBLIC_DEMO ? "The Render demo service may be waking after idle time..." : "Running forecasting analysis..."}</div>
        ) : result?.response ? (
          <div className="forecast-result"><div className="markdown-content"><ReactMarkdown>{result.response}</ReactMarkdown></div></div>
        ) : null}
      </div>
    </div>
  );
}

export default Forecasting;
