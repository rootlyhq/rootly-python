from typing import Literal

NewEscalationPolicyPathDataAttributesNotificationTypeFallback = Literal["audible", "quiet"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_FALLBACK_VALUES: set[
    NewEscalationPolicyPathDataAttributesNotificationTypeFallback
] = {
    "audible",
    "quiet",
}


def check_new_escalation_policy_path_data_attributes_notification_type_fallback(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesNotificationTypeFallback | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_FALLBACK_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_FALLBACK_VALUES!r}"
    )
