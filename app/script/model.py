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



class Account(Model):
    def __init__(self, val_type):
        super().__init__()
        self.val_type = val_type

    def new_init(self):
        super().new_init(self.val_type)

    def add_category(self, key:str):
        key.lower()
        if key not in self.value:
            self.value[key] = {}
        else:
            print(f"'{key}' already exist")

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

    def delete(self, value:list):
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
    def __init__(self, val_type):
        super().__init__()
        self.val_type = val_type
    
    def new_init(self):
        super().new_init(self.val_type)