from app.script import jnote

class Model(object):
    def __init__(self, notation=jnote.Notation):
        self.key = str(type(self).__name__).lower()
        self.notation = notation(self.key)

    def items(self) -> dict:
        return self.notation.get(self.key)

    def new_init(self, val_type=dict()):
        if not self.items():
            self.notation.set(value=val_type, key=self.key, new=True)
        else:
            print(self.key, 'already exists')

    def value(self):
        return self.items()[self.key]


class Account(Model):
    pass

class Income(Model):
    pass


