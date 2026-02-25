from typing import Literal, cast

NewLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType = Literal["escalation_policy", "group", "service"]

NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_ESCALATION_POLICY_TRIGGER_PARAMS_TYPE_VALUES: set[
    NewLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType
] = {
    "escalation_policy",
    "group",
    "service",
}


def check_new_live_call_router_data_attributes_escalation_policy_trigger_params_type(
    value: str | None,
) -> NewLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType | None:
    if value is None:
        return None
    if value in NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_ESCALATION_POLICY_TRIGGER_PARAMS_TYPE_VALUES:
        return cast(NewLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_LIVE_CALL_ROUTER_DATA_ATTRIBUTES_ESCALATION_POLICY_TRIGGER_PARAMS_TYPE_VALUES!r}"
    )
