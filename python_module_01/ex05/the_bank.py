class Account(object):
    
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account:  Account() new account to append
            @return   True if success, False if an error occured
        """
        
        if not isinstance(new_account, Account):
            return False
        if any(i.name == new_account.name for i in self.accounts):
            return False
        self.accounts.append(new_account)
        return True

    def validate_account(self, test_acc):
        obj = next((x for x in self.accounts if x.name == test_acc), None)
        attr = obj.__dict__.keys()
        if obj is None:
            return False
        print(attr)
        if len(attr) % 2 == 0:
            return False
        print('Got here!')
        if next((x for x in attr if x.startswith('b')), None):
            return False
        if not next((x for x in attr if x.startswith('zip') or x.startswith('addr')), None):
            return False
        if not next((x for x in attr if x == 'name' and isinstance(getattr(obj,x), str)), None):
            return False
        if not next((x for x in attr if x == 'id' and isinstance(getattr(obj,x), int)), None):
            return False
        if not next((x for x in attr if x == 'value' and isinstance(getattr(obj,x), (int, float))), None):
            return False
        return True

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
        if not isinstance(origin, str) or not isinstance(dest, str):
            return False
        if not isinstance(amount, (int, float)) or amount < 0:
            return False
        if not Bank.validate_account(self, origin) or not Bank.validate_account(self, dest):
            return False
        if amount > next((x for x in self.accounts if x.name == origin)).value:
            return False
        if origin == dest:
            return True
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        if next((x for x in self.accounts if x.name == name), None) is None:
            return False

        # Fixing account
        obj = next((x for x in self.accounts if x.name == name), None)
        attr = obj.__dict__.keys()
        if len(attr) % 2 == 0:
            obj.fixinglen = 'default'
        if not next((x for x in attr if x.startswith('zip') or x.startswith('addr')), None):
            obj.zip = 'default'
        if not next((x for x in attr if x == 'name' and isinstance(getattr(obj,x), str)), None):
            obj.name = 'default'
        if not next((x for x in attr if x == 'id' and isinstance(getattr(obj,x), int)), None):
            obj.id = Account.ID_COUNT
        if not next((x for x in attr if x == 'value' and isinstance(getattr(obj,x), (int, float))), None):
            obj.value = 0
        for x in attr:
            if x.startswith('b'): delattr(obj, x) 
        return True
        