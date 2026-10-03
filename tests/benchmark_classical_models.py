import os
import sys

# Change the notebook's active working directory to the project root
if os.path.basename(os.getcwd()) == "notebooks":
    os.chdir("..")

# Ensure the root path is also in sys.path
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())


from src.forecasting.registry import ForecastRegistry
from src.forecasting.pipeline import ForecastPipeline

from src.forecasting.moving_average import MovingAverageModel
from src.forecasting.arima import ARIMAModel
from src.forecasting.sarima import SARIMAModel
from src.forecasting.prophet import ProphetModel

from src.forecasting.report import ForecastReport

registry = ForecastRegistry()

# Moving Average
registry.add(
    ForecastPipeline.run(
        MovingAverageModel(window=7)
    )
)

# ARIMA
registry.add(
    ForecastPipeline.run(
        ARIMAModel(order=(5,1,0))
    )
)

# SARIMA
registry.add(
    ForecastPipeline.run(
        SARIMAModel(
            order=(1,1,0),
            seasonal_order=(2,0,1,7)
        )
    )
)

# Prophet
registry.add(
    ForecastPipeline.run(
        ProphetModel()
    )
)

registry.summary()

ForecastReport.generate(
    registry.get_results()
)