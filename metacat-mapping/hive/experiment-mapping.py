import json

import jq
import requests
from jsonschema import validate, ValidationError


# Read in experiment json file
with open("experiment.json") as file:
    experiment_data = json.load(file)

# Map data to ukaea-dataset schema using dataset.jq
jq_url = "https://raw.githubusercontent.com/ukaea/ukaea-metadata/main/metacat-mapping/hive/experiment.jq"
jq_spec = requests.get(jq_url).text

hive_experiment = jq.compile(jq_spec).input(experiment_data).first()

# Validate against ukaea-dataset.schema.json
schema_url = "https://raw.githubusercontent.com/ukaea/ukaea-metadata/main/ukaea-schema/ukaea-experiment.schema.json"
schema = requests.get(schema_url).json()

try:
    validate(instance=hive_experiment, schema=schema)
except ValidationError as e:
    print(f"Validation error: {e.message}")
