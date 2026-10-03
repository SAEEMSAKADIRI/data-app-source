import pandas as pd
import datetime
import os

def transform_data(df):
    """Groups data by category and calculates the total value."""
    return df.groupby('category', as_index=False)['value'].sum()

if __name__ == "__main__":
    print("Initializing data processing job...") 
    
    raw_data = {
        'category': ['Analytics', 'Engineering', 'Analytics', 'Engineering', 'Sales', 'Marketing'],
        'value': [120, 300, 150, 200, 400, 250]
    }
    df = pd.DataFrame(raw_data)
    
    print(f"Raw data loaded:\n{df}\n")
    processed_df = transform_data(df)
    print(f"Transformation complete. Aggregated output:\n{processed_df}")
    
    # LOGGING LOGIC
    log_dir = "/app/logs"
    # Check if the volume directory exists before writing
    if os.path.exists(log_dir):
        log_file = os.path.join(log_dir, "execution_log.txt")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Append mode ("a") ensures we add a new line every time
        with open(log_file, "a") as f:
            f.write(f"[{timestamp}] Jenkins executed data processing job successfully!\n")
            
    print("Job finished successfully.")
