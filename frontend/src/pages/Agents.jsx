import {
  Bot,
  BarChart3,
  TrendingUp,
  Package,
  Database,
  Brain,
  ArrowDown,
} from "lucide-react";


function Agents() {
  const agents = [
    {
      name: "Analytics Agent",
      description:
        "Analyzes historical sales data, trends, store performance, products, categories, and business KPIs.",
      icon: BarChart3,
      status: "Active",
      responsibility: "Business Analytics",
    },
    {
      name: "Forecast Agent",
      description:
        "Generates demand forecasts using the platform's forecasting models and interprets future demand patterns.",
      icon: TrendingUp,
      status: "Active",
      responsibility: "Demand Forecasting",
    },
    {
      name: "Inventory Agent",
      description:
        "Evaluates inventory conditions, stock risks, replenishment requirements, and fast- or slow-moving products.",
      icon: Package,
      status: "Active",
      responsibility: "Inventory Intelligence",
    },
    {
      name: "SQL Agent",
      description:
        "Handles database-oriented questions and generates or executes SQL queries against the analytics warehouse.",
      icon: Database,
      status: "Active",
      responsibility: "Data Retrieval",
    },
  ];


  return (
    <div className="agents-page">

      {/* =========================
          Page Header
      ========================= */}

      <div className="page-header">

        <div>
          <h1>AI Agents</h1>

          <p>
            Multi-agent AI system for business intelligence and decision support.
          </p>
        </div>

        <div className="dashboard-status">

          <span className="status-dot"></span>

          Multi-Agent System

        </div>

      </div>


      {/* =========================
          Architecture Overview
      ========================= */}

      <div className="dashboard-card">

        <div className="card-header">

          <div>
            <h2>Agent Architecture</h2>

            <p>
              Specialized AI agents collaborate to answer business questions.
            </p>
          </div>

          <Brain size={20} />

        </div>


        <div className="agent-flow">

          {/* Router */}

          <div className="agent-flow-node">

            <div className="agent-flow-icon">
              <Bot size={22} />
            </div>

            <div>
              <strong>Task Router</strong>

              <span>
                Understands the question and selects the required agents.
              </span>
            </div>

          </div>


          <div className="agent-flow-arrow">
            <ArrowDown size={20} />
          </div>


          {/* Specialist Agents */}

          <div className="agent-flow-grid">

            {agents.map((agent) => {

              const Icon = agent.icon;

              return (
                <div
                  className="agent-card"
                  key={agent.name}
                >

                  <div className="agent-card-top">

                    <div className="agent-icon">
                      <Icon size={22} />
                    </div>

                    <span className="agent-status">
                      <span className="status-dot"></span>
                      {agent.status}
                    </span>

                  </div>


                  <h3>
                    {agent.name}
                  </h3>


                  <p>
                    {agent.description}
                  </p>


                  <div className="agent-responsibility">
                    {agent.responsibility}
                  </div>

                </div>
              );
            })}

          </div>


          <div className="agent-flow-arrow">
            <ArrowDown size={20} />
          </div>


          {/* Executive Agent */}

          <div className="agent-flow-node executive-agent">

            <div className="agent-flow-icon">
              <Brain size={22} />
            </div>

            <div>
              <strong>Executive Agent</strong>

              <span>
                Combines specialist findings into a unified executive-level
                business report.
              </span>
            </div>

          </div>

        </div>

      </div>


      {/* =========================
          System Explanation
      ========================= */}

      <div className="dashboard-card">

        <div className="card-header">

          <div>
            <h2>How the System Works</h2>

            <p>
              From a natural-language question to an actionable business insight.
            </p>
          </div>

          <Bot size={20} />

        </div>


        <div className="agent-process">

          <div className="process-step">

            <div className="process-number">
              1
            </div>

            <div>
              <h3>User Question</h3>

              <p>
                A user asks a natural-language question about sales,
                forecasting, inventory, or the business.
              </p>
            </div>

          </div>


          <div className="process-step">

            <div className="process-number">
              2
            </div>

            <div>
              <h3>Task Routing</h3>

              <p>
                The Task Router identifies which specialist agents are
                relevant to the question.
              </p>
            </div>

          </div>


          <div className="process-step">

            <div className="process-number">
              3
            </div>

            <div>
              <h3>Specialist Analysis</h3>

              <p>
                Selected agents query the appropriate data or forecasting
                services and generate domain-specific findings.
              </p>
            </div>

          </div>


          <div className="process-step">

            <div className="process-number">
              4
            </div>

            <div>
              <h3>Executive Synthesis</h3>

              <p>
                When multiple agents are involved, the Executive Agent
                combines their findings into a unified business response.
              </p>
            </div>

          </div>

        </div>

      </div>

    </div>
  );
}


export default Agents;