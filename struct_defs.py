class Account:
    def __init__(self, account_number, account_name, description, type, category):
        self.account_number = account_number
        self.account_name = account_name
        self.description = description
        self.type = type
        self.category = category

    def __repr__(self):
        return f"Account(account_number={self.account_number}, account_name={self.account_name}, description={self.description}, type={self.type}, category={self.category})"
