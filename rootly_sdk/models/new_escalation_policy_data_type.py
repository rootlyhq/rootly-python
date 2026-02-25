from typing import Literal, cast

NewEscalationPolicyDataType = Literal["escalation_policies"]

NEW_ESCALATION_POLICY_DATA_TYPE_VALUES: set[NewEscalationPolicyDataType] = {
    "escalation_policies",
}


def check_new_escalation_policy_data_type(value: str | None) -> NewEscalationPolicyDataType | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_DATA_TYPE_VALUES:
        return cast(NewEscalationPolicyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_DATA_TYPE_VALUES!r}")
