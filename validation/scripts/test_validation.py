import json
from jsonschema import FormatChecker, Draft202012Validator
from pathlib import Path

from referencing import Registry, Resource
initial_registry = Registry()

BASE_PATH = Path('.').resolve()
with (BASE_PATH/'toplevel.schema.json').open() as f_toplevel:
    toplevel_schema = json.load(f_toplevel)

# resource = Resource.from_contents(toplevel_schema)
# registry = resource @ initial_registry

with (BASE_PATH/'schemas/scicat.dataset.schema.json').open() as f_file1:
    person_schema = json.load(f_file1)

resource = Resource.from_contents(person_schema)
registry = resource @ initial_registry

# with (BASE_PATH/'schemas/address_schema.json').open() as f_file2:
    # address_schema = json.load(f_file2)

# resource = Resource.from_contents(address_schema)
# registry = resource @ registry

validator = Draft202012Validator(
    toplevel_schema,
    registry=registry,
)

with (BASE_PATH/'../json_tests/examples/person_test.json').open() as f_file:
    data_to_validate = json.load(f_file)

validator.validate(data_to_validate)
