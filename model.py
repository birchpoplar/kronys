from struct_defs import Event
from database import add_transactions
from actors import SingleCustomer, MultipleCustomer, Vendor

def single_customer_event_generator(customer):
    events = []
    event_date = customer.month
    name = customer.name
    reference = f"INV-{customer.name}-{customer.month}"
    amount = customer.revenue
    account = customer.account
    matching_account = 1001

    event = Event(event_date, name, reference, amount, account, matching_account)
    events.append(event)

    return events

def multiple_customer_event_generator(customer):
    events = []
    event_date = customer.month
    name = customer.name
    amount = customer.revenue
    account = customer.account
    matching_account = 1001

    for month in range(customer.month, customer.month + customer.length):
        event = Event(month, name, f"INV-{customer.name}-{month - customer.month}", amount, account, matching_account)
        events.append(event)

    return events

def event_generator(actors):
    events = []
    
    for actor in actors:
        if isinstance(actor, SingleCustomer):
            customer_events = single_customer_event_generator(actor)
            events.extend(customer_events)
        elif isinstance(actor, MultipleCustomer):
            customer_events = multiple_customer_event_generator(actor)
            events.extend(customer_events)
        else:
            raise ValueError("Unknown actor type")

    return events

def ledger_generator(conn, events, accounts, start_month, end_month):
    transactions = []

    for month in range(start_month, end_month):
        for event in events:
            if event.event_date == month:
                if get_account_type_by_number(accounts, event.account) == "CR":
                    # Main transaction entry
                    main_transaction = (
                        event.event_date,
                        event.account,
                        event.matching_account,
                        event.name,
                        event.reference,
                        0,
                        event.amount,
                    )    
                    transactions.append(main_transaction)
                    
                    # Matching transaction entry
                    matching_transaction = (
                        event.event_date,
                        event.matching_account,
                        event.account,
                        event.name,
                        event.reference,
                        event.amount,
                        0,
                    )
                    transactions.append(matching_transaction)            
        
    # print(transactions)

    add_transactions(conn, transactions)

def get_account_type_by_number(accounts, account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account.type
    return None
