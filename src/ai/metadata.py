from src.ai.analyzers.seasonality import SeasonalityAnalyzer
from src.ai.analyzers.statistics import StatisticsAnalyzer
from src.ai.analyzers.trend import TrendAnalyzer

class ForecastMetadataBuilder:

    @staticmethod
    def build(
        actual,
        forecast
    ):
        return {
            'trend': TrendAnalyzer.analyze(
                actual,
                forecast
            ),

            'seasonality': SeasonalityAnalyzer.analyze(
                forecast
            ),

            'statistics': StatisticsAnalyzer.analyze(
                forecast
            )
        }
