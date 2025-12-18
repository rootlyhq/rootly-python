from typing import Literal, cast

NewIncidentDataAttributesKind = Literal[
    "backfilled", "example", "example_sub", "normal", "normal_sub", "scheduled", "scheduled_sub", "test", "test_sub"
]

NEW_INCIDENT_DATA_ATTRIBUTES_KIND_VALUES: set[NewIncidentDataAttributesKind] = {
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


def check_new_incident_data_attributes_kind(value: str) -> NewIncidentDataAttributesKind:
    if value in NEW_INCIDENT_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(NewIncidentDataAttributesKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_DATA_ATTRIBUTES_KIND_VALUES!r}")
