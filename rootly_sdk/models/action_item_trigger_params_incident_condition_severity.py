from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionSeverity = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SEVERITY_VALUES: set[ActionItemTriggerParamsIncidentConditionSeverity] = {
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


def check_action_item_trigger_params_incident_condition_severity(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionSeverity | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SEVERITY_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionSeverity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SEVERITY_VALUES!r}"
    )
