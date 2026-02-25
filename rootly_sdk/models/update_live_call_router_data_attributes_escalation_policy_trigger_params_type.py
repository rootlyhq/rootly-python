from typing import Literal, cast

UpdateLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType = Literal["EscalationPolicy", "Group", "Service"]

UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_ESCALATION_POLICY_TRIGGER_PARAMS_TYPE_VALUES: set[
    UpdateLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType
] = {
    "EscalationPolicy",
    "Group",
    "Service",
}


def check_update_live_call_router_data_attributes_escalation_policy_trigger_params_type(
    value: str | None,
) -> UpdateLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType | None:
    if value is None:
        return None
    if value in UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_ESCALATION_POLICY_TRIGGER_PARAMS_TYPE_VALUES:
        return cast(UpdateLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_ESCALATION_POLICY_TRIGGER_PARAMS_TYPE_VALUES!r}"
    )
