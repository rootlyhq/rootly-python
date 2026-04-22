from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesNotificationType = Literal["audible", "quiet"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesNotificationType
] = {
    "audible",
    "quiet",
}


def check_update_escalation_policy_path_data_attributes_notification_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesNotificationType | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesNotificationType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_VALUES!r}"
    )
