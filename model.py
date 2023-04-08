from database import add_transactions
from actors import SingleCustomer, MultipleCustomer
from database import fetch_transactions
import pandas as pd
from display import print_status_message, print_header
from rich.console import Console

def ledger_generator(conn, actors, accounts, start_month, end_month, console: Console):
    transactions = []

    print_status_message(console, "Generating ledger...", "processing")
    for month in range(start_month, end_month):
        for actor in actors:
            curr_activity, _ = actor.process_month()
            tacc_entry, tacc = [], []
            for key, value in curr_activity.items():
                acc_number = actor.accounts[key]
                # Build t-account entry as list with account number, debit, credit
                tacc_entry.append(acc_number)
                if get_account_type_by_number(accounts, acc_number) == "DR":
                    if value >0:
                        tacc_entry.append(value)
                        tacc_entry.append(0)
                    elif value < 0:
                        tacc_entry.append(0)
                        tacc_entry.append(value)
                    else:
                        # Skip this entry as zero value
                        pass                   
                elif get_account_type_by_number(accounts, acc_number) == "CR":
                    if value >0:
                        tacc_entry.append(0)
                        tacc_entry.append(value)
                    elif value < 0:
                        tacc_entry.append(value)
                        tacc_entry.append(0)
                    else:
                        # Skip this entry as zero value
                        pass

                # Now append the t-account entry to the t-account list
                if len(tacc_entry) == 3:
                    tacc.append(tacc_entry)
                tacc_entry = []

            # By this point we should have a t-account list of two entries for an actor for the month
            # Now process the t-account list to create the transactions
            if len(tacc) == 2:
                # Create a transaction entry
                transaction = []
                # Add the month
                transaction.append(month)
                # Add the debit account
                transaction.append(tacc[0][0])
                # Add the credit account
                transaction.append(tacc[1][0])
                # Add the name
                transaction.append(actor.name)
                # Add the reference
                transaction.append(0)
                # Add the debit amount
                transaction.append(tacc[0][1])
                # Add the credit amount
                transaction.append(tacc[1][1])
                # Add the transaction to the list of transactions
                transactions.append(transaction)
                # Now create the matching transaction to above
                transaction = []
                # Add the month
                transaction.append(month)
                # Add the debit account
                transaction.append(tacc[1][0])
                # Add the credit account
                transaction.append(tacc[0][0])
                # Add the name
                transaction.append(actor.name)
                # Add the reference
                transaction.append(0)
                # Add the debit amount
                transaction.append(tacc[1][1])
                # Add the credit amount
                transaction.append(tacc[0][1])
                # Add the transaction to the list of transactions
                transactions.append(transaction)
            else:
                pass

    # Now add the transactions to the database
    add_transactions(conn, transactions)


def get_account_type_by_number(accounts, account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account.type
    return None

def get_account_number_by_name(accounts, account_name):
    for account in accounts:
        if account.account_name == account_name:
            return account.account_number
    return None


