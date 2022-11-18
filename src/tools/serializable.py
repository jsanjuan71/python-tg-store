import json

def modelToJson(model):
    return json.dumps(
        model, 
        default=lambda o: o.__dict__, 
        sort_keys=True, 
        indent=4)