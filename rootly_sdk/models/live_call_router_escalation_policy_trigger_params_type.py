from typing import Literal, cast

LiveCallRouterEscalationPolicyTriggerParamsType = Literal["EscalationPolicy", "Group", "Service"]

LIVE_CALL_ROUTER_ESCALATION_POLICY_TRIGGER_PARAMS_TYPE_VALUES: set[LiveCallRouterEscalationPolicyTriggerParamsType] = {
    "EscalationPolicy",
    "Group",
    "Service",
}


def check_live_call_router_escalation_policy_trigger_params_type(
    value: str | None,
) -> LiveCallRouterEscalationPolicyTriggerParamsType | None:
    if value is None:
        return None
    if value in LIVE_CALL_ROUTER_ESCALATION_POLICY_TRIGGER_PARAMS_TYPE_VALUES:
        return cast(LiveCallRouterEscalationPolicyTriggerParamsType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIVE_CALL_ROUTER_ESCALATION_POLICY_TRIGGER_PARAMS_TYPE_VALUES!r}"
    )
