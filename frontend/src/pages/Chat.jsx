import { useState } from "react";
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

  const exampleQuestions = [
    "What are the top performing stores?",
    "What does the future demand forecast look like?",
    "What are the most important sales trends?",
    "Give me an overview of the retail business performance.",
  ];

  const askQuestion = async (value = question) => {
    const trimmedQuestion = value.trim();

    if (!trimmedQuestion || loading) {
      return;
    }

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

      setSelectedAgents(result.selected_agents || []);

      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          content:
            result.response ||
            "No response was returned by the intelligence system.",
        },
      ]);
    } catch (err) {
      console.error("Chat request failed:", err);

      setError(IS_PUBLIC_DEMO
        ? "Unable to retrieve a demo response. The service may be waking after idle time; please retry shortly."
        : "Unable to retrieve an AI response. Please try again.");
    } finally {
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
              ? "Demo interactions only. Responses do not call Gemini, query the live database, or run production agents."
              : "Ask natural-language questions about your retail data through the local production assistant."}
          </p>
        </div>

        <div className="dashboard-status">
          <span className="status-dot"></span>
          {IS_PUBLIC_DEMO ? "Demo Interaction" : "AI Intelligence"}
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
                ? "Ask about the available snapshots. This demo does not query live data or invoke an AI assistant."
                : "Ask about sales, forecasting, stores, products, and business performance."}
            </p>
          </div>

          {messages.length > 0 && (
            <button
              type="button"
              className="secondary-button"
              onClick={clearChat}
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
                The public demo returns an explanatory response. It does not execute the production AI agent system.
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
                    <div className="markdown-content">
                      <ReactMarkdown>
                        {message.content}
                      </ReactMarkdown>
                    </div>
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
