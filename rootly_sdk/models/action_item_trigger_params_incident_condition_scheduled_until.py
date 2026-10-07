from typing import Literal

ActionItemTriggerParamsIncidentConditionScheduledUntil = Literal["SET", "UNSET"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_UNTIL_VALUES: set[
    ActionItemTriggerParamsIncidentConditionScheduledUntil
] = {
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_condition_scheduled_until(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionScheduledUntil | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_UNTIL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_UNTIL_VALUES!r}"
    )
