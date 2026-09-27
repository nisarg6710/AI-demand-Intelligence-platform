import { useState } from "react";
import {
  TrendingUp,
  Brain,
  Send,
  RefreshCw,
  BarChart3,
} from "lucide-react";
import ReactMarkdown from "react-markdown";

import { getForecast } from "../services/api";

function Forecasting() {
  const [question, setQuestion] = useState(
    "What is the best forecasting model?"
  );

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const exampleQuestions = [
    "What is the best forecasting model?",
    "Compare the forecasting models.",
    "What is the future demand forecast for the next 12 months?",
    "Which months have the highest forecasted demand?",
  ];

  const runForecast = async (forecastQuestion = question) => {
    if (!forecastQuestion.trim()) {
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await getForecast(forecastQuestion);

      setResult(response);
    } catch (err) {
      console.error("Forecast request failed:", err);

      setError(
        "Unable to retrieve forecasting intelligence. Please try again."
      );
      setResult(null);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    runForecast();
  };

  const handleExample = (example) => {
    setQuestion(example);
    runForecast(example);
  };

  return (
    <div className="forecasting-page">

      {/* Page Header */}
      <div className="page-header">
        <div>
          <h1>Forecasting</h1>
          <p>
            Explore demand forecasts and evaluate forecasting models.
          </p>
        </div>

        <div className="dashboard-status">
          <span className="status-dot"></span>
          Forecast Intelligence
        </div>
      </div>

      {/* Overview Cards */}
      <div className="metrics-grid">

        <div className="metric-card">
          <div className="metric-card-header">
            <span className="metric-title">
              Forecasting Service
            </span>

            <div className="metric-icon">
              <TrendingUp size={20} />
            </div>
          </div>

          <div className="metric-value">
            Online
          </div>

          <div className="metric-description">
            Forecasting pipeline available
          </div>
        </div>

        <div className="metric-card">
          <div className="metric-card-header">
            <span className="metric-title">
              Forecast Models
            </span>

            <div className="metric-icon">
              <BarChart3 size={20} />
            </div>
          </div>

          <div className="metric-value">
            Multiple
          </div>

          <div className="metric-description">
            Models evaluated by the forecasting pipeline
          </div>
        </div>

        <div className="metric-card">
          <div className="metric-card-header">
            <span className="metric-title">
              AI Analysis
            </span>

            <div className="metric-icon">
              <Brain size={20} />
            </div>
          </div>

          <div className="metric-value">
            Gemini
          </div>

          <div className="metric-description">
            Natural-language forecasting intelligence
          </div>
        </div>

      </div>

      {/* Forecast Query */}
      <div className="dashboard-card forecast-query-card">

        <div className="card-header">
          <div>
            <h2>Forecast Query</h2>
            <p>
              Ask questions about forecasting models and future demand.
            </p>
          </div>

          <TrendingUp size={20} />
        </div>

        <form onSubmit={handleSubmit} className="forecast-form">

          <textarea
            value={question}
            onChange={(event) =>
              setQuestion(event.target.value)
            }
            placeholder="Ask a forecasting question..."
            rows={4}
            className="forecast-input"
          />

          <button
            type="submit"
            className="primary-button"
            disabled={loading}
          >
            {loading ? (
              <>
                <RefreshCw size={18} className="spin" />
                Analyzing...
              </>
            ) : (
              <>
                <Send size={18} />
                Run Forecast
              </>
            )}
          </button>

        </form>

        <div className="example-questions">

          <span className="example-label">
            Example questions
          </span>

          <div className="example-question-list">

            {exampleQuestions.map((example) => (
              <button
                key={example}
                type="button"
                className="example-question"
                onClick={() => handleExample(example)}
                disabled={loading}
              >
                {example}
              </button>
            ))}

          </div>

        </div>

      </div>

      {/* Error */}
      {error && (
        <div className="error-banner">
          {error}
        </div>
      )}

      {/* Forecast Result */}
      <div className="dashboard-card forecast-result-card">

        <div className="card-header">

          <div>
            <h2>Forecast Intelligence</h2>

            <p>
              AI-generated analysis from the forecasting pipeline.
            </p>
          </div>

          <Brain size={20} />

        </div>

        {loading ? (
          <div className="loading-state">
            <RefreshCw size={20} className="spin" />

            <span>
              Running forecasting analysis...
            </span>
          </div>
        ) : result?.response ? (
          <div className="forecast-result">

            {result.selected_action && (
              <div className="forecast-action">

                <span>
                  Selected forecasting action
                </span>

                <strong>
                  {result.selected_action}
                </strong>

              </div>
            )}

            <div className="markdown-content">
              <ReactMarkdown>
                {result.response}
              </ReactMarkdown>
            </div>

          </div>
        ) : (
          <div className="empty-state">

            <TrendingUp size={32} />

            <h3>
              No forecast analysis yet
            </h3>

            <p>
              Ask a forecasting question above to generate
              demand intelligence.
            </p>

          </div>
        )}

      </div>

    </div>
  );
}

export default Forecasting;