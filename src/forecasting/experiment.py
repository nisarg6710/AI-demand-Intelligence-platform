from dataclasses import dataclass

@dataclass
class ForecastingExperiment:

    model_name: str

    parameters: dict

    mae: float

    rmse: float

    mape: float

    train_time: float

    predict_time: float