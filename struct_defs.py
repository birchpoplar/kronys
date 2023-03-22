class Event:
    def __init__(self, event_date, name, reference, amount, account, matching_account):
        self.event_date = event_date
        self.name = name
        self.reference = reference
        self.amount = amount
        self.account = account
        self.matching_account = matching_account

    def __str__(self):
        return f"{self.event_date}, {self.name}, {self.reference}, {self.amount}, {self.account}, {self.matching_account}"

    def __repr__(self):
        return self.__str__()
    
class Account:
    def __init__(self, account_number, account_name, description, type, category):
        self.account_number = account_number
        self.account_name = account_name
        self.description = description
        self.type = type
        self.category = category

    def __repr__(self):
        return f"Account(account_number={self.account_number}, account_name={self.account_name}, description={self.description}, type={self.type}, category={self.category})"
