from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionStatus = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_STATUS_VALUES: set[ActionItemTriggerParamsIncidentConditionStatus] = {
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


def check_action_item_trigger_params_incident_condition_status(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionStatus | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_STATUS_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_STATUS_VALUES!r}"
    )
