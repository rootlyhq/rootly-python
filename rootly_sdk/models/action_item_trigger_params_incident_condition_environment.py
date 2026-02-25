from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionEnvironment = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ENVIRONMENT_VALUES: set[
    ActionItemTriggerParamsIncidentConditionEnvironment
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


def check_action_item_trigger_params_incident_condition_environment(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionEnvironment | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ENVIRONMENT_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionEnvironment, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ENVIRONMENT_VALUES!r}"
    )
