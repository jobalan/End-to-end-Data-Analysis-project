/*
=============================================================================
Python Script: Data Acquisition, Cleaning, Data Integration and Transformation
=============================================================================
Script Purpose:
    This script performs the complete ETL pipeline by merging four e-commerce source files,
calculating core metrics (Profit, Net Sales, COGS), and cleaning the data. Outputs a single, clean cleaned_sales_data.csv file,
ready for loading into the SQL Star Schema for analysis.
=============================================================================    
*/

import pandas as pd
import numpy as np

# --- Configuration Constants ---
FILE_USERS = 'users.csv'
FILE_PRODUCTS = 'products.csv'
FILE_ORDERS = 'orders.csv'
FILE_ORDER_ITEMS = 'order_items.csv'
OUTPUT_FILE = 'cleaned_sales_data.csv'


# --- 1. DATA ACQUISITION & CLEANING ---

def load_and_clean_data():
    """Loads files and converts the date column to datetime, handling errors."""
    try:
        data_dict = {
            'users': pd.read_csv(FILE_USERS),
            'products': pd.read_csv(FILE_PRODUCTS),
            'orders': pd.read_csv(FILE_ORDERS),
            'order_items': pd.read_csv(FILE_ORDER_ITEMS)
        }

        # Crucial cleaning: Convert date to datetime, coerce errors to NaT
        data_dict['orders']['order_date'] = pd.to_datetime(
            data_dict['orders']['order_date'], errors='coerce'
        )
        print("Data loaded and date column cleaned.")
        return data_dict

    except FileNotFoundError as e:
        print(f "Error: One or more files not found: {e}")
        return None


# --- 2. DATA INTEGRATION & FEATURE ENGINEERING ---

def merge_and_engineer_features(data_dict):
    """Merges DataFrames and calculates key business metrics (Net Sales, Profit)."""
    df_combined = data_dict['order_items'].copy()

    # 2.1 Merge DataFrames (Creating the Fact Table)

    # Merge with Orders (brings in user_id, date, status, shipping cost)
    df_combined = pd.merge(df_combined, data_dict['orders'].drop(columns=['payment_method']),
                           on='order_id', how='left')

    # Merge with Products (brings in category, subcategory, cost)
    df_combined = pd.merge(df_combined, data_dict['products'][['product_id', 'category', 'subcategory', 'cost']],
                           on='product_id', how='left')

    # Merge with Users (brings in customer details)
    df_combined = pd.merge(df_combined, data_dict['users'][
        ['user_id', 'age', 'gender', 'customer_segment', 'city', 'state', 'country']],
                           on='user_id', how='left')

    # 2.2 Feature Engineering (Business Metrics)

    # Gross Sales
    df_combined['gross_sales'] = df_combined['quantity'] * df_combined['unit_price']

    # Net Sales (Actual Revenue)
    df_combined['net_sales'] = df_combined['gross_sales'] * (1 - df_combined['discount'] / 100)

    # COGS (Cost of Goods Sold)
    df_combined['cogs'] = df_combined['quantity'] * df_combined['cost']

    # Profit
    df_combined['profit'] = df_combined['net_sales'] - df_combined['cogs']

    # New Flag: Identify high shipping costs (using numpy.where for efficiency)
    df_combined['high_shipping_flag'] = np.where(
        df_combined['shipping_cost'] > 40, 'Flagged', 'Normal'
    )

    # Extract Time Components
    df_combined['order_year'] = df_combined['order_date'].dt.year
    df_combined['order_month'] = df_combined['order_date'].dt.month

    print("Merging and feature engineering complete.")
    return df_combined


# --- 3. MAIN EXECUTION ---

def main():
    data_sources = load_and_clean_data()
    if data_sources is None: return

    df_final_fact = merge_and_engineer_features(data_sources)

    df_final_fact.to_csv(OUTPUT_FILE, index=False)
    print(f"\n--- ETL SUCCESS! Final dataset saved to {OUTPUT_FILE} ---")


if __name__ == '__main__':
    main()
