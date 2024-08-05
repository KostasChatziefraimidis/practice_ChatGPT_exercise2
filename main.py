from data_analysis import read_csv, calculate_summary_statistics, plot_sales


def main():
    # Read the CSV file
    file_path = 'data.csv'
    df = read_csv(file_path)

    # Calculate summary statistics
    summary = calculate_summary_statistics(df)
    print("Summary Statistics:")
    print(summary)

    # Plot the sales data
    plot_sales(df)


if __name__ == "__main__":
    main()

#end of exercise 2