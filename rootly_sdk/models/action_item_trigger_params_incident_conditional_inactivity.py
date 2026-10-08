from typing import Literal

ActionItemTriggerParamsIncidentConditionalInactivity = Literal["IS"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_VALUES: set[
    ActionItemTriggerParamsIncidentConditionalInactivity
] = {
    "IS",
}


def check_action_item_trigger_params_incident_conditional_inactivity(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionalInactivity | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_VALUES!r}"
    )
