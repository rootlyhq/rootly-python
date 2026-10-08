from typing import Literal

UserNotificationRuleNotificationType = Literal["audible", "quiet"]

USER_NOTIFICATION_RULE_NOTIFICATION_TYPE_VALUES: set[UserNotificationRuleNotificationType] = {
    "audible",
    "quiet",
}


def check_user_notification_rule_notification_type(value: str | None) -> UserNotificationRuleNotificationType | None:
    if value is None:
        return None
    if value in USER_NOTIFICATION_RULE_NOTIFICATION_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_NOTIFICATION_RULE_NOTIFICATION_TYPE_VALUES!r}")
