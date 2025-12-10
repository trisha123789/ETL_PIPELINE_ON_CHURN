
import os

import pandas as pd

from extract import extract_data

 

def tenure_group(tenure):

    if tenure <= 12:

        return "New"

    elif tenure <= 36:

        return "Regular"

    elif tenure <= 60:

        return "Loyal"

    else:

        return "Champion"

 

def month_group(months):

    if months <= 12:

        return "Low"

    elif months <= 36:

        return "Medium"

    elif months <= 60:

        return "High"

    else:

        return "Champion"

 

def internet_service(internet):

    return 1 if internet in ["Fiber optic", "DSL"] else 0

 

def multi_line_user(multi):

    return 1 if multi == "Yes" else 0

 

# Purpose: Clean and transform Telco Churn dataset

def transform_data(raw_path):

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    staged_dir = os.path.join(base_dir, "data", "staged")

    os.makedirs(staged_dir, exist_ok=True)

 

    df = pd.read_csv(raw_path)

 

    df['tenure_group'] = df['tenure'].apply(tenure_group)

    df['monthly_charge_segment'] = df['MonthlyCharges'].apply(month_group)

    df['has_internet_service'] = df['InternetService'].apply(internet_service)

    df['is_multi_line_user'] = df['MultipleLines'].apply(multi_line_user)

    df['contract_type_code'] = df['Contract'].map(

        {'Month-to-month': 0, 'One year': 1, 'Two year': 2}

    ).fillna(-1)

 

    df = df.drop(columns=["customerID", "gender", "SeniorCitizen", "Partner", "Dependents",

                          "PhoneService", "MultipleLines", "OnlineSecurity",

                          "OnlineBackup", "DeviceProtection", "TechSupport",

                          "StreamingTV", "StreamingMovies", "PaperlessBilling"])

    df.drop_duplicates(inplace=True)

    staged_path = os.path.join(staged_dir, "telco_cleaned.csv")

    df.to_csv(staged_path, index=False)

 

    print(f"✅ Data transformed and saved at: {staged_path}")

    return staged_path

 

 

if __name__ == "__main__":

    raw_path = extract_data()

    transform_data(raw_path)

