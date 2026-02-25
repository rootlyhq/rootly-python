from typing import Literal, cast

EscalationPolicyPathResponseDataType = Literal["escalation_paths"]

ESCALATION_POLICY_PATH_RESPONSE_DATA_TYPE_VALUES: set[EscalationPolicyPathResponseDataType] = {
    "escalation_paths",
}


def check_escalation_policy_path_response_data_type(value: str | None) -> EscalationPolicyPathResponseDataType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RESPONSE_DATA_TYPE_VALUES:
        return cast(EscalationPolicyPathResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RESPONSE_DATA_TYPE_VALUES!r}")
