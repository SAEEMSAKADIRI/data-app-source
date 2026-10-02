import pandas as pd

def transform_data(df):
    """Groups data by category and calculates the total value."""
    return df.groupby('category', as_index=False)['value'].sum()

if __name__ == "__main__":
    print("Initializing data processing job...")
    
    # Simulating data extraction
    raw_data = {
        'category': ['Analytics', 'Engineering', 'Analytics', 'Engineering', 'Sales'],
        'value': [120, 300, 150, 200, 400]
    }
    df = pd.DataFrame(raw_data)
    
    print(f"Raw data loaded:\n{df}\n")
    
    # Simulating data transformation
    processed_df = transform_data(df)
    
    print(f"Transformation complete. Aggregated output:\n{processed_df}")
    print("Job finished successfully.")
