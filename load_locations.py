import pandas as pd
import csv 


def convert_excel_to_csv():
    # Load the Excel file
    df = pd.read_excel("your_file.xlsx", sheet_name=0)  # Change sheet_name if needed

    # Save as CSV
    df.to_csv("your_file.csv", index=False)


with open("locations.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["place"], end=" ")
        print(row["somethingzip"])  # Access column by name
