import json

import jq
import requests

# Read in pulse json file
with open("out-dataset.json") as file:
    pulse_data = json.load(file)


# Map data to ukaea-dataset schema using dataset.jq
jq_url = "https://ukaea.github.io/ukaea-metadata/metacat-mapping/hive/dataset.jq"
jq_spec = requests.get(jq_url).text

with open("reverse-metacat-mapping/hive/dataset.jq") as jd:
    jq_spec = jd.read()


hive_pulse = jq.compile(jq_spec).input(pulse_data).first()
