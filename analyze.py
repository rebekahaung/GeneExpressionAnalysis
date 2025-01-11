import pandas as pd

def analyze_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        
        numeric_data = data.select_dtypes(include=['number', 'float64', 'int64'])

        if numeric_data.empty:
            print("No numeric data found for analysis.")
        else:
            summary = numeric_data.describe()
            print("Summary statistics:")
            print(summary)
            
            summary.to_csv("results/summary_statistics.csv")
            print("Summary statistics saved to 'results/summary_statistics.csv'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    analyze_data("data/processed_expression_data.csv")