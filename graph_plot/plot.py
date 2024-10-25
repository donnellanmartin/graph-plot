import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data from a CSV file
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None

# Step 2: Process the data
def process_data(data):
    # Group by category and sum the values (if needed)
    processed_data = data.groupby('Category')['Value'].sum().reset_index()
    return processed_data

# Step 3: Visualize the data
def visualize_data(processed_data):
    plt.bar(processed_data['Category'], processed_data['Value'], color='skyblue')
    plt.title('Category Values')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function to orchestrate the steps
def main():
    file_path = 'data.csv'
    data = load_data(file_path)

    if data is not None:
        processed_data = process_data(data)
        visualize_data(processed_data)

if __name__ == "__main__":
    main()
