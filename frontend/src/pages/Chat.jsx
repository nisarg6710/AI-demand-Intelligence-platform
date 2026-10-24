import { useRef, useState } from "react";
import {
  Send,
  MessageSquare,
  RefreshCw,
  Bot,
  User,
} from "lucide-react";
import ReactMarkdown from "react-markdown";

import { getChat, IS_PUBLIC_DEMO } from "../services/api";

function Chat() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [selectedAgents, setSelectedAgents] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const requestInFlight = useRef(false);

  const exampleQuestions = [
    "What are the top performing stores?",
    "What does the future demand forecast look like?",
    "What are the most important sales trends?",
    "Give me an overview of the retail business performance.",
  ];

  const askQuestion = async (value = question) => {
    const trimmedQuestion = value.trim();

    if (!trimmedQuestion || requestInFlight.current) {
      return;
    }

    requestInFlight.current = true;
    setLoading(true);
    setError(null);

    setMessages((previous) => [
      ...previous,
      {
        role: "user",
        content: trimmedQuestion,
      },
    ]);

    setQuestion("");

    try {
      const result = await getChat(trimmedQuestion);
      if (!result || typeof result.response !== "string") {
        throw new Error("The chat service returned an incomplete response.");
      }

      setSelectedAgents(result.selected_agents || []);

      const supported = result.success === true && result.supported === true;
      const metadata = result.answer_source === "gemini"
        ? "Gemini-generated general guidance · no snapshot measurements queried"
        : result.snapshot_generation
          ? `Snapshot ${result.snapshot_generation} · freshness unverified · ${result.units || "units sold"}`
          : null;

      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          content: result.response,
          status: supported
            ? result.answer_source === "gemini" ? "ai_answer" : "answer"
            : result.intent_status || "unsupported",
          metadata,
        },
      ]);
    } catch (err) {
      console.error("Chat request failed:", err);

      if (err.response?.status === 503) {
        setError("The analytics snapshot is unavailable or invalid. No analytical answer was returned; please try again later.");
      } else if (err.response) {
        setError(`The chat request could not be completed (HTTP ${err.response.status}). No analytical answer was returned.`);
      } else {
        setError(IS_PUBLIC_DEMO
          ? "Unable to reach the demo service. It may be waking after idle time; no analytical answer was returned. Please retry shortly."
          : "Unable to retrieve an AI response. Please try again.");
      }
    } finally {
      requestInFlight.current = false;
      setLoading(false);
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    askQuestion();
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter" && (event.ctrlKey || event.metaKey)) {
      event.preventDefault();
      askQuestion();
    }
  };

  const clearChat = () => {
    setMessages([]);
    setSelectedAgents([]);
    setError(null);
  };

  return (
    <div className="chat-page">

      {/* Header */}
      <div className="page-header">
        <div>
          <h1>{IS_PUBLIC_DEMO ? "Business Chat Demo" : "AI Business Chat"}</h1>
          <p>
            {IS_PUBLIC_DEMO
              ? "Snapshot analytics and forecasts are deterministic. General project questions may use Gemini when configured; no live database or production agents are used."
              : "Ask natural-language questions about your retail data through the local production assistant."}
          </p>
        </div>

        <div className="dashboard-status">
          <span className="status-dot"></span>
          {IS_PUBLIC_DEMO ? "Hybrid Demo" : "AI Intelligence"}
        </div>
      </div>

      {/* Agent Status */}
      {selectedAgents.length > 0 && (
        <div className="dashboard-card chat-agents-card">

          <div className="card-header">
            <div>
              <h2>{IS_PUBLIC_DEMO ? "Demo Response Label" : "Active Intelligence Agents"}</h2>
              <p>
                {IS_PUBLIC_DEMO
                  ? "This label describes the demo response, not a running production agent."
                  : "Agents selected by the production query routing system."}
              </p>
            </div>

            <Bot size={20} />
          </div>

          <div className="chat-agent-list">
            {selectedAgents.map((agent) => (
              <span
                className="chat-agent-badge"
                key={agent}
              >
                {agent}
              </span>
            ))}
          </div>

        </div>
      )}

      {/* Chat */}
      <div className="dashboard-card chat-container">

        <div className="chat-header">
          <div>
            <h2>{IS_PUBLIC_DEMO ? "Demo Assistant" : "Business Intelligence Assistant"}</h2>
            <p>
              {IS_PUBLIC_DEMO
                ? "Ask about snapshot metrics for deterministic answers, or general project-capability questions for optional Gemini guidance."
                : "Ask about sales, forecasting, stores, products, and business performance."}
            </p>
          </div>

          {messages.length > 0 && (
            <button
              type="button"
              className="secondary-button"
              onClick={clearChat}
              disabled={loading}
            >
              Clear Chat
            </button>
          )}
        </div>

        {/* Messages */}
        <div className="chat-messages">

          {messages.length === 0 ? (
            <div className="chat-empty">

              <div className="chat-empty-icon">
                <MessageSquare size={28} />
              </div>

              <h3>
                Start a business conversation
              </h3>

              <p>
                Analytics and forecasts use the read-only snapshot. General project guidance may use Gemini when configured; it does not use live business measurements.
              </p>

            </div>
          ) : (
            messages.map((message, index) => (
              <div
                className={`chat-message ${message.role}`}
                key={`${message.role}-${index}`}
              >

                <div className="chat-message-icon">
                  {message.role === "user" ? (
                    <User size={18} />
                  ) : (
                    <Bot size={18} />
                  )}
                </div>

                <div className="chat-message-content">

                  <div className="chat-message-role">
                    {message.role === "user"
                      ? "You"
                      : (IS_PUBLIC_DEMO ? "Demo Assistant" : "AI Assistant")}
                  </div>

                  {message.role === "assistant" ? (
                    <>
                      {IS_PUBLIC_DEMO && message.status && (
                        <p className="chat-message-status">
                          {message.status === "answer"
                            ? "Snapshot-grounded answer"
                            : message.status === "ai_answer"
                              ? "AI-generated general guidance"
                              : message.status === "provider_unavailable"
                                ? "Gemini unavailable · fixed project information"
                                : message.status === "ambiguous"
                                  ? "Please clarify"
                                  : "Unsupported question"}
                        </p>
                      )}
                      <div className="markdown-content">
                        <ReactMarkdown>{message.content}</ReactMarkdown>
                      </div>
                      {message.metadata && (
                        <p className="chat-message-metadata">{message.metadata}</p>
                      )}
                    </>
                  ) : (
                    <p>{message.content}</p>
                  )}

                </div>

              </div>
            ))
          )}

          {loading && (
            <div className="chat-message assistant">

              <div className="chat-message-icon">
                <Bot size={18} />
              </div>

              <div className="chat-message-content">

                <div className="chat-message-role">
                  {IS_PUBLIC_DEMO ? "Demo Assistant" : "AI Assistant"}
                </div>

                <div className="chat-thinking">
                  <RefreshCw
                    size={16}
                    className="spin"
                  />
                  {IS_PUBLIC_DEMO
                    ? "Waiting for the demo service. It may be waking after idle time..."
                    : "Analyzing your question..."}
                </div>

              </div>

            </div>
          )}

        </div>

        {/* Input */}
        <form
          className="chat-input-area"
          onSubmit={handleSubmit}
        >

          <textarea
            value={question}
            onChange={(event) =>
              setQuestion(event.target.value)
            }
            onKeyDown={handleKeyDown}
            placeholder="Ask a business question..."
            rows={3}
            disabled={loading}
          />

          <div className="chat-input-footer">

            <span>
              Ctrl + Enter to send
            </span>

            <button
              type="submit"
              className="primary-button"
              disabled={loading || !question.trim()}
            >
              {loading ? (
                <>
                  <RefreshCw
                    size={17}
                    className="spin"
                  />
                  Thinking...
                </>
              ) : (
                <>
                  <Send size={17} />
                  {IS_PUBLIC_DEMO ? "Send Demo Question" : "Ask AI"}
                </>
              )}
            </button>

          </div>

        </form>

      </div>

      {/* Example Questions */}
      <div className="dashboard-card">

        <div className="card-header">
          <div>
            <h2>Example Questions</h2>
            <p>
              Try one of these business intelligence queries.
            </p>
          </div>

          <MessageSquare size={20} />
        </div>

        <div className="example-question-list">

          {exampleQuestions.map((example) => (
            <button
              type="button"
              className="example-question"
              key={example}
              onClick={() => askQuestion(example)}
              disabled={loading}
            >
              {example}
            </button>
          ))}

        </div>

      </div>

      {error && (
        <div className="error-banner">
          {error}
        </div>
      )}

    </div>
  );
}

export default Chat;
