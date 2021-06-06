# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
from app import find_qualifying_loans, save_qualifying_loans
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


header = ["Lender", "Max_Loan", "Amount", "Max_LTV", "Max_DTI"," Min_Credit","Score", "Interest_Rate"]

def save_csv(output_path):



# Set the output file path
    output_path = Path("qualifying_loans.csv")

# print("writing the data to a csv file..."), a print statement to verify path is working 

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
    with open(output_path, 'w') as csvfile: #use 'with open' to open a new CSV file
        csvwriter = save_csv.writer(csvfile) # create a csvwriter using the csv library
        csvwriter.writerow(header) # use the csvwriter to write the 'header' variable as the first row
        for bank_data in find_qualifying_loans:
            csvwriter.writerow(save_qualifying_loans) # use the csvwriter to write the qualifying_loans to a row in the CSV file 

# print(save_qualifying_loans) # a print statement to verify code is working
