from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionMitigatedAt = Literal["SET", "UNSET"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_MITIGATED_AT_VALUES: set[
    ActionItemTriggerParamsIncidentConditionMitigatedAt
] = {
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_condition_mitigated_at(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionMitigatedAt | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_MITIGATED_AT_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionMitigatedAt, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_MITIGATED_AT_VALUES!r}"
    )
