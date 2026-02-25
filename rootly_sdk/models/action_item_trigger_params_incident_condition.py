from typing import Literal, cast

ActionItemTriggerParamsIncidentCondition = Literal["ALL", "ANY", "NONE"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_VALUES: set[ActionItemTriggerParamsIncidentCondition] = {
    "ALL",
    "ANY",
    "NONE",
}


def check_action_item_trigger_params_incident_condition(value: str | None) -> ActionItemTriggerParamsIncidentCondition | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_VALUES:
        return cast(ActionItemTriggerParamsIncidentCondition, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_VALUES!r}"
    )
