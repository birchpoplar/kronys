from database import create_connection, create_table, add_transactions, fetch_transactions
from parse_input import parse_input_file, parse_coa_file
from model import ledger_generator
from display import print_ledger
import pandas as pd
import openpyxl
from export import fetch_transactions_to_df, income_statement_dataframe, balance_sheet_dataframe, create_excel_file, add_total_row

def main():
    database = "financial_statement_projection.db"
    conn = create_connection(database)

    start_month = 1
    end_month = 12

    if conn is not None:
        create_table(conn)
        print("General ledger table created.")
    else:
        print("Error! Cannot create the database connection.")


    input_file = "main.coa"
    accounts = parse_coa_file(input_file)

    input_file = "input.yaml"
    parsed_actors = parse_input_file(input_file)

    ledger_generator(conn, parsed_actors, accounts, start_month, end_month)

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

