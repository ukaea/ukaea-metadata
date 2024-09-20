import re
import json
import argparse
from pathlib import Path


 # regex to match camel case
def match_camel_case(s): 
    # match camelCase format using regular expression
    return bool(re.match(r'^[$a-z]+([A-Z][a-z]+)*$', s))


def validate_camel_case(data): 
    # validate camelCase in json key
    for key, value in data.items(): 
        if not match_camel_case(key): 
            return False, f"Invalid key format (not CamelCase): {key}"
        
        # check if json value is a dictionary
        if isinstance(value, dict): 
            is_valid, message = validate_camel_case(value) # recursive check nested dictionary
            if not is_valid: 
                return False, f"Nested error: {message}"
    return True, None


def val_json_file(json_file_paths):
    # initialize empty list to store error result for invalid json file validation
    invalid_result = []
    for json_file in json_file_paths.split(" "):  
        print(json_file)
        try: 
            with open(Path(json_file), 'r') as jf: 
                data = json.load(jf)
            is_valid, message = validate_camel_case(data)
            if not is_valid: 
                # append result of json file with non cameCase keys
                invalid_result.append(f"{json_file} - {message}")
        except json.JSONDecodeError as e: 
            # append result of invalid json file 
            invalid_result.append(f"Error in file {json_file}, Invalid JSON format {e}")

    # return 
    if len(invalid_result) > 0: 
        return "\n".join(invalid_result)
    else: 
        return True 



if __name__ == "__main__": 

    parser = argparse.ArgumentParser(description="all json files in the repository")
    parser.add_argument("json_file_paths", type=str, 
                        help="pass the paths to all json files in the repository")
    arg = parser.parse_args()
    
    validation_result = val_json_file(arg.json_file_paths)
    print(validation_result)