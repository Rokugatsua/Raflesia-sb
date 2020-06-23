from typing import NewType

from app.script import jnote

class Model(object):
    def __init__(self, notation=jnote.Notation):
        self.key = str(type(self).__name__).lower()
        self.notation = notation(self.key)
        self.__temp = self.notation.get(self.key)

    def items(self) -> dict:
        return self.__temp

    def new_init(self, val_type=dict()):
        if not self.items():
            self.notation.set(value=val_type, key=self.key, new=True)
        else:
            print(self.key, 'already exists')

    @property
    def value(self):
        f"get value from '{self.key}' key"
        try:
            return self.__temp[self.key]
        except KeyError as e:
            print(f"'{e}' not found on database" )

    def commit(self):
        self.notation.set(value=self.value, key=self.key)

def sync(tipe, account, ctg, amount):
        maccount = Account()
        ctgname, ctg2, accval, accval2 = None, None, 0, 0
        for key, val in maccount.value.items():
            if account in val.keys():
                ctgname = key
                accval = val[account]
            if ctg in val.keys():
                ctg2 = val
                accval2 = val[ctg]
        
        if tipe == 'expense':
            
            maccount.update_account(account,(accval - amount), ctgname)
        elif tipe == 'income':
            maccount.update_account(account,(accval + amount), ctgname)
        elif tipe == 'transfer':
            maccount.update_account(account,(accval - amount), ctgname)
            maccount.update_account(ctg,(accval2 + amount), ctg2)
        else:
            print('tipe not found')

        maccount.commit()

class Account(Model):
    def __init__(self):
        super().__init__()
        self.val_type = dict()

    def new_init(self):
        super().new_init(self.val_type)

    def add_category(self, key:str):
        try:
            if key not in self.value:
                self.value[key] = {}
            else:
                print(f"'{key}' already exist")
        except:
            print(f"'{key}' not found")

    def delete_category(self, key:str):
        key.lower()
        if key in self.value:
            del self.value[key]
        else:
            print(f"'{key}' not found")

    def edit_category(self, old_key:str, new_key:str):
        old_key.lower()
        new_key.lower()
        val = {}
        if old_key in self.value and new_key not in self.value:
            val = self.value[old_key]
            self.value[new_key] = val

            del self.value[old_key]

    def add_account(self, key:str, value:int, category:str):
        key.lower()
        try:
            if key not in self.value[category.lower()]:
                self.value[category][key] = value
            else:
                print(f"'{key}' already exist")
        except:
            print(f"'{category}' not found")

    def delete_account(self, key:str, category:str):
        key.lower()
        try:
            if key in self.value[category.lower]:
                del self.value[category][key]
            else:
                print(f"'{key}' not found")
        except:
            print(f"'{category}' not found")                

    def edit_account(self, old_key:str, new_key:str, category:str):
        old_key.lower()
        new_key.lower()
        val = {}
        try:
            if old_key in self.value[category.lower()] \
                and new_key not in self.value[category.lower()]:
                val = self.value[category][old_key]
                self.value[category][new_key] = val

                del self.value[old_key]
        except:
            print(f"'{category}' not found")

    def update_account(self, key:str, value:int, category:str):
        key.lower()
        try:
            if key in self.value[category.lower()]:
                self.value[category][key] =  value
        except:
            print(f"'{category}' not found")
        

class Income(Model):
    def add(self, value):
        if value not in self.value:
            self.value.append(value)
        else:
            print(f"'{value}' already exist")

    def adds(self, values:list):
        if type(values) == list:
            temp = list()
            for value in values:
                if value not in self.value:
                    self.value.append(value)
                else:
                    temp.append(value)
            if temp:
                print(f"{temp} already exist")

    def delete(self, value):
        if value in self.value:
            try:
                self.value.remove(value)
            except:
                pass
        else:
            print(f"'{value}' not exists")
        

    def edit(self, old_value, new_value):
        if old_value in self.value and new_value not in self.value:
            index = self.value.index(old_value)
            self.value[index] = new_value

class Expense(Income):
    pass

class Budget(Model):
    def __init__(self):
        super().__init__()
        self.val_type = dict()
    
    def new_init(self):
        super().new_init(self.val_type)

class Transaction(Model):
    def __init__(self):
        super().__init__()
        self.val_type = list()
        self.account = Account()

    def new_init(self):
        super().new_init(self.val_type)

    def add(self, date, account, category, content, amount, tipe):
        if date and account and category and content and amount:
            value = {}
            value['_id'] = self.value[-1]['_id'] + 1
            value['date'] = date
            value['content'] = content
            value['account'] = account
            value['category'] = category
            if tipe == 'expense':
                value['amount'] = -amount
            else:
                value['amount'] = amount
            self.value.append(value)
            self.commit()
            self.sync(tipe, account, category, amount)
        else:
            print("fill all value")

    def delete(self, id):
        if id:
            try:
                self.value.pop(id)
            except:
                print("id not exists")


    def sync(self, tipe, account, ctg, amount):
        sync(tipe,account,ctg,amount)