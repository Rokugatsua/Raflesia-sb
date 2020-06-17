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
    info_path = setting_path
    def __init__(self, setting_file=setting_path):
        self.setting_file = setting_file

    def get(self, keys):
        "getting value with keys"
        with open(self.setting_file, 'r') as jfile:
            setting_data = json.load(jfile)

            for key, value in setting_data.items():
                if key == keys:
                    return value
