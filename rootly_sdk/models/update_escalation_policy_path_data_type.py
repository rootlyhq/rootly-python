from typing import Literal, cast

UpdateEscalationPolicyPathDataType = Literal["escalation_paths"]

UPDATE_ESCALATION_POLICY_PATH_DATA_TYPE_VALUES: set[UpdateEscalationPolicyPathDataType] = {
    "escalation_paths",
}


def check_update_escalation_policy_path_data_type(value: str | None) -> UpdateEscalationPolicyPathDataType | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_TYPE_VALUES:
        return cast(UpdateEscalationPolicyPathDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_TYPE_VALUES!r}")
