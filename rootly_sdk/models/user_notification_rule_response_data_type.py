from typing import Literal, cast

UserNotificationRuleResponseDataType = Literal["user_notification_rules"]

USER_NOTIFICATION_RULE_RESPONSE_DATA_TYPE_VALUES: set[UserNotificationRuleResponseDataType] = {
    "user_notification_rules",
}


def check_user_notification_rule_response_data_type(value: str | None) -> UserNotificationRuleResponseDataType | None:
    if value is None:
        return None
    if value in USER_NOTIFICATION_RULE_RESPONSE_DATA_TYPE_VALUES:
        return cast(UserNotificationRuleResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_NOTIFICATION_RULE_RESPONSE_DATA_TYPE_VALUES!r}")
