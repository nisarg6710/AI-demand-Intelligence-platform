import {
  BarChart3,
  TrendingUp,
  Package,
  Database,
  Brain,
  ArrowDown,
  CheckCircle2,
} from "lucide-react";

const agents = [
  {
    name: "Analytics Agent",
    description:
      "Analyzes historical sales, stores, products, categories, departments, and business trends.",
    capabilities: [
      "Sales analytics",
      "Store performance",
      "Product analysis",
      "Category analysis",
    ],
    icon: BarChart3,
  },
  {
    name: "Forecast Agent",
    description:
      "Evaluates forecasting models and provides future demand intelligence.",
    capabilities: [
      "Model comparison",
      "Forecast evaluation",
      "Future demand forecasting",
      "Prediction analysis",
    ],
    icon: TrendingUp,
  },
  {
    name: "Inventory Agent",
    description:
      "Provides inventory-oriented intelligence using demand and sales information.",
    capabilities: [
      "Inventory analysis",
      "Demand signals",
      "Stock intelligence",
      "Business recommendations",
    ],
    icon: Package,
  },
  {
    name: "SQL Agent",
    description:
      "Translates business questions into database queries and retrieves structured information.",
    capabilities: [
      "Natural-language SQL",
      "Database querying",
      "Structured data retrieval",
      "Query analysis",
    ],
    icon: Database,
  },
];

function Agents() {
  return (
    <div className="agents-page">

      {/* Header */}
      <div className="page-header">
        <div>
          <h1>AI Agents</h1>
          <p>
            Specialized intelligence agents powering the retail platform.
          </p>
        </div>

        <div className="dashboard-status">
          <span className="status-dot"></span>
          Multi-Agent System
        </div>
      </div>

      {/* Architecture */}
      <div className="dashboard-card agent-architecture">

        <div className="card-header">
          <div>
            <h2>Multi-Agent Architecture</h2>
            <p>
              Business questions are routed to specialized intelligence agents.
            </p>
          </div>

          <Brain size={20} />
        </div>

        <div className="agent-flow">

          <div className="agent-flow-node router-node">
            <Brain size={22} />
            <strong>Query Router</strong>
            <span>Understands the business question</span>
          </div>

          <ArrowDown className="agent-flow-arrow" size={22} />

          <div className="agent-flow-specialists">

            {agents.map((agent) => {
              const Icon = agent.icon;

              return (
                <div
                  className="agent-flow-node"
                  key={agent.name}
                >
                  <Icon size={20} />
                  <strong>{agent.name}</strong>
                  <span>Specialized analysis</span>
                </div>
              );
            })}

          </div>

          <ArrowDown className="agent-flow-arrow" size={22} />

          <div className="agent-flow-node executive-node">
            <Brain size={22} />
            <strong>Executive Response</strong>
            <span>Combines intelligence into a business response</span>
          </div>

        </div>

      </div>

      {/* Agents */}
      <div className="agents-grid">

        {agents.map((agent) => {
          const Icon = agent.icon;

          return (
            <div
              className="dashboard-card agent-card"
              key={agent.name}
            >

              <div className="agent-card-icon">
                <Icon size={24} />
              </div>

              <div className="agent-card-content">

                <div className="agent-card-title">
                  <div>
                    <h2>{agent.name}</h2>

                    <div className="agent-status">
                      <span className="status-dot"></span>
                      Available
                    </div>
                  </div>
                </div>

                <p className="agent-description">
                  {agent.description}
                </p>

                <div className="agent-capabilities">

                  <h3>Capabilities</h3>

                  {agent.capabilities.map((capability) => (
                    <div
                      className="agent-capability"
                      key={capability}
                    >
                      <CheckCircle2 size={15} />
                      <span>{capability}</span>
                    </div>
                  ))}

                </div>

              </div>

            </div>
          );
        })}

      </div>

      {/* Workflow */}
      <div className="dashboard-card agent-workflow">

        <div className="card-header">
          <div>
            <h2>How the System Works</h2>
            <p>
              End-to-end flow for natural-language business intelligence.
            </p>
          </div>

          <Brain size={20} />
        </div>

        <div className="workflow-grid">

          <div className="workflow-step">
            <span>01</span>
            <h3>Ask</h3>
            <p>
              A user submits a natural-language business question.
            </p>
          </div>

          <div className="workflow-step">
            <span>02</span>
            <h3>Route</h3>
            <p>
              The query router identifies the appropriate specialist agent.
            </p>
          </div>

          <div className="workflow-step">
            <span>03</span>
            <h3>Analyze</h3>
            <p>
              The selected agent retrieves and analyzes the required data.
            </p>
          </div>

          <div className="workflow-step">
            <span>04</span>
            <h3>Respond</h3>
            <p>
              The system produces a business-oriented natural-language response.
            </p>
          </div>

        </div>

      </div>

    </div>
  );
}

export default Agents;