import csv


def count_rows_columns(csv_file):
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
        num_rows = len(rows) - 1  # Exclude header
        num_columns = len(rows[0]) if rows else 0
        print(f"Total rows (excluding header): {num_rows}")
        print(f"Total columns: {num_columns}")
# Usage


count_rows_columns('/Users/khush/Downloads/spotify-2023.csv')
