import os
from datetime import datetime

class ReportWriter:

    @staticmethod
    def save_markdown(
        explanation,
        filename=None
    ):
        report_dir = 'artifacts/reports'

        os.makedirs(
            report_dir,
            exist_ok=True
        )

        if filename is None:
            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            filename = (
                f"forecast_report_{timestamp}.md"
            )

        path = os.path.join(
            report_dir,
            filename
        )

        with open(
            path,
            'w',
            encoding='utf-8'
        ) as file:
            
            file.write(explanation)
        
        return path