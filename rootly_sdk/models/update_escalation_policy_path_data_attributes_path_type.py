from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesPathType = Literal["deferral", "escalation"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_PATH_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesPathType
] = {
    "deferral",
    "escalation",
}


def check_update_escalation_policy_path_data_attributes_path_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesPathType | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_PATH_TYPE_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesPathType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_PATH_TYPE_VALUES!r}"
    )
