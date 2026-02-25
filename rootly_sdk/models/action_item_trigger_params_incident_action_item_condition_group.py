from typing import Literal, cast

ActionItemTriggerParamsIncidentActionItemConditionGroup = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_CONDITION_GROUP_VALUES: set[
    ActionItemTriggerParamsIncidentActionItemConditionGroup
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


def check_action_item_trigger_params_incident_action_item_condition_group(
    value: str | None,
) -> ActionItemTriggerParamsIncidentActionItemConditionGroup | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_CONDITION_GROUP_VALUES:
        return cast(ActionItemTriggerParamsIncidentActionItemConditionGroup, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_CONDITION_GROUP_VALUES!r}"
    )
