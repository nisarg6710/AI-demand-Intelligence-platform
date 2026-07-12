from src.ai.metadata import ForecastMetadataBuilder
from src.ai.prompts.prompt_builder import PromptBuilder
from src.ai.llm.gemini_client import GeminiClient
from src.ai.report import ReportWriter
from src.ai.html_report import HTMLReportGenerator
from src.ai.prompt_writer import PromptWriter
from src.ai.metadata_writer import MetadataWriter
from src.utils.logger import ProjectLogger


class ForecastExplainer:

    def __init__(self):

        self.client = GeminiClient()
        self.logger = ProjectLogger.get_logger()

    def explain(
        self,
        actual,
        forecast,
    ):

        metadata = ForecastMetadataBuilder.build(
            actual,
            forecast,
        )

        metadata_path = MetadataWriter.save(
            metadata
        )

        self.logger.info(
            'Forecast metadata saved.'
        )

        prompts = PromptBuilder.build(
            metadata,
        )

        prompt_paths = PromptWriter.save(
            prompts['system_prompt'],
            prompts["user_prompt"]
        )

        self.logger.info(
            "Prompt artifacts saved."
        )

        explanation = self.client.generate(
            prompts["system_prompt"],
            prompts["user_prompt"],
        )

        self.logger.info(
            "LLM explanation generated."
        )

        report_path = ReportWriter.save_markdown(
            explanation
        )
        self.logger.info(
            "Markdown report generated."
        )

        html_path = HTMLReportGenerator.generate(
            report_path
        )
        self.logger.info(
            "HTML report generated."
        )

        return {

            "metadata": metadata,

            "metadata_path": metadata_path,

            "system_prompt": prompts["system_prompt"],

            "user_prompt": prompts["user_prompt"],

            "prompt_paths": prompt_paths,

            "explanation": explanation,

            'report_path': report_path,

            'html_report': html_path

        }