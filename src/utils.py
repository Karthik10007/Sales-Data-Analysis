import pandas as pd

def load_data(file_path):
    try:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        print(data.head())
        return data
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return None