import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("RetailStoreProductSalesDataset.csv")

print(df.columns)

column_name = 'price'   # you can change this to: 'discount', 'footfall', etc.

plt.hist(df[column_name], bins=15, edgecolor='black')

plt.xlabel(column_name)
plt.ylabel("Frequency")
plt.title(f"Histogram of {column_name}")

plt.show()