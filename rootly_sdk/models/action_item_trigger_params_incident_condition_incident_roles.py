from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionIncidentRoles = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_ROLES_VALUES: set[
    ActionItemTriggerParamsIncidentConditionIncidentRoles
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


def check_action_item_trigger_params_incident_condition_incident_roles(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionIncidentRoles | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_ROLES_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionIncidentRoles, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_ROLES_VALUES!r}"
    )
