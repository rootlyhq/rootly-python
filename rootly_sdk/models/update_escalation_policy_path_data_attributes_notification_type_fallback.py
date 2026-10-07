from typing import Literal

UpdateEscalationPolicyPathDataAttributesNotificationTypeFallback = Literal["audible", "quiet"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_FALLBACK_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesNotificationTypeFallback
] = {
    "audible",
    "quiet",
}


def check_update_escalation_policy_path_data_attributes_notification_type_fallback(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesNotificationTypeFallback | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_FALLBACK_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_FALLBACK_VALUES!r}"
    )
