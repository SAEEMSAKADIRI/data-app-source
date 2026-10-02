import pandas as pd
from src.process_data import transform_data

def test_transform_data():
    # Setup test data
    input_data = pd.DataFrame({
        'category': ['A', 'A', 'B'],
        'value': [10, 20, 30]
    })
    
    # Execute function
    result = transform_data(input_data)
    
    # Assertions to ensure logic is correct
    assert len(result) == 2, "Should group into exactly 2 categories"
    
    # Check if category 'A' summed correctly (10 + 20 = 30)
    val_a = result[result['category'] == 'A']['value'].iloc[0]
    assert val_a == 30, f"Expected 30 for category A, got {val_a}"
