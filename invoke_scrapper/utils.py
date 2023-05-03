from functools import wraps
import json

def jsonify(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return json.dumps(res)
    return wrapper
