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
