from src.forecasting.deep_learning.data import ForecastDataLoader


def main():
    print("=" * 50)
    print("Testing ForecastDataLoader")
    print("=" * 50)

    loader = ForecastDataLoader()

    train, validation, test, scaler = loader.prepare()

    print("\nData Shapes")
    print("-" * 30)
    print(f"Train      : {train.shape}")
    print(f"Validation : {validation.shape}")
    print(f"Test       : {test.shape}")

    print("\nSample Values")
    print("-" * 30)
    print("Train (first 5):")
    print(train[:5])

    print("\nValidation (first 5):")
    print(validation[:5])

    print("\nTest (first 5):")
    print(test[:5])

    print("\nScaler Information")
    print("-" * 30)
    print(f"Minimum: {scaler.data_min_}")
    print(f"Maximum: {scaler.data_max_}")

    print("\nNormalization Check")
    print("-" * 30)
    print(f"Train Min : {train.min():.4f}")
    print(f"Train Max : {train.max():.4f}")


if __name__ == "__main__":
    main()