'''JsonStorage type = key/value'''
#I will add some code, that was recomended to use
import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
local_storage = {}
args = parser.parse_args().__dict__#added arguments in variable
with open(storage_path, 'w') as f:
    pass
if args['value'] is None:
    #Search for value
    pass
else:
    #Add new value in the file and in the local_storage
    local_storage[args["key"]] = args["value"]
    variable = json.dumps(local_storage)
    print(type(json.loads(variable)), end='')
    #Ok, it's better to go sleep