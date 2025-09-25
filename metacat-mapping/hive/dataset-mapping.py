# Read in pulse json file
import json

import jq
import requests
from jsonschema import validate, ValidationError


with open("pulse.json") as file:
    pulse_data = json.load(file)

# Map data to ukaea-dataset schema using dataset.jq
jq_url = "https://raw.githubusercontent.com/ukaea/ukaea-metadata/main/metacat-mapping/hive/dataset.jq"
jq_spec = requests.get(jq_url).text

hive_dataset = jq.compile(jq_spec).input(pulse_data).first()

# Query scicat using experimentID to get contactEmail, ownerGroup and owner
hive_dataset["contactEmail"] = "<contactEmail>"
hive_dataset["ownerGroup"] = "<ownerGroup>"
hive_dataset["owner"] = "<owner>"

# Validate against ukaea-dataset.schema.json
schema_url = "https://raw.githubusercontent.com/ukaea/ukaea-metadata/main/ukaea-schema/ukaea-dataset.schema.json"
schema = requests.get(schema_url).json()

try:
    validate(instance=hive_dataset, schema=schema)
except ValidationError as e:
    print(f"Validation error: {e.message}")
