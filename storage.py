'''JsonStorage type = key/value'''
#I will add some code, that was recomended to use
import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.json')#magic
try:
    f = open(storage_path, 'r')
except FileNotFoundError:
    f = open(storage_path, 'w')
finally:
    f.close()

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")

local_storage = {}

args = parser.parse_args().__dict__#added arguments in variable


if args['val'] is None:
    #Search for value
    with open(storage_path, 'r') as f:
        try:
            local_storage = json.load(f)#something wrong
            print(local_storage.get(args['key']))
        except json.decoder.JSONDecodeError:
            print(None)

else:
    #Add new value in the file and in the local_storage
    print(args['val'])
    with open(storage_path, 'r') as f:
        try:
            local_storage = json.load(f)
            print(local_storage)
        except json.decoder.JSONDecodeError:
            print('Error 2')
        if local_storage.get(args['key']) is None:
            local_storage[args['key']] = args['val']
        else:
            local_storage[args['key']] = local_storage[args['key']]+', '+args['val']
    with open(storage_path, 'w') as f:
        json.dump(local_storage, f)