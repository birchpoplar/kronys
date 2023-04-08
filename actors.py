from collections import defaultdict
import pandas as pd

class Actor:
    def __init__(self, name, accounts, params, subtype):
        pass

    def process_month(self):
        pass

    def curr_status(self):
        pass

    def report_record(self):
        pass


class Customer(Actor):
    def __init__(self, name, accounts, params, subtype):
        # set customer name
        self.name = name
        # set initial month to zero
        self.curr_month = 0
        # set initial parameters for customer
        self.params = params
        # set accounts
        self.accounts = accounts
        # set customer type
        self.subtype = subtype
        # create dict of lists for recording
        self.record = defaultdict(list)
        # create dict for current month activity
        self.curr_activity = {}

    def process_month(self):
        pass

    def curr_status(self):
        # Return the current status of the customer
        return self.name, self.curr_month, self.accounts, self.params, self.record
    
    def report_record(self):
        # Return a dataframe of the record plus the account names
        return self.accounts, self.record


class SingleCustomer(Customer):
    def __init__(self, name, account_list, params):
        super().__init__(name, account_list, params, "Single")

    def process_month(self):
        # Function to process a single month for a single customer
        # *** NOTE: this function may need to return an actors list, for actors created by this function
        
        # define 
        actors = []

        # update month
        self.curr_month += 1
        
        # apply revenue
        if self.curr_month == self.params['start_month']:
            self.record['revenue'].append(self.params['revenue'])
            self.curr_activity['revenue'] = self.params['revenue']
        else:
            self.record['revenue'].append(0)
            self.curr_activity['revenue'] = 0

        # apply receivable
        if self.curr_month >= self.params['start_month']: 
            self.record['receivable'].append(self.params['revenue'])
            if self.curr_month == self.params['start_month']:
                self.curr_activity['receivable'] = self.params['revenue']
            else:
                self.curr_activity['receivable'] = 0
        else:
            self.record['receivable'].append(0)
            self.curr_activity['receivable'] = 0

        return self.curr_activity, self.record


class MultipleCustomer(Customer):
    def __init__(self, name, account_list, params):
        super().__init__(name, account_list, params, "Multiple")

    def process_month(self):
        # Function to process a single month for a recurring, multiple month customer
        
        # update month
        self.curr_month += 1
        
        # apply revenue
        if self.curr_month >= self.params['start_month'] and self.curr_month <= self.params['start_month'] + self.params['length']:
            self.record['revenue'].append(self.params['revenue'])
            self.curr_activity['revenue'] = self.params['revenue']
        else:
            self.record['revenue'].append(0)
            self.curr_activity['revenue'] = 0

        # apply receivable
        if self.curr_month >= self.params['start_month'] and self.curr_month <= self.params['start_month'] + self.params['length']:  
            self.record['receivable'].append(self.params['revenue'] * (self.curr_month - self.params['start_month'] + 1))
            self.curr_activity['receivable'] = self.params['revenue']
        else:
            self.record['receivable'].append(0)
            self.curr_activity['receivable'] = 0

        return self.curr_activity, self.record


class Receivable(Actor):
    def __init__(self, name, accounts, params, subtype):
        # set customer name
        self.name = name
        # set initial month to zero
        self.curr_month = 0
        # set initial parameters for customer
        self.params = params
        # set accounts
        self.accounts = accounts
        # set customer type
        self.subtype = subtype
        # create dict of lists for recording
        self.record = defaultdict(list)
        # create dict for current month activity
        self.curr_activity = {}
