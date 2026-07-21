from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionLabel = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_LABEL_VALUES: set[ActionItemTriggerParamsIncidentConditionLabel] = {
    "ANY",
    "CONTAINS",
    "CONTAINS_ALL",
    "CONTAINS_NONE",
    "IS",
    "IS NOT",
    "NONE",
    "SET",
    "UNSET",
}


def check_action_item_trigger_params_incident_condition_label(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionLabel | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_LABEL_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionLabel, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITION_LABEL_VALUES!r}"
    )
