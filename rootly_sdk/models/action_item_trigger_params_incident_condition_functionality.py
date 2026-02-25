from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionFunctionality = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_FUNCTIONALITY_VALUES: set[
    ActionItemTriggerParamsIncidentConditionFunctionality
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


def check_action_item_trigger_params_incident_condition_functionality(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionFunctionality | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_FUNCTIONALITY_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionFunctionality, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_FUNCTIONALITY_VALUES!r}"
    )
