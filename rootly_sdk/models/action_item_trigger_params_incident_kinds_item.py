from typing import Literal, cast

ActionItemTriggerParamsIncidentKindsItem = Literal[
    "backfilled", "example", "example_sub", "normal", "normal_sub", "scheduled", "scheduled_sub", "test", "test_sub"
]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_KINDS_ITEM_VALUES: set[ActionItemTriggerParamsIncidentKindsItem] = {
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


def check_action_item_trigger_params_incident_kinds_item(
    value: str | None,
) -> ActionItemTriggerParamsIncidentKindsItem | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_KINDS_ITEM_VALUES:
        return cast(ActionItemTriggerParamsIncidentKindsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_KINDS_ITEM_VALUES!r}"
    )
