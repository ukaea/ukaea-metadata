#!/usr/bin/env bash

for schema in ukaea-schema/diagnostics/*.schema.json ukaea-schema/facility/hive/*.schema.json; do
    
    prefix=$(basename "$schema" .schema.json)
    if [[ $schema == ukaea-schema/diagnostics/* ]]; then
        example="ukaea-schema/examples/diagnostics/${prefix}.json"
        
    else 
         example="ukaea-schema/examples/hive/${prefix}.json"
    fi

    if [ -f "$example" ]; then
        echo "validating $example against $schema .."
        jsonschema validate "$schema" "$example" || {
            echo " validation failed for schema: $schema and example: $example"
            exit 1
        }
    else
        echo "no example found for schema $schema"
    fi
done