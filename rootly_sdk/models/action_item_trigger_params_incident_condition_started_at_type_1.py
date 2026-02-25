from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionStartedAtType1 = Literal["SET", "UNSET"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_TYPE_1_VALUES: set[
    ActionItemTriggerParamsIncidentConditionStartedAtType1
] = {
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_condition_started_at_type_1(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionStartedAtType1 | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_TYPE_1_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionStartedAtType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_TYPE_1_VALUES!r}"
    )
