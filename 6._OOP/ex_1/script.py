class Bank:
    def __init__(self):
        self.accounts = []


class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust


class Customer:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        else:
            self.name = args[0]
            self.age = args[1]

 #   def __repr__(self):
 #       return self.name

 #   def __str__(self):
 #       pass
