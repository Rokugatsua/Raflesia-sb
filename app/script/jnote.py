import json
import os



# Default JPath or Json Path
def jpath(json_file:str='default.json') -> str:
    " Return path of data file json "
    curdir = os.getcwd()
    if curdir.endswith('script'):
        scurdir = curdir.split('/')
        return os.path.join("".join(scurdir[-1]), 'data', json_file)
    else:
        return os.path.join(curdir, 'app', 'data', json_file)

# __setting path__
setting_path = jpath('setting.json')

class jset:
    """read and write json setting file"""
    info_path = setting_path
    def __init__(self, setting_file=setting_path):
        
        self.setting_file = setting_file
        self._temp = {}

    def get(self, keys):
        "getting value with keys"
        with open(self.setting_file, 'r') as jfile:
            setting_data = json.load(jfile)

            for key, value in setting_data.items():
                self._temp[key] = value
                if key == keys:
                    return value

    def set(self, keys, values, new=False):
        "insert or update value in setting file with criteria"
        if not self._temp:
            self.get(keys)
        with open(self.setting_file, 'w') as jfile:
            if not new:
                for key in self._temp.keys():
                    if key == keys:
                        self._temp[key] = values
            else:
                self._temp[keys] = values

            if self._temp:
                json.dump(obj=self._temp, fp=jfile, indent=4)


database_path = jpath(jset().get('database'))

def jread(json_file=database_path):
    """ reading json file as generator """
    with open(json_file, 'r') as jfile:
        jdata = json.load(jfile)
        # generate key and value in json file
        for keyval in jdata.items():
            yield keyval


def jwrite(json_data:dict, json_file=database_path):
    """ write data to json """
    with open(json_file, 'w') as jfile:
        json.dump(json_data, fp=jfile, indent=4)