from database import create_connection, create_table, add_transactions, fetch_transactions
from parse_input import parse_input_file, parse_coa_file
from model import ledger_generator
from display import print_ledger
import pandas as pd

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
    print(parsed_actors)
    for actor in parsed_actors:
        print(actor.accounts)

    ledger_generator(conn, parsed_actors, accounts, start_month, end_month)



if __name__ == "__main__":
    main()

