from typing import Literal, cast

UpdateUserNotificationRuleDataAttributesEnabledContactTypesItem = Literal[
    "call", "device", "email", "non_critical_device", "slack", "sms"
]

UPDATE_USER_NOTIFICATION_RULE_DATA_ATTRIBUTES_ENABLED_CONTACT_TYPES_ITEM_VALUES: set[
    UpdateUserNotificationRuleDataAttributesEnabledContactTypesItem
] = {
    "call",
    "device",
    "email",
    "non_critical_device",
    "slack",
    "sms",
}


def check_update_user_notification_rule_data_attributes_enabled_contact_types_item(
    value: str | None,
) -> UpdateUserNotificationRuleDataAttributesEnabledContactTypesItem | None:
    if value is None:
        return None
    if value in UPDATE_USER_NOTIFICATION_RULE_DATA_ATTRIBUTES_ENABLED_CONTACT_TYPES_ITEM_VALUES:
        return cast(UpdateUserNotificationRuleDataAttributesEnabledContactTypesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_USER_NOTIFICATION_RULE_DATA_ATTRIBUTES_ENABLED_CONTACT_TYPES_ITEM_VALUES!r}"
    )
