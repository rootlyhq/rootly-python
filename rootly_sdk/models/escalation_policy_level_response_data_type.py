from typing import Literal, cast

EscalationPolicyLevelResponseDataType = Literal["escalation_levels"]

ESCALATION_POLICY_LEVEL_RESPONSE_DATA_TYPE_VALUES: set[EscalationPolicyLevelResponseDataType] = {
    "escalation_levels",
}


def check_escalation_policy_level_response_data_type(value: str | None) -> EscalationPolicyLevelResponseDataType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_LEVEL_RESPONSE_DATA_TYPE_VALUES:
        return cast(EscalationPolicyLevelResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_LEVEL_RESPONSE_DATA_TYPE_VALUES!r}"
    )
