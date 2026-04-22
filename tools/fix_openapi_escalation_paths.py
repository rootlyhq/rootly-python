#!/usr/bin/env python3
"""
Post-download fix for escalation path rules in the OpenAPI spec.

openapi-python-client cannot handle inline oneOf variants with properties/required
but no $ref. This script extracts each rule variant into a named component schema
and replaces inline definitions with $ref pointers.

Also fixes upstream bug where urgency_ids array is missing items definition.

Run after downloading swagger.json, before generating:
    python tools/fix_openapi_escalation_paths.py tools/swagger.json

See: https://github.com/rootlyhq/rootly/pull/14888
"""

import json
import sys
from pathlib import Path

RULE_NAMES = {
    "alert_urgency": "escalation_path_rule_alert_urgency",
    "working_hour": "escalation_path_rule_working_hour",
    "json_path": "escalation_path_rule_json_path",
    "field": "escalation_path_rule_field",
    "service": "escalation_path_rule_service",
    "deferral_window": "escalation_path_rule_deferral_window",
}


def fix_spec(data: dict) -> int:
    schemas = data["components"]["schemas"]

    source_schema = schemas.get("new_escalation_policy_path")
    if not source_schema:
        print("new_escalation_policy_path not found in spec")
        return 1

    source_items = (
        source_schema["properties"]["data"]["properties"]["attributes"]["properties"]["rules"]["items"]
    )

    if "oneOf" not in source_items and "anyOf" not in source_items:
        print("No oneOf/anyOf found in rules items")
        return 1

    union_key = "oneOf" if "oneOf" in source_items else "anyOf"
    variants = source_items[union_key]
    extracted = 0

    for variant in variants:
        rule_type = variant.get("properties", {}).get("rule_type", {}).get("enum", [None])[0]
        if not rule_type or rule_type not in RULE_NAMES:
            continue

        ref_name = RULE_NAMES[rule_type]
        variant["type"] = "object"

        for prop in variant.get("properties", {}).values():
            if prop.get("type") == "array" and "items" not in prop:
                prop["items"] = {"type": "string"}

        schemas[ref_name] = variant
        extracted += 1

    ref_list = [{"$ref": f"#/components/schemas/{name}"} for name in RULE_NAMES.values()]

    for schema_name in ["new_escalation_policy_path", "update_escalation_policy_path"]:
        if schema_name not in schemas:
            continue
        items = schemas[schema_name]["properties"]["data"]["properties"]["attributes"]["properties"]["rules"]["items"]
        items.pop("type", None)
        items["oneOf"] = ref_list

    if "escalation_policy_path" in schemas:
        resp_items = schemas["escalation_policy_path"]["properties"]["rules"]["items"]
        resp_items.pop("type", None)
        resp_items["oneOf"] = ref_list

    print(f"Extracted {extracted} rule variants as named schemas")
    return 0


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <swagger.json>")
        return 1

    path = Path(sys.argv[1])
    data = json.loads(path.read_text())
    result = fix_spec(data)
    if result == 0:
        path.write_text(json.dumps(data))
    return result


if __name__ == "__main__":
    exit(main())
