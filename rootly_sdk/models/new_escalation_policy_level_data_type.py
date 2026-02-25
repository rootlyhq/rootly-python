from typing import Literal, cast

NewEscalationPolicyLevelDataType = Literal["escalation_levels"]

NEW_ESCALATION_POLICY_LEVEL_DATA_TYPE_VALUES: set[NewEscalationPolicyLevelDataType] = {
    "escalation_levels",
}


def check_new_escalation_policy_level_data_type(value: str | None) -> NewEscalationPolicyLevelDataType | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_LEVEL_DATA_TYPE_VALUES:
        return cast(NewEscalationPolicyLevelDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_LEVEL_DATA_TYPE_VALUES!r}")
