from database import fetch_transactions

def print_ledger(conn):
    transactions = fetch_transactions(conn)
    if not transactions:
        print("No transactions found in the general ledger.")
        return

    header = ("ID", "Date", "Account", "Matching Account", "Name", "Reference", "Debit", "Credit")
    row_format = "{:<5} {:<10} {:<20} {:<20} {:<15} {:<25} {:<8} {:<8}"
    print(row_format.format(*header))

    for transaction in transactions:
        print(row_format.format(*transaction))