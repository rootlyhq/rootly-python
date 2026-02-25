from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionSubStatus = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUB_STATUS_VALUES: set[
    ActionItemTriggerParamsIncidentConditionSubStatus
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


def check_action_item_trigger_params_incident_condition_sub_status(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionSubStatus | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUB_STATUS_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionSubStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUB_STATUS_VALUES!r}"
    )
