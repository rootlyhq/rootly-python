from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionVisibility = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_VISIBILITY_VALUES: set[
    ActionItemTriggerParamsIncidentConditionVisibility
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


def check_action_item_trigger_params_incident_condition_visibility(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionVisibility | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_VISIBILITY_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionVisibility, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_VISIBILITY_VALUES!r}"
    )
