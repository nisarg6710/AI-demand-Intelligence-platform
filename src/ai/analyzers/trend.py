import numpy as np

class TrendAnalyzer:

    @staticmethod
    def analyze(actual, forecast):

        actual = np.asarray(actual).flatten()
        forecast = np.asarray(forecast).flatten()

        last_actual = actual[-1]
        mean_forecast = forecast.mean()

        growth = (
            (mean_forecast - last_actual) / last_actual
        ) * 100

        if growth > 10:
            direction = 'Strong Increase'

        elif growth > 2:
            direction = 'Increasing'
        
        elif growth < -10:
            direction = 'Strong Decrease'
        
        elif growth < -2:
            direction = 'Decreasing'
        
        else:
            direction = 'Stable'
        
        return {
            'direction': direction,
            'growth_percent': round(
                float(growth),
                2
            ),

            'last_actual': float(last_actual),
            'average_forecast': float(mean_forecast)
        }