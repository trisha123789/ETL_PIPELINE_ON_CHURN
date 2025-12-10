import os

import pandas as pd

 

def extract_data():

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    data_dir = os.path.join(base_dir, "data", "raw")

    os.makedirs(data_dir, exist_ok=True)

 

    raw_path = os.path.join(data_dir, "WA_Fn-UseC_-Telco-Customer-Churn.csv")

    pd.read_csv(raw_path)  # just validate file exists and is readable

 

    print(f"✅ Data loaded from: {raw_path}")

    return raw_path
