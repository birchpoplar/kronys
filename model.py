from struct_defs import Event
from database import add_transactions
from actors import SingleCustomer, MultipleCustomer
from database import fetch_transactions
import pandas as pd

def ledger_generator(conn, actors, accounts, start_month, end_month):
    transactions = []

    for month in range(start_month, end_month):
        for actor in actors:
            curr_activity, _ = actor.process_month()
            first_key = 0
            for key, value in curr_activity.items():
                if first_key == 0:
                    main_account = actor.accounts[key]
                    first_key = 1
                else:
                    matching_account = actor.accounts[key]

            if get_account_type_by_number(accounts, actor.accounts[main_account]) == "CR":
                main_transaction = (
                    month,
                    main_account,
                    matching_account,
                    actor.name,
                    0,
                    
                    )
            # Main transaction entry
            main_transaction = (
                month,
                e,
                event.matching_account,
                event.name,
                event.reference,
                0,
                event.amount,
            )    
            transactions.append(main_transaction)
                    

            transactions.append(matching_transaction) 

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


