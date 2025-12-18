from typing import Literal, cast

IncidentTriggerParamsIncidentKindsItem = Literal[
    "backfilled", "example", "example_sub", "normal", "normal_sub", "scheduled", "scheduled_sub", "test", "test_sub"
]

INCIDENT_TRIGGER_PARAMS_INCIDENT_KINDS_ITEM_VALUES: set[IncidentTriggerParamsIncidentKindsItem] = {
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


def check_incident_trigger_params_incident_kinds_item(value: str) -> IncidentTriggerParamsIncidentKindsItem:
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_KINDS_ITEM_VALUES:
        return cast(IncidentTriggerParamsIncidentKindsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_KINDS_ITEM_VALUES!r}"
    )
