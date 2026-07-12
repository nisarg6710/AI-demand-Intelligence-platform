import os
from datetime import datetime

import markdown


class HTMLReportGenerator:

    @staticmethod
    def generate(
        markdown_path,
        output_filename=None,
    ):

        with open(
            markdown_path,
            "r",
            encoding="utf-8",
        ) as file:

            md_text = file.read()

        html_body = markdown.markdown(md_text)

        html = f"""
<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<title>Forecast Report</title>

<style>

body {{
    font-family: Arial, sans-serif;
    margin: 40px;
    line-height: 1.7;
    max-width: 1000px;
}}

h1 {{
    color: #1565C0;
}}

h2 {{
    color: #2E7D32;
}}

h3 {{
    color: #6A1B9A;
}}

code {{
    background: #eeeeee;
    padding: 2px 4px;
}}

</style>

</head>

<body>

{html_body}

</body>

</html>
"""

        report_dir = "artifacts/reports"

        os.makedirs(
            report_dir,
            exist_ok=True,
        )

        if output_filename is None:

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            output_filename = (
                f"forecast_report_{timestamp}.html"
            )

        output_path = os.path.join(
            report_dir,
            output_filename,
        )

        with open(
            output_path,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(html)

        return output_path