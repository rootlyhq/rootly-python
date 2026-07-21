from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionStartedAt = Literal["SET", "UNSET"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_VALUES: set[
    ActionItemTriggerParamsIncidentConditionStartedAt
] = {
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_condition_started_at(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionStartedAt | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionStartedAt, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_VALUES!r}"
    )
