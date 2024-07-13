import pandas as pd
import matplotlib.pyplot as plt

def read_csv(file_path):
    return pd.read_csv(file_path)

def calculate_summary_statistics(df):
    return df.describe()

def plot_sales(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['sales'], marker='o')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title('Sales Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()