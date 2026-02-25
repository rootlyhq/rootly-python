from typing import Literal, cast

EscalationPolicyResponseDataType = Literal["escalation_policies"]

ESCALATION_POLICY_RESPONSE_DATA_TYPE_VALUES: set[EscalationPolicyResponseDataType] = {
    "escalation_policies",
}


def check_escalation_policy_response_data_type(value: str | None) -> EscalationPolicyResponseDataType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_RESPONSE_DATA_TYPE_VALUES:
        return cast(EscalationPolicyResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_RESPONSE_DATA_TYPE_VALUES!r}")
