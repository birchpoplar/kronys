import csv
from actors import Customer, SingleCustomer, MultipleCustomer
from struct_defs import Account
import yaml


def parse_input_file(filename):
    with open(filename, 'r') as file:
        content = yaml.safe_load(file)

    actors = []
    for entry in content:
        main_type = entry['type']
        subtype = entry['subtype']
        name = entry['name']
        account_list = entry['accounts']
        params = entry['params']

        if main_type == 'Customer' and subtype == 'Single':
            actor = SingleCustomer(name, account_list, params)
            actors.append(actor)
        
        if main_type == 'Customer' and subtype == 'Multiple':
            actor = MultipleCustomer(name, account_list, params)
            actors.append(actor)

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