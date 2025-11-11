import json
from pathlib import Path

import jq
import requests
from jsonschema import ValidationError, validate

# Read in pulse json file
with open("pulse.json") as file:
    pulse_data = json.load(file)

pulse_directory = Path(
    f"/mnt/HIVE/{pulse_data['experimentNumber']}/{pulse_data['sampleNumber']}/{pulse_data['pulseNumber']}"
)

# Query metacat using experimentID to get contactEmail, ownerGroup and owner
contact_email = "<contactEmail>"
owner_group = "<ownerGroup>"
owner = "<owner>"

# Map data to ukaea-dataset schema using dataset.jq
jq_url = "https://ukaea.github.io/ukaea-metadata/metacat-mapping/hive/dataset.jq"
jq_spec = requests.get(jq_url).text

hive_pulse = jq.compile(jq_spec).input(pulse_data).all()

for dataset in hive_pulse:
    dataset["contactEmail"] = contact_email
    dataset["ownerGroup"] = owner_group
    dataset["owner"] = owner

    # Validate against ukaea-dataset.schema.json
    schema_url = (
        "https://ukaea.github.io/ukaea-metadata/ukaea-schema/ukaea-dataset.schema.json"
    )
    schema = requests.get(schema_url).json()

    try:
        validate(instance=dataset, schema=schema)
    except ValidationError as e:
        print(f"Validation error: {e.message}")

    output_file = (
        pulse_directory
        / Path(f"{dataset['instrument']}")
        / f"{dataset['instrument']}-metadata.json"
    )

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w") as file:
        json.dump(dataset, file, indent=4)
