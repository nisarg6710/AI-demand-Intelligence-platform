import { useState } from "react";

import {
  MessageSquare,
  Send,
  Bot,
  Sparkles,
} from "lucide-react";

import ReactMarkdown from "react-markdown";

import { getChat } from "../services/api";


function Chat() {
  const [question, setQuestion] = useState(
    "What are the most important insights from the retail data?"
  );

  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);


  const exampleQuestions = [
    "Give me a sales summary.",
    "Which stores are performing best?",
    "Show me sales by weekday.",
    "What are the most important insights from the retail data?",
  ];


  const handleAsk = async () => {

    if (!question.trim() || loading) {
      return;
    }

    setLoading(true);
    setError(null);
    setResponse(null);

    try {

      const result = await getChat(question);

      console.log("CHAT RESPONSE:", result);

      if (!result.success) {
        throw new Error(
          result.error || "The AI assistant could not process your question."
        );
      }

      setResponse(result);

    } catch (err) {

      console.error("Chat request failed:", err);

      setError(
        err.response?.data?.detail ||
        err.message ||
        "Unable to get a response from the AI assistant."
      );

    } finally {

      setLoading(false);

    }
  };


  const handleExampleClick = (example) => {

    if (loading) {
      return;
    }

    setQuestion(example);
    setError(null);

  };


  return (
    <div className="chat-page">

      {/* =========================
          Page Header
      ========================= */}

      <div className="page-header">

        <div>

          <h1>AI Chat</h1>

          <p>
            Ask natural-language questions about your retail business.
          </p>

        </div>

        <div className="dashboard-status">

          <span className="status-dot"></span>

          AI Assistant

        </div>

      </div>


      {/* =========================
          Question Card
      ========================= */}

      <div className="dashboard-card chat-question-card">

        <div className="card-header">

          <div>

            <h2>
              Ask the AI Assistant
            </h2>

            <p>
              Get grounded business insights from your retail data.
            </p>

          </div>

          <MessageSquare size={20} />

        </div>


        <textarea
          className="chat-input"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {

            if (
              e.key === "Enter" &&
              (e.ctrlKey || e.metaKey)
            ) {
              handleAsk();
            }

          }}
          placeholder="Ask a question about your business data..."
          rows={5}
          disabled={loading}
        />


        <div className="chat-input-footer">

          <span className="chat-input-hint">
            Press Ctrl + Enter to ask
          </span>


          <button
            className="primary-button"
            onClick={handleAsk}
            disabled={loading || !question.trim()}
          >

            <Send size={16} />

            {loading ? "Analyzing..." : "Ask AI"}

          </button>

        </div>

      </div>


      {/* =========================
          Example Questions
      ========================= */}

      <div className="dashboard-card chat-examples-card">

        <div className="card-header">

          <div>

            <h2>
              Try asking
            </h2>

            <p>
              Example questions you can ask the AI assistant.
            </p>

          </div>

          <Sparkles size={20} />

        </div>


        <div className="chat-examples">

          {exampleQuestions.map((example) => (

            <button
              key={example}
              className="chat-example"
              onClick={() => handleExampleClick(example)}
              disabled={loading}
            >

              <MessageSquare size={15} />

              <span>
                {example}
              </span>

            </button>

          ))}

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
          AI Response
      ========================= */}

      <div className="dashboard-card chat-response-card">

        <div className="card-header">

          <div>

            <h2>
              AI Response
            </h2>

            <p>
              Business intelligence generated from your retail data.
            </p>

          </div>

          <Bot size={20} />

        </div>


        {/* =========================
            Selected Agents
        ========================= */}

        {response?.selected_agents?.length > 0 && (

          <div className="chat-agent-section">

            <div className="result-label">
              Selected Agent
            </div>


            <div className="chat-agent-list">

              {response.selected_agents.map((agent) => (

                <span
                  key={agent}
                  className={`agent-badge agent-${agent}`}
                >

                  <span className="agent-dot"></span>

                  {agent.charAt(0).toUpperCase() + agent.slice(1)} Agent

                </span>

              ))}

            </div>

          </div>

        )}


        <div className="analytics-result">

          <div className="result-label">
            AI Analysis
          </div>


          <div className="result-content chat-response-content">

            {loading ? (

              <div className="chat-loading">

                <span className="chat-loading-dot"></span>
                <span className="chat-loading-dot"></span>
                <span className="chat-loading-dot"></span>

                <span className="chat-loading-text">
                  AI assistant is analyzing your question...
                </span>

              </div>

            ) : response?.response ? (

              <ReactMarkdown>
                {response.response}
              </ReactMarkdown>

            ) : (

              <div className="chat-empty-state">

                <Bot size={24} />

                <div>

                  <strong>
                    Ask the AI assistant a question
                  </strong>

                  <p>
                    Your business intelligence response will appear here.
                  </p>

                </div>

              </div>

            )}

          </div>

        </div>

      </div>

    </div>
  );
}


export default Chat;