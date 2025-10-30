import json

import jq

# Read in experiment json file
with open("out-experiment.json") as file:
    experiment_data = json.load(file)

# Map data to ukaea-dataset schema using dataset.jq
jq_url = "https://ukaea.github.io/ukaea-metadata/metacat-mapping/hive/experiment.jq"
# jq_spec = requests.get(jq_url).text

with open("reverse-metacat-mapping/hive/experiment.jq") as jf:
    jq_spec = jf.read()

hive_experiment = jq.compile(jq_spec).input(experiment_data).first()
print(hive_experiment)
# with open("out-experiment.json", "w") as fp:
#     json.dump(hive_experiment, fp)

# # Validate against ukaea-dataset.schema.json
# schema_url = (
#     "https://ukaea.github.io/ukaea-metadata/ukaea-schema/ukaea-experiment.schema.json"
# )
# schema = requests.get(schema_url).json()

# try:
#     validate(instance=hive_experiment, schema=schema)
# except ValidationError as e:
#     print(f"Validation error: {e.message}")
# except ValidationError as e:
#     print(f"Validation error: {e.message}")
