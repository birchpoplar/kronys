from database import create_connection, create_table, add_transactions, fetch_transactions
from parse_input import parse_input_file, parse_coa_file
from model import ledger_generator
from display import print_ledger, print_status_message, print_header
from rich.console import Console
import pandas as pd
import openpyxl
import os
from export import fetch_transactions_to_df, income_statement_dataframe, balance_sheet_dataframe, create_excel_file, add_total_row

def main():
    database = "financial_statement_projection.db"
    conn = create_connection(database)

    console = Console()
    print_header(console)

    print_status_message(console, "Initial parameters set.", "complete")
    start_month = 1
    end_month = 12


    # Check if the file exists
    if os.path.exists(database):
        console.print("[bold red]Warning:[/bold red] The file 'financial_statement_projection.db' already exists.")
        user_input = input("Do you want to delete the existing file and create a new one? (yes/no) [yes]: ")
        if user_input.lower() == "no":
            print_status_message(console, "Aborted. The existing file will not be deleted.", "error")
            exit()
        else:
            os.remove(database)
            print_status_message(console, "Existing file deleted.", "complete")

    conn = create_connection(database)

    if conn is not None:
        create_table(conn)
        print_status_message(console, "General ledger table created.", "complete")
    else:
        print_status_message(console, "Error! Cannot create the database connection.", "error")
        exit()

    print_status_message(console, "Database connection established.", "complete")

    input_file = "main.coa"
    accounts = parse_coa_file(input_file)

    input_file = "input.yaml"
    parsed_actors = parse_input_file(input_file)

    ledger_generator(conn, parsed_actors, accounts, start_month, end_month, console)

    # print_ledger(conn)

    transactions = fetch_transactions_to_df(conn)
    
    income_statement = income_statement_dataframe(accounts, transactions, start_month, end_month)
    print(income_statement)

    balance_sheet = balance_sheet_dataframe(accounts, transactions, start_month, end_month)
    print(balance_sheet)

    create_excel_file(income_statement, 'income_statement.xlsx', start_month, end_month)

    # Load or create your workbook and worksheet
    workbook = openpyxl.load_workbook('income_statement.xlsx')
    worksheet = workbook.active

    # Get the row number for the totals row
    total_row_num = worksheet.max_row + 1

    # Add the totals row
    add_total_row(worksheet, total_row_num)

    # Save the workbook
    workbook.save('income_statement_with_totals.xlsx')

if __name__ == "__main__":
    main()

