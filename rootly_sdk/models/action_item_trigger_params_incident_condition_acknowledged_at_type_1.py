from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionAcknowledgedAtType1 = Literal["SET", "UNSET"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_TYPE_1_VALUES: set[
    ActionItemTriggerParamsIncidentConditionAcknowledgedAtType1
] = {
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_condition_acknowledged_at_type_1(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionAcknowledgedAtType1 | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_TYPE_1_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionAcknowledgedAtType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_TYPE_1_VALUES!r}"
    )
