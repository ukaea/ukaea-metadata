import re
import json
import argparse
from pathlib import Path
import sys


 # regex to match camel case
def match_camel_case(s): 
    # match camelCase format using regular expression
    return bool(re.match(r'^[$a-z]+([.A-Z0-9]+[a-z]*)*$', s))


def validate_camel_case(data): 
    # validate camelCase in json key
    for key, value in data.items(): 
        if not match_camel_case(key): 
            return False, f"Invalid key format (not CamelCase): {key}"
        
        # check if json value is a dictionary
        if isinstance(value, dict): 
            is_valid, message = validate_camel_case(value) # recursive check nested dictionary
            if not is_valid: 
                return False, f"{message}"
    return True, None


def val_json_file(json_file):
    # initialize empty list to store error result for invalid json file validation
    try: 
        with open(Path(json_file), 'r') as jf: 
            data = json.load(jf)
        is_valid, message = validate_camel_case(data)
        if not is_valid: 
            # append result of json file with non cameCase keys
            print(f"json file: {json_file} contains {message}")
            sys.exit(1)
        else: 
            return(f"json file: {json_file} contains valid camelCase keys")
    except json.JSONDecodeError as e: 
        # append result of invalid json file 
        print(f"Error in file {json_file}, Invalid JSON format {e}")
        sys.exit(1)
        




if __name__ == "__main__": 

    parser = argparse.ArgumentParser(description="all json files in the repository")
    parser.add_argument("json_file_paths", type=str, 
                        help="pass the paths to all json files in the repository")
    arg = parser.parse_args()
    
    validation_result = val_json_file(arg.json_file_paths)
    print(validation_result)
