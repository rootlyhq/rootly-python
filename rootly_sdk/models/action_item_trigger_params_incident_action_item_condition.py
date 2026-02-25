from typing import Literal, cast

ActionItemTriggerParamsIncidentActionItemCondition = Literal["ALL", "ANY", "NONE"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_CONDITION_VALUES: set[
    ActionItemTriggerParamsIncidentActionItemCondition
] = {
    "ALL",
    "ANY",
    "NONE",
}


def check_action_item_trigger_params_incident_action_item_condition(
    value: str | None,
) -> ActionItemTriggerParamsIncidentActionItemCondition | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_CONDITION_VALUES:
        return cast(ActionItemTriggerParamsIncidentActionItemCondition, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_CONDITION_VALUES!r}"
    )
