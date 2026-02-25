from typing import Literal, cast

ActionItemTriggerParamsIncidentActionItemConditionStatus = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_CONDITION_STATUS_VALUES: set[
    ActionItemTriggerParamsIncidentActionItemConditionStatus
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


def check_action_item_trigger_params_incident_action_item_condition_status(
    value: str | None,
) -> ActionItemTriggerParamsIncidentActionItemConditionStatus | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_CONDITION_STATUS_VALUES:
        return cast(ActionItemTriggerParamsIncidentActionItemConditionStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_CONDITION_STATUS_VALUES!r}"
    )
