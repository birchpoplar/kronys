import re
import csv
from actors import Customer, SingleCustomer, MultipleCustomer, Vendor
from struct_defs import Account

def parse_single_customer_data(match):
    name, account, month, revenue = match.groups()
    return SingleCustomer(name, int(account), int(month), int(revenue))

def parse_multiple_customer_data(match):
    name, account, month, length, revenue = match.groups()
    return MultipleCustomer(name, int(account), int(month), int(length), int(revenue))

def parse_vendor_data(match):
    name, account, month, expense = match.groups()
    return Vendor(name, int(account), int(month), int(expense))

def parse_input_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

    patterns = [
        (re.compile(r'Customer\s*{(?:\s*name:\s*(\w+),\s*subtype:\s*Single,\s*account:\s*(\w+),\s*month:\s*(\d+),\s*revenue:\s*(\d+)\s*)}'), parse_single_customer_data),
        (re.compile(r'Customer\s*{(?:\s*name:\s*(\w+),\s*subtype:\s*Multiple,\s*account:\s*(\w+),\s*month:\s*(\d+),\s*length:\s*(\d+),\s*revenue:\s*(\d+)\s*)}'), parse_multiple_customer_data),
        (re.compile(r'Vendor\s*{(?:\s*name:\s*(\w+),\s*account:\s*(\w+),\s*month:\s*(\d+),\s*expense:\s*(\d+)\s*)}'), parse_vendor_data),
    ]

    actors = []
    for pattern, parse_func in patterns:
        matches = pattern.finditer(content)
        for match in matches:
            actor = parse_func(match)
            actors.append(actor)
    print(actors)

    return actors

def parse_coa_file(file_path):
    accounts = []

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            account_number = int(row['account_number'])
            account_name = row['account_name']
            description = row['description']
            type = row['type']
            category = row['category']

            account = Account(account_number, account_name, description, type, category)
            accounts.append(account)

    return accounts