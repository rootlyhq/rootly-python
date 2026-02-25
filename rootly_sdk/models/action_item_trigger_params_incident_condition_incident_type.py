from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionIncidentType = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_TYPE_VALUES: set[
    ActionItemTriggerParamsIncidentConditionIncidentType
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


def check_action_item_trigger_params_incident_condition_incident_type(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionIncidentType | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_TYPE_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionIncidentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_TYPE_VALUES!r}"
    )
