#The task is to create decorator for functions, that will make their returned values in json form
import json

def to_json(func):
    def newFunc(*args, **kargs):
        if func(*args, **kargs) is dict():
            part = json.dump(func(*args, **kargs))
        else:
            part = json.dumps(func(*args, **kargs))
        return part
    return newFunc

