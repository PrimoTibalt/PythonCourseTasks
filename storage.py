'''JsonStorage type = key/value'''
#I will add some code, that was recomended to use
import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')#magic

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")

local_storage = {}

args = parser.parse_args().__dict__#added arguments in variable


if args['value'] is None:
    #Search for value
    with open(storage_path, 'r+', encoding='utf-8') as f:
        try:
            local_storage = json.load(f)#something wrong
            print(local_storage.get(args['key'], None))
        except json.decoder.JSONDecodeError:
            print('Error with reading from a file')
else:
    #Add new value in the file and in the local_storage
    print(args['value'])
    with open(storage_path, 'r+', encoding='utf-8') as f:
        try:
            local_storage = json.load(f)
        except json.decoder.JSONDecodeError:
            print('Error with writing in a file')
        if local_storage.get(args['key']) is None:
            local_storage[args['key']] = args['value']
        else:
            local_storage[args['key']] = [local_storage[args['key']], args['value']]
        json.dump(local_storage, f)