# validate.py

import pandas as pd

from supabase import create_client, Client

from dotenv import load_dotenv

import os

 

def get_supabase_client() -> Client:

    """Initialize and return Supabase client."""

    load_dotenv()

    url = os.getenv("SUPABASE_URL")

    key = os.getenv("SUPABASE_KEY")

   

    if not url or not key:

        raise ValueError("❌ Missing SUPABASE_URL or SUPABASE_KEY in .env")

       

    return create_client(url, key)

def validate_data(local_path: str, table_name: str = "customer_churn"):

    # Convert to absolute path

    if not os.path.isabs(local_path):

        local_path = os.path.abspath(os.path.join(os.path.dirname(__file__), local_path))

    print(f"🔍 Looking for data file at: {local_path}")

    if not os.path.exists(local_path):

        print(f"❌ Error: File not found at {local_path}")

        print("ℹ️  Please run transform.py first to generate the transformed data")

        return

    try:

        supabase = get_supabase_client()

        df = pd.read_csv(local_path)

        total_rows = len(df)

        print(f"📊 Validating {total_rows} rows in '{table_name}'...")

        # Check for missing values

        missing_tenure = df['tenure'].isnull().sum()

        missing_monthly_charges = df['MonthlyCharges'].isnull().sum()

        missing_total_charges = df['TotalCharges'].isnull().sum()

        if missing_tenure > 0 or missing_monthly_charges > 0 or missing_total_charges > 0:

            print(f"❌ Missing values found - tenure: {missing_tenure}, MonthlyCharges: {missing_monthly_charges}, TotalCharges: {missing_total_charges}")

            return

        # Check for unique count of rows

        unique_rows = len(df.drop_duplicates())

        if unique_rows != total_rows:

            print(f"❌ Duplicate rows found - unique rows: {unique_rows}, total rows: {total_rows}")

            return

        # Check for existence of segments

        tenure_segments = df['tenure_group'].unique()

        monthly_charge_segments = df['monthly_charge_segment'].unique()

        if 'New' not in tenure_segments or 'Regular' not in tenure_segments or 'Loyal' not in tenure_segments or 'Champion' not in tenure_segments:

            print(f"❌ Missing tenure segments: {tenure_segments}")

            return

        if 'Medium' not in monthly_charge_segments or 'High' not in monthly_charge_segments or 'Champion' not in monthly_charge_segments:

            print(f"❌ Missing monthly charge segments: {monthly_charge_segments}")

            return

        # Check for existence of contract codes

        contract_codes = df['contract_type_code'].unique()

        if 0 not in contract_codes or 1 not in contract_codes or 2 not in contract_codes:

            print(f"❌ Missing contract codes: {contract_codes}")

            return

        # All checks passed

        print("✅ Validation successful!")

    except Exception as e:

        print(f"⚠️  Error during validation: {e}")

       

 

if __name__ == "__main__":

    # Path relative to the script location

    staged_csv_path = os.path.join("..", "data", "staged", "telco_cleaned.csv")

    validate_data(staged_csv_path)
