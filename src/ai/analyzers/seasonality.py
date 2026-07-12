import numpy as np

class SeasonalityAnalyzer:

    @staticmethod
    def analyze(forecast):

        forecast = np.asarray(
            forecast
        ).flatten()

        if len(forecast) < 14:
            return {

                'weekly_seasonality': False,
                'seasonality_strength': 'Unknown'
            }

        correlation = np.corrcoef(
            forecast[:-7],
            forecast[7:]
        )[0,1]

        if correlation >= 0.8:
            strength = 'Strong'
        
        elif correlation >= 0.5:
            strength = 'Moderate'
        
        elif correlation >= 0.2:
            strength = 'Weak'
        
        else:
            strength = 'None'
        
        return {
            'weekly_seasonality': bool(correlation >= 0.5),
            'seasonality_strength': strength,
            'correlation': round(
                float(correlation),
                3,
            )
        }