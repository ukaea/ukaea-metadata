import json

import jq
import requests
from jsonschema import validate, ValidationError

# TODO: Loop through equipment directory
# Read in equipment json file
with open("equipment.json") as file:
    instrument_data = json.load(file)

# Map data to ukaea-dataset schema using dataset.jq
jq_url = "https://ukaea.github.io/ukaea-metadata/metacat-mapping/hive/instrument.jq"
jq_spec = requests.get(jq_url).text

hive_instrument = jq.compile(jq_spec).input(instrument_data).first()

# Validate against ukaea-dataset.schema.json
schema_url = (
    "https://ukaea.github.io/ukaea-metadata/ukaea-schema/ukaea-instrument.schema.json"
)
schema = requests.get(schema_url).json()

try:
    validate(instance=hive_instrument, schema=schema)
except ValidationError as e:
    print(f"Validation error: {e.message}")
