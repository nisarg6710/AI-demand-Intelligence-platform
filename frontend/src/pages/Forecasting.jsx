import { useState } from "react";
import {
  TrendingUp,
  Send,
  CheckCircle2,
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


  const handleForecast = async () => {
    if (!question.trim()) {
      return;
    }

    try {
      setLoading(true);
      setError(null);
      setResult(null);

      const response = await getForecast(
        question.trim()
      );

      setResult(response);

    } catch (err) {
      console.error("Forecasting error:", err);

      setError(
        "Unable to generate the forecast analysis. Please try again."
      );

    } finally {
      setLoading(false);
    }
  };


  return (
    <div className="forecasting-page">

      {/* =========================
          Page Header
      ========================= */}

      <div className="page-header">

        <div>

          <h1>Forecasting</h1>

          <p>
            Explore demand forecasting models and predictions.
          </p>

        </div>

        <div className="dashboard-status">

          <span className="status-dot"></span>

          Forecast Intelligence

        </div>

      </div>


      {/* =========================
          Question Card
      ========================= */}

      <div className="dashboard-card forecasting-question-card">

        <div className="card-header">

          <div>

            <h2>
              Ask a Forecasting Question
            </h2>

            <p>
              Use natural language to explore demand forecasting.
            </p>

          </div>

          <TrendingUp size={20} />

        </div>


        <div className="forecast-input-area">

          <textarea
            value={question}
            onChange={(event) =>
              setQuestion(event.target.value)
            }
            placeholder="e.g. Which forecasting model performs best?"
            rows={4}
          />

          <button
            className="forecast-button"
            onClick={handleForecast}
            disabled={loading || !question.trim()}
          >

            <Send size={17} />

            {loading
              ? "Analyzing..."
              : "Analyze Forecast"}

          </button>

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
          Loading
      ========================= */}

      {loading && (

        <div className="dashboard-card forecast-result-card">

          <div className="forecast-loading">

            <div className="forecast-loading-icon">
              <TrendingUp size={20} />
            </div>

            <div>

              <strong>
                Generating forecasting analysis
              </strong>

              <p>
                The forecasting agent is analyzing the request.
              </p>

            </div>

          </div>

        </div>

      )}


      {/* =========================
          Forecast Result
      ========================= */}

      {result && !loading && (

        <div className="dashboard-card forecast-result-card">

          <div className="card-header">

            <div>

              <h2>
                Forecast Assessment
              </h2>

              <p>
                AI-powered forecasting analysis.
              </p>

            </div>

            <CheckCircle2
              size={20}
              className="forecast-success-icon"
            />

          </div>


          {/* =========================
              Request Summary
          ========================= */}

          <div className="forecast-request-summary">

            <div className="forecast-result-label">
              Question
            </div>

            <div className="forecast-question">
              {result.question || question}
            </div>

          </div>


          {/* =========================
              Selected Action
          ========================= */}

          <div className="forecast-action">

            <div className="forecast-result-label">
              Selected Forecast Action
            </div>

            <div className="forecast-action-value">
              {result.selected_action}
            </div>

          </div>


          {/* =========================
              AI Response
          ========================= */}

          <div className="forecast-response">

            <div className="forecast-result-label">
              AI Analysis
            </div>

            <div className="forecast-response-content">

              <ReactMarkdown>
                {result.response}
              </ReactMarkdown>

            </div>

          </div>

        </div>

      )}

    </div>
  );
}


export default Forecasting;