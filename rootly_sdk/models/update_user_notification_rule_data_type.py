from typing import Literal, cast

UpdateUserNotificationRuleDataType = Literal["user_notification_rules"]

UPDATE_USER_NOTIFICATION_RULE_DATA_TYPE_VALUES: set[UpdateUserNotificationRuleDataType] = {
    "user_notification_rules",
}


def check_update_user_notification_rule_data_type(value: str | None) -> UpdateUserNotificationRuleDataType | None:
    if value is None:
        return None
    if value in UPDATE_USER_NOTIFICATION_RULE_DATA_TYPE_VALUES:
        return cast(UpdateUserNotificationRuleDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_USER_NOTIFICATION_RULE_DATA_TYPE_VALUES!r}")
