from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionDetectedAtType1 = Literal["SET", "UNSET"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_TYPE_1_VALUES: set[
    ActionItemTriggerParamsIncidentConditionDetectedAtType1
] = {
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_condition_detected_at_type_1(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionDetectedAtType1 | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_TYPE_1_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionDetectedAtType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_TYPE_1_VALUES!r}"
    )
