from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionSummary = Literal["SET", "UNSET"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_VALUES: set[ActionItemTriggerParamsIncidentConditionSummary] = {
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_condition_summary(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionSummary | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionSummary, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_VALUES!r}"
    )
