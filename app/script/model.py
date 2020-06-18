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
        return self.__temp[self.key]

    def commit(self):
        self.notation.set(value=self.value, key=self.key)



class Account(Model):
    pass

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

