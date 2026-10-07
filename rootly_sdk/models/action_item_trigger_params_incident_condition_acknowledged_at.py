from typing import Literal

ActionItemTriggerParamsIncidentConditionAcknowledgedAt = Literal["SET", "UNSET"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_VALUES: set[
    ActionItemTriggerParamsIncidentConditionAcknowledgedAt
] = {
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_condition_acknowledged_at(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionAcknowledgedAt | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_VALUES!r}"
    )
