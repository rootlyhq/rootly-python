from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionDetectedAt = Literal["SET", "UNSET"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_VALUES: set[
    ActionItemTriggerParamsIncidentConditionDetectedAt
] = {
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_condition_detected_at(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionDetectedAt | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionDetectedAt, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_VALUES!r}"
    )
