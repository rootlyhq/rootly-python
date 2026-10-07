from typing import Literal

EscalationPolicyPathNotificationTypeFallback = Literal["audible", "quiet"]

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_FALLBACK_VALUES: set[EscalationPolicyPathNotificationTypeFallback] = {
    "audible",
    "quiet",
}


def check_escalation_policy_path_notification_type_fallback(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeFallback | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_FALLBACK_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_FALLBACK_VALUES!r}"
    )
