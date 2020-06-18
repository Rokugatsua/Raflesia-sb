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




class Account(Model):
    pass

class Income(Model):
    val_type = list()

    def add(self, value):
        self.val_type.append(value)

    def adds(self, values:list):
        if type(values) == list:
            self.val_type.extend(values)

    def delete(self, value:list):
        if value in self.value:
            try:
                self.value.remove(value)
            except:
                print(f"{value} not exists")


