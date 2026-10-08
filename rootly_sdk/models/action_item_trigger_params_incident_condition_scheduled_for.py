from typing import Literal

ActionItemTriggerParamsIncidentConditionScheduledFor = Literal["SET", "UNSET"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_FOR_VALUES: set[
    ActionItemTriggerParamsIncidentConditionScheduledFor
] = {
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_condition_scheduled_for(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionScheduledFor | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_FOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_FOR_VALUES!r}"
    )
