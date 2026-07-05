from src.forecasting.metrics import ForecastMetrics

class ForecastEvaluator:

    @staticmethod
    def evaluate(actual, predicted):

        return {
            'MAE': ForecastMetrics.mae(
                actual,
                predicted
            ),

            'RMSE': ForecastMetrics.rmse(
                actual,
                predicted
            ),
            
            'MAPE': ForecastMetrics.mape(
                actual,
                predicted
            )
        }