import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("RetailStoreProductSalesDataset.csv")

# (Optional) check column names
print(df.columns)

# Use a valid numeric column
column_name = 'price'   # you can change this to: 'discount', 'footfall', etc.

# Create histogram
plt.hist(df[column_name], bins=15, edgecolor='black')

# Labels and title
plt.xlabel(column_name)
plt.ylabel("Frequency")
plt.title(f"Histogram of {column_name}")

# Show plot
plt.show()