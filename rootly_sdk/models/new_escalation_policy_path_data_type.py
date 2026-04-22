from typing import Literal, cast

NewEscalationPolicyPathDataType = Literal["escalation_paths"]

NEW_ESCALATION_POLICY_PATH_DATA_TYPE_VALUES: set[NewEscalationPolicyPathDataType] = {
    "escalation_paths",
}


def check_new_escalation_policy_path_data_type(value: str | None) -> NewEscalationPolicyPathDataType | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_TYPE_VALUES:
        return cast(NewEscalationPolicyPathDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_TYPE_VALUES!r}")
