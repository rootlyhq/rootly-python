from typing import Literal, cast

NewEscalationPolicyPathDataAttributesPathType = Literal["deferral", "escalation"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_PATH_TYPE_VALUES: set[NewEscalationPolicyPathDataAttributesPathType] = {
    "deferral",
    "escalation",
}


def check_new_escalation_policy_path_data_attributes_path_type(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesPathType | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_PATH_TYPE_VALUES:
        return cast(NewEscalationPolicyPathDataAttributesPathType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_PATH_TYPE_VALUES!r}"
    )
