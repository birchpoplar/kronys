from database import create_connection, create_table, add_transactions, fetch_transactions
from parse_input import parse_input_file, parse_coa_file
from model import event_generator, ledger_generator
from display import print_ledger

def main():
    database = "financial_statement_projection.db"
    conn = create_connection(database)

    start_month = 1
    end_month = 36

    if conn is not None:
        create_table(conn)
        print("General ledger table created.")
    else:
        print("Error! Cannot create the database connection.")

    input_file = "input.mdl"
    parsed_actors = parse_input_file(input_file)
    print(parsed_actors)

    file_path = 'main.coa'
    accounts = parse_coa_file(file_path)

    events = event_generator(parsed_actors)
    for event in events:
        print(event)

    ledger_generator(conn, events, accounts, start_month, end_month)
    print_ledger(conn)

if __name__ == "__main__":
    main()

