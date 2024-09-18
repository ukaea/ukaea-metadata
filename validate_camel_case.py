import re
import json


 # regex to match camel case
def match_camel(s): 
    return bool(re.match(r'^[a-z]+([A-Z][a-z]+)*$', s))


def validate_camel_case(data): 
    for key, value in data: 
        if not match_camel(key): 
            return False, print("not camelcase")
        
        # check if json value is a dictionary
        if isinstance(value, dict): 
            validate_camel_case(value) # recursive check nested dictionary


def val_json_file(json_file_path):
    for json_file in json_file_path:  
        with open(json_file, 'r') as jf: 
            data = json.load(jf)
        if validate_camel_case(data): 
            return True
        else: 
            return (f"{json_file} contains non camelCase keys") 


if __name__ == "__main__": 
    val_json_file()