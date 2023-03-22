class Customer:
    def __init__(self, name, account, month, subtype):
        self.name = name
        self.account = account
        self.month = month
        self.subtype = subtype

    def __repr__(self):
        return f"Customer(name={self.name}, account={self.account}, month={self.month}, subtype={self.subtype})"

class SingleCustomer(Customer):
    def __init__(self, name, account, month, revenue):
        super().__init__(name, account, month, "Single")
        self.revenue = revenue

    def __repr__(self):
        return f"SingleCustomer(name={self.name}, account={self.account}, month={self.month}, revenue={self.revenue})"

class MultipleCustomer(Customer):
    def __init__(self, name, account, month, length, revenue):
        super().__init__(name, account, month, "Multiple")
        self.length = length
        self.revenue = revenue

    def __repr__(self):
        return f"MultipleCustomer(name={self.name}, account={self.account}, month={self.month}, length={self.length}, revenue={self.revenue})"

class Vendor:
    def __init__(self, name, account, month, expense):
        self.name = name
        self.account = account
        self.month = month
        self.expense = expense

    def __repr__(self):
        return f"Vendor(name={self.name}, account={self.account}, month={self.month}, revenue={self.expense})"

