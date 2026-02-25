from typing import Literal, cast

UpdateEscalationPolicyDataType = Literal["escalation_policies"]

UPDATE_ESCALATION_POLICY_DATA_TYPE_VALUES: set[UpdateEscalationPolicyDataType] = {
    "escalation_policies",
}


def check_update_escalation_policy_data_type(value: str | None) -> UpdateEscalationPolicyDataType | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_DATA_TYPE_VALUES:
        return cast(UpdateEscalationPolicyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_DATA_TYPE_VALUES!r}")
