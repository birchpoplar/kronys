import sqlite3
from sqlite3 import Error

def create_connection(database):
    """Create a database connection to the SQLite database specified by the database file."""
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    """Create the general ledger table."""
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS general_ledger (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        month NUMBER NOT NULL,
        account NUMBER NOT NULL,
        matching_account NUMBER NOT NULL,
        name TEXT,
        reference TEXT,
        debit REAL NOT NULL,
        credit REAL NOT NULL
    );
    """

    try:
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
    except Error as e:
        print(e)

def add_transaction(conn, transaction):
    """Insert a transaction into the general ledger table."""
    sql_insert_transaction = """
    INSERT INTO general_ledger (date, account, matching_account, name, reference, debit, credit)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    """
    cursor = conn.cursor()
    cursor.execute(sql_insert_transaction, transaction)
    conn.commit()
    return cursor.lastrowid

def add_transactions(conn, transactions):
    """Insert multiple transactions into the general ledger table."""
    for transaction in transactions:
        add_transaction(conn, transaction)

def fetch_transactions(conn):
    """Fetch all transactions from the general ledger table."""
    sql_fetch_transactions = "SELECT * FROM general_ledger;"
    cursor = conn.cursor()
    cursor.execute(sql_fetch_transactions)
    transactions = cursor.fetchall()
    return transactions