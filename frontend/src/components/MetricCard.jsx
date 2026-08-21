function MetricCard({ title, value, description, icon }) {
  return (
    <div className="metric-card">
      <div className="metric-card-header">
        <span className="metric-title">{title}</span>

        <div className="metric-icon">
          {icon}
        </div>
      </div>

      <div className="metric-value">
        {value}
      </div>

      {description && (
        <div className="metric-description">
          {description}
        </div>
      )}
    </div>
  );
}

export default MetricCard;