#!/usr/bin/env python3
"""Extract the inline data schema from nullable severity responses."""

import json
import sys
from pathlib import Path

SCHEMA_NAME = "nullable_severity_response"
DATA_SCHEMA_NAME = "nullable_severity_response_data"
DATA_SCHEMA_REF = f"#/components/schemas/{DATA_SCHEMA_NAME}"


def fix_spec(data: dict) -> int:
    schemas = data.get("components", {}).get("schemas", {})
    schema = schemas.get(SCHEMA_NAME)
    if not isinstance(schema, dict):
        print(f"{SCHEMA_NAME} not found in spec")
        return 1

    properties = schema.get("properties")
    data_schema = properties.get("data") if isinstance(properties, dict) else None
    if isinstance(data_schema, dict) and data_schema.get("$ref") == DATA_SCHEMA_REF:
        print("Nullable severity data schema already extracted")
        return 0
    if not isinstance(data_schema, dict) or data_schema.get("type") != "object":
        print(f"{SCHEMA_NAME}.data is not an inline object schema")
        return 1
    if DATA_SCHEMA_NAME in schemas:
        print(f"{DATA_SCHEMA_NAME} already exists in spec")
        return 1

    schemas[DATA_SCHEMA_NAME] = data_schema
    properties["data"] = {"$ref": DATA_SCHEMA_REF}
    print(f"Extracted {SCHEMA_NAME}.data as {DATA_SCHEMA_NAME}")
    return 0


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <swagger.json>")
        return 1

    path = Path(sys.argv[1])
    data = json.loads(path.read_text())
    result = fix_spec(data)
    if result == 0:
        path.write_text(json.dumps(data))
    return result


if __name__ == "__main__":
    sys.exit(main())
