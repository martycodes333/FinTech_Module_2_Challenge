# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
# from pathlib import Path


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




def save_csv(output_path, qualifying_loans):
    '''Saves the qualifying loans as a CSV file.
    
        Args:
            with open(csvpath) Open a csvfile path
            csvwriter: write the data to the csvfile
            qualifying loans (list of lists): a list of the rows of data for the new CSV file
            header (list): write a header for the new CSV list being saved
            csvwriter

        Returns: 
            A saved CSV file at the user-specified file name (.csv) and directory
        
 
        
    '''
    header = ["Lender", "Max_Loan", "Amount", "Max_LTV", "Max_DTI"," Min_Credit_Score", "Interest_Rate"] 


    with open(output_path, 'w', newline="") as csvfile: #use 'with open' to open a new CSV file
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(header) 
        csvwriter.writerows(qualifying_loans)
    

