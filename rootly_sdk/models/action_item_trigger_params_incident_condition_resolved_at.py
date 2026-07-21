from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionResolvedAt = Literal["SET", "UNSET"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_RESOLVED_AT_VALUES: set[
    ActionItemTriggerParamsIncidentConditionResolvedAt
] = {
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_condition_resolved_at(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionResolvedAt | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_RESOLVED_AT_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionResolvedAt, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_RESOLVED_AT_VALUES!r}"
    )
