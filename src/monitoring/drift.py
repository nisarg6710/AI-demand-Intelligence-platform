from dataclasses import dataclass

import numpy as np


@dataclass
class DriftReport:
    statistic: float
    threshold: float
    drift_detected: bool


class DriftMonitor:
    """
    Lightweight distribution-drift detector.

    Uses the difference between the empirical means and standard
    deviations of reference and current observations.
    """

    def __init__(self, threshold: float = 0.2):
        self.threshold = threshold

    def detect(
        self,
        reference,
        current,
    ) -> DriftReport:

        reference = np.asarray(reference, dtype=float)
        current = np.asarray(current, dtype=float)

        reference = reference[np.isfinite(reference)]
        current = current[np.isfinite(current)]

        if len(reference) == 0 or len(current) == 0:
            raise ValueError(
                "Reference and current data must contain "
                "at least one finite value."
            )

        reference_mean = np.mean(reference)
        current_mean = np.mean(current)

        reference_std = np.std(reference)

        if reference_std == 0:
            statistic = abs(current_mean - reference_mean)
        else:
            statistic = (
                abs(current_mean - reference_mean)
                / reference_std
            )

        return DriftReport(
            statistic=float(statistic),
            threshold=self.threshold,
            drift_detected=bool(statistic > self.threshold),
        )