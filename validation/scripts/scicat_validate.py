import json
from jsonschema import FormatChecker, validators
from pathlib import Path


def get_schema(filename):

    BASE_PATH = Path('.').resolve()
    SCHEMA_PATH = BASE_PATH / 'schemas'
    with (SCHEMA_PATH/filename).open() as f_schema:
        schema = json.load(f_schema)
    return schema


if __name__ == '__main__':

    from referencing import Registry, Resource
    registry = Registry()

    BASE_PATH = Path('.').resolve()
    with (BASE_PATH/'toplevel.schema.json').open() as f_toplevel:
        toplevel_schema = json.load(f_toplevel)
    with (BASE_PATH/'examples/test.json').open() as f:
        json_to_validate = json.load(f)

    # resource = Resource.from_contents(toplevel_schema)
    # registry = resource @ initial_registry

    sub_schema_filenames = [
            'scicat.dataset.schema.json',
            'scicat.dataset-raw.schema.json',
            'scicat.dataset-derived.schema.json',
    ]
    for sub_schema_str in sub_schema_filenames:
        sub_schema = get_schema(sub_schema_str)
        temp_resource = Resource.from_contents(sub_schema)
        registry = temp_resource @ registry

    print('#####################################')
    print(registry.contents('urn:scicat:dataset-schema'))
    print('#####################################')
    print(registry.contents('urn:scicat:dataset-raw-schema'))
    print('#####################################')
    print(registry.contents('urn:scicat:dataset-derived-schema'))

    validator = validators.Draft202012Validator(
        schema=toplevel_schema,
        # format_checker=FormatChecker(),
        registry=registry,
    )

    # print(validator.schema)

    data_to_validate = {
        "person": {
            "name": "John",
            "age": 30
        },
        "address": {
            "street": "123 Main St",
            "city": "Example City",
            "zipcode": "12345"
        }
    }

    validator.validate(
        data_to_validate
    )
