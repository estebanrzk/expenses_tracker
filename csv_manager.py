import pandas as pd
import os

file_path = 'data/expenses.csv'
expenses_columns = ['id', 'name', 'amount', 'category', 'time', 'description']

def initiator():
    # Create data directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Initialize CSV with headers if file doesn't exist
    if not os.path.exists(file_path):
        pd.DataFrame(columns=expenses_columns).to_csv(file_path, index=False)

def read_csv():
    return pd.read_csv(file_path)

def save_data(new_expense):
    # Read existing data or create empty DataFrame
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame(columns=expenses_columns)
    
    # Generate new ID
    new_id = df['id'].max() + 1 if not df.empty else 1
    new_expense['id'] = new_id
    
    # Append new data and save
    updated_df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
    updated_df.to_csv(file_path, index=False)


