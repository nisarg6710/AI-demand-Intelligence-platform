import numpy as np
import torch

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error


class Evaluator:

    def __init__(self, model):

        self.model = model

    def load_model(
        self,
        checkpoint_path,
    ):

        self.model.load_state_dict(
            torch.load(
                checkpoint_path,
                map_location=self.model.device,
            )
        )

        self.model.eval()

    def predict(
        self,
        dataloader,
    ):

        predictions = []
        targets = []

        with torch.no_grad():

            for X, y in dataloader:

                X = X.to(self.model.device)

                prediction = self.model(X)

                predictions.extend(
                    prediction.cpu().numpy()
                )

                targets.extend(
                    y.numpy()
                )

        predictions = np.array(predictions)
        targets = np.array(targets)

        return predictions, targets

    def inverse_transform(
        self,
        scaler,
        predictions,
        targets,
    ):

        predictions = scaler.inverse_transform(
            predictions
        )

        targets = scaler.inverse_transform(
            targets
        )

        return predictions, targets

    def calculate_metrics(
        self,
        predictions,
        targets,
    ):

        mae = mean_absolute_error(
            targets,
            predictions,
        )

        rmse = np.sqrt(
            mean_squared_error(
                targets,
                predictions,
            )
        )

        epsilon = 1e-8

        mape = np.mean(

            np.abs(
                (targets - predictions)
                /
                (targets + epsilon)
            )

        ) * 100

        return {
            'predictions': predictions,

            'targets': targets,

            'metrics':{

                "MAE": mae,

                "RMSE": rmse,

                "MAPE": mape
            },

        }

    def evaluate(
        self,
        checkpoint_path,
        dataloader,
        scaler,
    ):

        self.load_model(
            checkpoint_path
        )

        predictions, targets = self.predict(
            dataloader
        )

        predictions, targets = self.inverse_transform(
            scaler,
            predictions,
            targets,
        )

        return self.calculate_metrics(
            predictions,
            targets,
        )