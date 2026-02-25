from typing import Literal, cast

ActionItemTriggerParamsIncidentActionItemConditionPriority = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_CONDITION_PRIORITY_VALUES: set[
    ActionItemTriggerParamsIncidentActionItemConditionPriority
] = {
    "ANY",
    "CONTAINS",
    "CONTAINS_ALL",
    "CONTAINS_NONE",
    "IS",
    "IS NOT",
    "NONE",
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_action_item_condition_priority(
    value: str | None,
) -> ActionItemTriggerParamsIncidentActionItemConditionPriority | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_CONDITION_PRIORITY_VALUES:
        return cast(ActionItemTriggerParamsIncidentActionItemConditionPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_CONDITION_PRIORITY_VALUES!r}"
    )
