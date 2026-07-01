import pandas as pd

from src.transforms.sales import transform_sales

df = pd.read_csv(
    "data/raw/m5/sales_train_validation.csv",
    nrows=2
)

print("Original shape:", df.shape)

sales_df = transform_sales(df)

print("Transformed shape:", sales_df.shape)

print(sales_df.head(10))