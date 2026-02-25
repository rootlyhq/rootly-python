from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionMitigatedAtType1 = Literal["SET", "UNSET"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_MITIGATED_AT_TYPE_1_VALUES: set[
    ActionItemTriggerParamsIncidentConditionMitigatedAtType1
] = {
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_condition_mitigated_at_type_1(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionMitigatedAtType1 | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_MITIGATED_AT_TYPE_1_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionMitigatedAtType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_MITIGATED_AT_TYPE_1_VALUES!r}"
    )
