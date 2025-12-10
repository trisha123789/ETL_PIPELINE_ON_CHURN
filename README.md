
#ETL Pipeline on Customer Churn Data

This project demonstrates a complete ETL (Extract–Transform–Load) pipeline built on a customer Churn dataset, showcasing real-world data engineering and data preprocessing skills. The pipeline cleans the data, transforms it into an analysis-ready format, and loads it into a cloud database using Supabase.


<img width="890" height="417" alt="image" src="https://github.com/user-attachments/assets/5ad21394-fc73-4a3a-9774-85ba5236f92c" />

🔍 Project Overview

The goal of this ETL pipeline is to prepare churn data for analytics and machine learning.
It includes:

Extracting raw data from a CSV file

Transforming it with cleaning, encoding, feature engineering, and grouping

Loading the processed dataset into Supabase

Performing exploratory analysis to understand churn patterns

⚙️ ETL Pipeline Steps
1️⃣ Extract

Read the raw churn CSV file

Inspected schema, column types, and missing values

Identified categorical, numerical, and target variables

2️⃣ Transform

Cleaning & preprocessing steps applied:

Removed/handled missing values

Standardized category names

Converted TotalCharges to numeric

Created tenure groups

Encoded Yes/No fields

One-hot encoded categorical variables

Detected outliers

Created transformed columns for analysis

Validated the final schema before load

3️⃣ Load

Connected to Supabase using the REST API

Inserted transformed rows in batches

Handled schema validation errors

Verified table structure in Supabase dashboard

Loaded final dataset into a table named churn_transformed

📈 Analysis Performed

After successful ETL, exploratory analysis included:

Churn rate by tenure group

Churn rate by contract type

Churn vs monthly charges

Pivot tables for insights

Visualizations using pandas, seaborn, and matplotlib

📦 Tech Stack

Python

Pandas, NumPy

Supabase (REST API)

Matplotlib / Seaborn

Jupyter Notebook / VS Code

📁 Project Structure
├── data/
│   ├── churn_raw.csv
│   └── churn_transformed.csv
├── notebooks/
│   └── churn_etl.ipynb
├── scripts/
│   └── etl_churn.py
├── README.md

🚀 Key Learnings

Building real ETL workflows

Cleaning enterprise-like customer datasets

Understanding churn behavior

Handling batch insertion with Supabase

Improving data quality for ML models

✨ Future Enhancements

Add churn prediction model

Build a dashboard using Streamlit

Schedule ETL using Cron / Airflow
