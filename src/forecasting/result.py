from dataclasses import dataclass


@dataclass
class ForecastResult:

    model_name: str

    mae: float
    rmse: float
    mape: float

    train_time: float
    predict_time: float