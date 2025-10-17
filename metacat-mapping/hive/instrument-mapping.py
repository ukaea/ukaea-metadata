import json
from pathlib import Path

import jq
import requests
from jsonschema import validate, ValidationError

equipment_dir = Path("equipment")

for equipment_file in equipment_dir.glob("*.json"):
    # Read in equipment json file
    with open(equipment_file) as file:
        instrument_data = json.load(file)

    # Map data to ukaea-instrument schema using instrument.jq
    jq_url = "https://ukaea.github.io/ukaea-metadata/metacat-mapping/hive/instrument.jq"
    jq_spec = requests.get(jq_url).text

    hive_instrument = jq.compile(jq_spec).input(instrument_data).first()

    # Validate against ukaea-instrument.schema.json
    schema_url = (
        "https://ukaea.github.io/ukaea-metadata/ukaea-schema/ukaea-instrument.schema.json"
    )
    schema = requests.get(schema_url).json()

    try:
        validate(instance=hive_instrument, schema=schema)
    except ValidationError as e:
        print(f"Validation error: {e.message}")
