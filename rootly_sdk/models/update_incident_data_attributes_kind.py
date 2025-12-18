from typing import Literal, cast

UpdateIncidentDataAttributesKind = Literal[
    "backfilled", "example", "example_sub", "normal", "normal_sub", "scheduled", "scheduled_sub", "test", "test_sub"
]

UPDATE_INCIDENT_DATA_ATTRIBUTES_KIND_VALUES: set[UpdateIncidentDataAttributesKind] = {
    "backfilled",
    "example",
    "example_sub",
    "normal",
    "normal_sub",
    "scheduled",
    "scheduled_sub",
    "test",
    "test_sub",
}


def check_update_incident_data_attributes_kind(value: str) -> UpdateIncidentDataAttributesKind:
    if value in UPDATE_INCIDENT_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(UpdateIncidentDataAttributesKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_DATA_ATTRIBUTES_KIND_VALUES!r}")
