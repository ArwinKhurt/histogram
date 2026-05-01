ArwinKhurtAyuban_TPPrefi_ModelingandSim_BSCS601
Retail Store Product Sales Histogram
Overview

This project presents a simple data analysis and visualization of a retail dataset using Python. It generates a histogram to show the distribution of a selected numeric variable, such as product price, allowing for basic exploratory data analysis.

Dataset
File Name: RetailStoreProductSalesDataset.csv
Description: The dataset contains retail store product sales data, including numerical attributes such as price, discount, and other relevant variables.

Ensure the dataset file is located in the same directory as the Python script before execution.

Requirements

The project requires the following Python libraries:

pip install pandas matplotlib
How to Run
Download or clone the repository.
Place the dataset file (RetailStoreProductSalesDataset.csv) in the project directory.
Run the script using the following command:
python histogram.py
Methodology

The script follows these steps:

Imports the required libraries (pandas and matplotlib).
Loads the dataset from a CSV file into a DataFrame.
Displays column names to verify available data fields.
Selects a numeric column for analysis (default: price).
Generates a histogram with a specified number of bins.
Labels the axes and assigns a descriptive title.
Displays the histogram.
Output

The output is a histogram that illustrates the frequency distribution of the selected variable. This helps in understanding:

The spread of the data
The central tendency
The presence of potential outliers
Customization

To analyze a different variable, modify the following line in the script:

column_name = 'price'

Replace 'price' with any other numeric column available in the dataset (e.g., discount, footfall).

Notes
The selected column must contain numeric data.
Ensure the dataset file path is correct.
The number of bins in the histogram can be adjusted within the script.
