from typing import Literal, cast

NewUserNotificationRuleDataAttributesEnabledContactTypesItem = Literal[
    "call", "device", "email", "non_critical_device", "slack", "sms"
]

NEW_USER_NOTIFICATION_RULE_DATA_ATTRIBUTES_ENABLED_CONTACT_TYPES_ITEM_VALUES: set[
    NewUserNotificationRuleDataAttributesEnabledContactTypesItem
] = {
    "call",
    "device",
    "email",
    "non_critical_device",
    "slack",
    "sms",
}


def check_new_user_notification_rule_data_attributes_enabled_contact_types_item(
    value: str | None,
) -> NewUserNotificationRuleDataAttributesEnabledContactTypesItem | None:
    if value is None:
        return None
    if value in NEW_USER_NOTIFICATION_RULE_DATA_ATTRIBUTES_ENABLED_CONTACT_TYPES_ITEM_VALUES:
        return cast(NewUserNotificationRuleDataAttributesEnabledContactTypesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_USER_NOTIFICATION_RULE_DATA_ATTRIBUTES_ENABLED_CONTACT_TYPES_ITEM_VALUES!r}"
    )
