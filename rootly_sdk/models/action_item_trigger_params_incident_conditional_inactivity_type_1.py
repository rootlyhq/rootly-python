from typing import Literal, cast

ActionItemTriggerParamsIncidentConditionalInactivityType1 = Literal["IS"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_TYPE_1_VALUES: set[
    ActionItemTriggerParamsIncidentConditionalInactivityType1
] = {
    "IS",
}


def check_action_item_trigger_params_incident_conditional_inactivity_type_1(
    value: str | None,
) -> ActionItemTriggerParamsIncidentConditionalInactivityType1 | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_TYPE_1_VALUES:
        return cast(ActionItemTriggerParamsIncidentConditionalInactivityType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_TYPE_1_VALUES!r}"
    )
