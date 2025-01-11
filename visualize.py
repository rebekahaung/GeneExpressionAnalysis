import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_visualizations(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        
        numeric_data = data.select_dtypes(include=['number', 'float64', 'int64'])
        
    
        if numeric_data.empty:
            print("No numeric data found for visualization.")
        else:
            # Heat map
            plt.figure(figsize=(10, 8))
            sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm")
            plt.title("Correlation Heatmap")
            plt.xlabel("Genes")
            plt.ylabel("Genes")
            plt.savefig("results/heatmap.png")
            print("Heatmap saved to 'results/heatmap.png'.")
            plt.close()
            
            # Box plot
            plt.figure(figsize=(10, 6))
            sns.boxplot(data=numeric_data)
            plt.title("Boxplot of Gene Expression")
            plt.xlabel("Gene Samples")
            plt.ylabel("Expression Level")
            plt.savefig("results/boxplot.png")
            print("Boxplot saved to 'results/boxplot.png'.")
            plt.close()
            
            # Bar plot
            plt.figure(figsize=(10, 6))
            sns.barplot(data=numeric_data.mean(axis=0).reset_index(), x=0, y='index', ci=None)
            plt.xlabel("Average Gene Expression Level")
            plt.ylabel("Samples")
            plt.title("Barplot of Gene Expression Averages")
            plt.savefig("results/barplot.png")
            print("Barplot saved to 'results/barplot.png'.")
            plt.close()
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_visualizations("data/processed_expression_data.csv")
