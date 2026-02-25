from typing import Literal, cast

UserNotificationRuleListDataItemType = Literal["user_notification_rules"]

USER_NOTIFICATION_RULE_LIST_DATA_ITEM_TYPE_VALUES: set[UserNotificationRuleListDataItemType] = {
    "user_notification_rules",
}


def check_user_notification_rule_list_data_item_type(value: str | None) -> UserNotificationRuleListDataItemType | None:
    if value is None:
        return None
    if value in USER_NOTIFICATION_RULE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(UserNotificationRuleListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_NOTIFICATION_RULE_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
