from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionSummaryType1 = Literal["SET", "UNSET"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_TYPE_1_VALUES: set[
    ActionItemTriggerParamsIncidentConditionSummaryType1
] = {
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_condition_summary_type_1(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionSummaryType1 | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_TYPE_1_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionSummaryType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_TYPE_1_VALUES!r}"
    )
