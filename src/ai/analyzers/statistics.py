import numpy as np

class StatisticsAnalyzer:

    @staticmethod
    def analyze(forecast):

        forecast = np.asarray(
            forecast
        ).flatten()

        return {
            'mean': round(
                float(np.mean(forecast)),
                2
            ),

            'minimum': round(
                float(np.min(forecast)),
                2
            ),

            'maximum': round(
                float(np.max(forecast)),
                2
            ),

            'std_dev': round(
                float(np.std(forecast)),
                2
            ),

            'range': round(
                float(
                    np.max(forecast) - np.min(forecast)
                ),
                2
            )
        }