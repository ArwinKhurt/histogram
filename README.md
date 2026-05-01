# Retail Store Product Sales Histogram

This is a task performance for the subject Modeling and Simulation.

---

## Overview

This project performs a simple data analysis and visualization of a retail dataset using Python. It generates a histogram to display the distribution of a selected numeric variable, such as product price, to support basic exploratory data analysis.

---

## What it does

- Loads a dataset containing retail product sales data  
- Generates a histogram for a selected numeric column  
- Displays the frequency distribution of values  
- Helps identify patterns such as:
  - Data spread  
  - Central tendency  
  - Potential outliers  

---

## Dataset

- **File Name:** `RetailStoreProductSalesDataset.csv`  
- **Description:** Contains retail store product sales data, including numerical attributes such as price, discount, and other relevant variables  

Ensure the dataset file is located in the same directory as the Python script before execution.

---

## Requirements

The project requires the following Python libraries:

bash
pip install pandas matplotlib

## How to Run

1. Download or clone the repository  
2. Place the dataset file in the project directory  
3. Run the script using the following command:

bash
python histogram.py

## Methodology

The script performs the following steps:

- Imports the required libraries (`pandas` and `matplotlib`)  
- Loads the dataset into a DataFrame  
- Displays column names to verify available data fields  
- Selects a numeric column for analysis (default: `price`)  
- Generates a histogram with a specified number of bins  
- Labels the axes and assigns a descriptive title  
- Displays the histogram  

---

## Output

- A histogram showing the frequency distribution of the selected variable  
- Provides insight into:
  - Data spread  
  - Central tendency  
  - Potential outliers  

---

## Customization

To analyze a different variable, modify the following line in the script:

python
column_name = 'price'

You may replace 'price' with another numeric column such as:
discount
footfall

