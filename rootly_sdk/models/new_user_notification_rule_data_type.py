from typing import Literal, cast

NewUserNotificationRuleDataType = Literal["user_notification_rules"]

NEW_USER_NOTIFICATION_RULE_DATA_TYPE_VALUES: set[NewUserNotificationRuleDataType] = {
    "user_notification_rules",
}


def check_new_user_notification_rule_data_type(value: str | None) -> NewUserNotificationRuleDataType | None:
    if value is None:
        return None
    if value in NEW_USER_NOTIFICATION_RULE_DATA_TYPE_VALUES:
        return cast(NewUserNotificationRuleDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_USER_NOTIFICATION_RULE_DATA_TYPE_VALUES!r}")
