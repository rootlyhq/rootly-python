from typing import Literal, cast

UpdateEscalationPolicyLevelDataType = Literal["escalation_levels"]

UPDATE_ESCALATION_POLICY_LEVEL_DATA_TYPE_VALUES: set[UpdateEscalationPolicyLevelDataType] = {
    "escalation_levels",
}


def check_update_escalation_policy_level_data_type(value: str | None) -> UpdateEscalationPolicyLevelDataType | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_LEVEL_DATA_TYPE_VALUES:
        return cast(UpdateEscalationPolicyLevelDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_LEVEL_DATA_TYPE_VALUES!r}")
