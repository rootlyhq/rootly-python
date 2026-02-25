from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionService = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SERVICE_VALUES: set[ActionItemTriggerParamsIncidentConditionService] = {
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


def check_action_item_trigger_params_incident_condition_service(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionService | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SERVICE_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionService, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SERVICE_VALUES!r}"
    )
