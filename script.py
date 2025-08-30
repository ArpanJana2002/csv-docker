import pandas as pd
import os

def process_data(file_path):
    """Process and analyze measurements data from CSV or Excel file"""
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found!")
        return
    
    try:
        # Read the data file into a DataFrame
        print(f"Loading data from: {file_path}")
        
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Use CSV or Excel files.")
        
        print(f"Successfully loaded {len(df)} rows and {len(df.columns)} columns\n")
        
        # Display dataset info
        print("=== DATASET INFORMATION ===")
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        
        # Display the first few rows of the DataFrame
        print("\n=== FIRST 5 ROWS ===")
        print(df.head())
        
        # Display data types
        print("\n=== DATA TYPES ===")
        print(df.dtypes)
        
        # Display summary statistics of the DataFrame
        print("\n=== SUMMARY STATISTICS ===")
        print(df.describe())
        
        # Check for missing values in the DataFrame
        print("\n=== MISSING VALUES ===")
        missing_values = df.isnull().sum()
        print(missing_values)
        
        if missing_values.sum() == 0:
            print("✅ No missing values found!")
        else:
            print(f"⚠️  Total missing values: {missing_values.sum()}")
            
    except Exception as e:
        print(f"Error processing file: {e}")
        return

if __name__ == "__main__":
    process_data("Data/measurements.csv")
